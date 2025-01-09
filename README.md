
## Introduction

This is a RAG application that uses NLP and vector storage to answer questions from PDF documents accurately, leveraging LangChain, Chroma, FAISS, and HuggingFace.


## Run Locally

Clone the project

```bash
  git clone https://github.com/tradaokamsa/rag-application.git
```

Go to the project directory

```bash
  cd rag-application
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Go to `/data` to add PDFs

```bash
  cd data
```
Run `download.py` to install examples *or* creating folder `/files` then add your PDFs 
```bash
  python3 download.py
```

Start the server
```bash
  cd ..
  uvicorn app:app --reload
```



## Tech Stack

**Backend:** `FastAPI` for building the API

**NLP:** `LangChain` framework, `HuggingFace` for loading pre-trained models and generating embeddings

**Vector Storage:** `Chroma` for embedding storage and retrieval


## Demo

![](https://private-user-images.githubusercontent.com/97043830/401642396-5b649ea0-fdc0-4067-a49b-a055197341d1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzY0NDQ3OTgsIm5iZiI6MTczNjQ0NDQ5OCwicGF0aCI6Ii85NzA0MzgzMC80MDE2NDIzOTYtNWI2NDllYTAtZmRjMC00MDY3LWE0OWItYTA1NTE5NzM0MWQxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAxMDklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMTA5VDE3NDEzOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI1ODFkOWI2YjBhN2FlNDIzZTE0Njc4NDljYjJhYmVmMzRhYTI0ZWMzZmE0YTZkM2ZiNGI4NDQzNjc0YTI5MGEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.eQZXoxBh_HJ-QARdUYfEA1mwq0Xq7VcmNIQ9_VJrBfA)

