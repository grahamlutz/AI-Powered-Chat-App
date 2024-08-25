# Advanced AI-Powered Chat Application

A sophisticated chat application that leverages the power of LangChain and ChatGPT to create a highly interactive and intelligent conversational experience. The app goes far beyond simple text generation, incorporating advanced features and production-ready techniques.

## Key features of my chat app include:

1. **Complex text generation pipelines** that can incorporate external information, allowing the chatbot to access and utilize a wide range of data sources.

2. **Reusable configuration components** that can be easily reassembled, making the app highly flexible and adaptable to different use cases.

3. **Self-improving text generation capabilities** - A user feedback system with upvotes and downvotes, which helps refine and improve the chatbot's responses over time.

4. **Comprehensive observability and tracing capabilities**, providing insights into user interactions and system performance.

5. **Distributed processing for efficient text generation**, ensuring smooth performance even under heavy loads.

6. **Implementation of conversational memory**, allowing the chatbot to store, retrieve, and summarize previous messages for more context-aware interactions.

7. **Semantic search functionality using embeddings**, enabling more accurate and relevant responses.

8. **Retrieval Augmented Generation (RAG)** to ensure accuracy and efficiency.

9. **Integration with vector databases** like ChromaDB and Pinecone for efficient storage and retrieval of embeddings.

10. **Advanced context management using retrievers** to refine, reduce, and rank relevant information.

11. **Server-to-browser text streaming** for a more dynamic and responsive user experience.

The centerpiece of the app is a "Chat-with-a-PDF" feature, which allows users to upload PDF documents and engage in conversations about their content. The app can understand and answer questions about the uploaded documents, making it a powerful tool for information retrieval and analysis.

To ensure optimal performance, I've implemented distributed processing using Celery and Redis, allowing the app to handle multiple requests efficiently.

Throughout the development process, I focused on creating production-ready, scalable solutions that can be easily maintained and expanded. The modular architecture of the app, built using LangChain's chains and components, allows for easy modifications and additions of new features.

This chat app represents a comprehensive implementation of advanced AI-driven conversational technology, showcasing the potential of integrating ChatGPT into real-world applications.

## First Time Setup

## Using Pipenv [Recommended]

```
# Install dependencies
pipenv install

# Create a virtual environment
pipenv shell

# Initialize the database
flask --app app.web init-db

```

## Using Venv [Optional]

These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv.

```
# Create the venv virtual environment
python -m venv .venv

# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
flask --app app.web init-db
```

# Running the app [Pipenv]

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
flask --app app.web init-db
```

# Running the app [Venv]

_These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv._

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
flask --app app.web init-db
```
