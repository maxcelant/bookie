import openai
from backend.schemas.ai_response import AIResponse


class Bookie:
    def __init__(self, model_type='gpt-3.5-turbo', functions=[], callables={}, history=[]):
        self.model_type = model_type
        self.functions = functions
        self.callables = callables
        self.history = history

    def add_to_history(self, role, content):
        self.history.append({"role": role, "content": content})

    def call_model(self):
        completion = openai.ChatCompletion.create(
            model=self.model_type,
            messages=self.history,
            functions=self.functions,
            function_call="auto"
        )
        return completion.choices[0].message

    def handle_function_call(self, response_message):
        function_name = response_message.function_call.name

        function_response = self.callables[function_name]()

        self.history.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response
            }
        )

        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.history,
        )
        self.history.append(
            {"role": "assistant", "content": response_message.content})

        return AIResponse(text=second_response.choices[0].message.content)

    def handle_normal_response(self, response_message):
        self.history.append(
            {"role": "assistant", "content": response_message.content})
        return AIResponse(text=response_message.content)
