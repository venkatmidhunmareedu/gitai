import ollama 
from .utils import chat,list_models
import json

def generate_name() -> str:
    with open('gitai.config.json') as f:
        config = json.load(f)
    return chat(config.get('prompts').get('name'))