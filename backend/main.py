from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request
import openai
import os

from bookie import Bookie
from schemas.ai_response import AIResponse
from schemas.question import Question
from functions import functions
from callables import callables
from init import initial_state


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
secret_key = os.getenv('MIDDLEWARE_SECRET')
app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=secret_key)


def get_session(request: Request):
    return request.session


@app.get('/ask', response_model=AIResponse)
async def get_completion(question: Question, session: dict = Depends(get_session)):

    conversation_history = session.get(
        "history", [{"role": "system", "content": initial_state}])

    conversation_history = conversation_history[:-1]

    bookie = Bookie(
        model_type='gpt-3.5-turbo',
        functions=functions,
        callables=callables,
        history=conversation_history
    )

    bookie.add_to_history(role='user', content=question.text)
    response_message = bookie.call_model()

    if response_message.get("function_call"):
        response = bookie.handle_function_call(
            response_message=response_message)
    else:
        response = bookie.handle_normal_response(
            response_message=response_message)

    session["history"] = bookie.get_history()

    return response
