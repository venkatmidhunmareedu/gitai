from ollama import Client
import json

client = Client(host='http://localhost:11434')

model='gemma:2b'

with open('gitai.config.json') as f:
    config = json.load(f)
    if config.get('model') is not None:
        model = config.get('model')
    else :
        model = 'gemma:2b'



def chat(message : str,model=model) -> str:
    response = client.chat(model=model, messages=[
      {
        'role': 'user',
        'content': message,
      },
    ])
    
    # stringify the response
    return response['message']['content']

def list_models() -> list[str]:
    return client.list()

