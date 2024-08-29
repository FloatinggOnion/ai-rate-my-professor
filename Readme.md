### Rate My Professor Backend
This is a RAG api that allows users to search professors with natural language queries. It uses the HuggingFace API to generate embeddings for the professor data and the user's query, and then uses similarity search to find the most relevant professors. The backend is built using FastAPI and the frontend is built using React.

### Running Instructions
1. Clone the repository and navigate to the backend directory.
2. Install the required dependencies using `pipenv install`.
3. Set up the environment variables by creating a `.env` file with the variables as showng in `.env.example`.
4. Run the backend server using `uvicorn main:app --reload` or `fastapi dev`.
5. To create the db, navigate to `localhost:8000/process` or `localhost:8000/docs` and click the `Try it out` button and then `Execute` button to run the endpoint. This will create the db and populate it with the professor data. This may take a while to complete.
6. Navigate to the frontend directory and install the required dependencies using `npm install`.
7. Run the frontend server using `npm run dev`.
8. Open your browser and navigate to `http://localhost:5173` to view the application.

### Technologies Used
* FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
* HuggingFace Transformers: A library for state-of-the-art Natural Language Processing (NLP) for PyTorch, TensorFlow, and JAX.
* SentenceTransformers: A library for generating sentence embeddings using pre-trained transformer models. It provides a simple and easy-to-use API for generating embeddings for sentences and paragraphs, and for performing semantic search and clustering tasks.
* ReactJS: A JavaScript library for building user interfaces, specifically for single-page applications. It allows developers to create reusable UI components that can be easily composed to build complex UIs. ReactJS uses a virtual DOM to efficiently update and render components, and it supports server-side rendering and code splitting to improve performance and SEO.
* TailwindCSS: A utility-first CSS framework for rapidly building custom user interfaces. It provides a set of pre-defined utility classes that can be used to style HTML elements quickly and easily, without having to write custom CSS. TailwindCSS also supports dark mode and responsive design, and it can be easily integrated with other front-end frameworks and libraries.
* Vite: A build tool that aims to provide a faster and leaner development experience for modern web projects. It uses native ES modules for faster startup times and hot module replacement (HMR) for faster rebuild times. Vite also supports TypeScript, JSX, and CSS modules out of the box, and it can be easily integrated with other front-end frameworks and libraries.

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

### Contact
If you have any questions or concerns, please contact me at [my email](mailto:jesseosems123@gmail.com).