import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key
response = openai.Completion.create(
    engine="davinci",
    prompt="Translate the following from english to spanish: 'hello world'",
    max_tokens=10
)

print(response.choices[0].text)