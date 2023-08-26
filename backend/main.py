from fastapi import FastAPI
import openai
import os
from dotenv import load_dotenv

from bookie import Bookie
from schemas.ai_response import AIResponse
from schemas.question import Question
from functions import functions
from callables import callables
from init import initial_state

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
app = FastAPI()


@app.get('/ask', response_model=AIResponse)
async def get_completion(question: Question):

    bookie = Bookie(
        model_type='gpt-3.5-turbo',
        functions=functions,
        callables=callables,
        history=[{"role": "system", "content": initial_state}]
    )

    bookie.add_to_history(role='user', content=question.text)
    response_message = bookie.call_model()

    if response_message.get("function_call"):
        return bookie.handle_function_call(response_message=response_message)

    return bookie.handle_normal_response(response_message=response_message)
