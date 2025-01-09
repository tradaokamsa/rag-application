import torch
# from transformers import BitsAndBytesConfig
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface.llms import HuggingFacePipeline

# quantization_config = BitsAndBytesConfig(load_in_4bit=True)

def get_hf_llm(model_name: str = "facebook/opt-125m",
               max_new_token: int = 1024,
               **kwargs):
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name, 
        # quantization_config=quantization_config,
        # low_cpu_mem_usage=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=max_new_token,
        pad_token_id=tokenizer.eos_token_id,
        device_map="auto"
    )
    
    llm = HuggingFacePipeline(
        pipeline=model_pipeline,
        model_kwargs=kwargs
    )

    return llm
    