from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your OpenAI API key
# api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI LLM wrapper from LangChain
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# Test prompt
response = llm.invoke("Write a one-line motivational quote.")
print(response)
