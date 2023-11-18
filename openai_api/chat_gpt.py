from openai import OpenAI
from pathlib import os
from dotenv import load_dotenv


load_dotenv()

def get_texto_descritivo(local):

  client = OpenAI(
      api_key= os.getenv("OPENAI_API_KEY"),
  )

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": f"Faça um resumo sobre {local} enfatizando o porque este lugar é incrível. Utilize uma linguagem informal e até 100 caracteres no máximo em cada parágrafo. Crie 2 parágrafos neste resumo."}
    ]
  )

  return completion.choices[0].message.content
