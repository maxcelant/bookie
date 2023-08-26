from fastapi import FastAPI
import openai
from pydantic import BaseModel

from init import initial_state
from flights import get_flights

openai.api_key = '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'
app = FastAPI()

conversation_history = [{"role": "system", "content": initial_state}]

functions = [
    {
        "name": "get_flights",
                "description": "Get the data of the current flights occuring (this is not real data)",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
    }
]


class Question(BaseModel):
    text: str


@app.get('/ask', response_model=AIResponse)
async def get_completion(question: Question):

    conversation_history.append(
        {"role": "user", "content": question.text})

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=conversation_history,
        functions=functions,
        function_call="auto"
    )

    response_message = completion.choices[0].message

    if response_message.get("function_call"):
        function_name = response_message.function_call.name

        if function_name == "get_flights":
            function_response = get_flights()

            conversation_history.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response
                }
            )

            second_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation_history,
            )
            conversation_history.append(
                {"role": "assistant", "content": response_message.content})
            return AIResponse(text=second_response.choices[0].message.content)

    conversation_history.append(
        {"role": "assistant", "content": response_message.content})
    return AIResponse(text=response_message.content)
