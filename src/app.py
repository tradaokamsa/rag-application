import os
os.environ['TOKENIZERS_PARALLELISM'] = 'false'

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from src.base.llm_model import get_hf_llm
# from src.rag.main import build_rag_chain, InputQA, OutputQA

# llm = get_hf_llm(temperature=0.9)
# genai_docs = "./data/files"

# genai_chain = build_rag_chain(llm, data_dir=genai_docs, data_type="pdf")

app = FastAPI(
    title="LangChain Server",
    description="A simple API server for Q&A using LangChain",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/check")
async def check():
    return {"status": "ok"}

# @app.post("/qa", response_model=OutputQA)
# async def qa(input_qa: InputQA):
#     answer = genai_chain.invoke(input_qa.question)
#     return {"answer": answer}