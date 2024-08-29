from langchain_community.document_loaders import JSONLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

import json
from pathlib import Path

def process_data():
    
    # Load the review data
    with open(Path("reviews.json"), 'r') as file:
        data = json.load(file)
    
    loader = JSONLoader('reviews.json', jq_schema='.reviews[]', text_content=False)
    split_data = loader.load_and_split(RecursiveCharacterTextSplitter())
    
    print(len(split_data))
    
    ids = [review['professor'] for review in data['reviews']]
    
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    # embedding_function = HuggingFaceEmbeddings(model="sentence-transformers/all-mpnet-base-v2")
    
    # create chroma database with IDs
    Chroma.from_documents(documents=split_data, collection_name='reviews', persist_directory='db', embedding=embedding_function, ids=ids)