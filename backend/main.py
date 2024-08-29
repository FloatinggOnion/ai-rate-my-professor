from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse
import google.generativeai as genai
from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage

from utils import process_data

from dotenv import load_dotenv
import json
import os

from models import Query

load_dotenv()

API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

PROMPT_TEMPLATE = '''
    You are a rate my professor agent to help students find classes, that takes in user questions and answers them. For every user question, the top 3 professors that match the user question are returned. Use them to answer the question if needed based on the context below:
    {context}

    ---

    Answer this question based on the above context: {question}
'''

genai.configure(api_key=API_KEY)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/process")
async def process():
    process_data()
    return {"status": "success"}


@app.post("/query", status_code=status.HTTP_200_OK)
async def query_item(query: Query):
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="db",embedding_function=embedding_function, collection_name='reviews')
    results = db.similarity_search(query.query, k=query.neighbours)
    
    if len(results) == 0:
        return Response({'response': 'Unable to find matching results'}, status_code=status.HTTP_200_OK)
    
    formatted_prompt = PROMPT_TEMPLATE.format(
        context="\n".join(doc.page_content for doc in results),
        question=query.query
    )
    
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=formatted_prompt)
    
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )
    
    response = chat.send_message(query.query)

    print(response.text)

    formatted_response = {'answer': response.text}

    return JSONResponse({'response': formatted_response}, status_code=status.HTTP_200_OK)