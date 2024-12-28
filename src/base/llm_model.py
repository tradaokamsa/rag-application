import torch
from transformers import BitsAndBytesConfig
from transformers import AutoTokenizer, AutoModelForCasualLM
from transformers import pipeline
from langchain.llms.huggingface_pipeline import HuggingfacePipeline

nf4_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",  
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16
)