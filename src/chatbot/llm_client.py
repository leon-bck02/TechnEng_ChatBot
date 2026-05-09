from openai import AzureOpenAI
from .config import OPENAI_API_KEY, ENDPOINT, MODEL
from .prompts import SYSTEM_PROMPT


class LLMClient:

    def __init__(self):
        self.client = AzureOpenAI(
            api_key=OPENAI_API_KEY,
            azure_endpoint=ENDPOINT,
            api_version="2024-12-01-preview",
        )
        self.model = MODEL    
        self.system_prompt = SYSTEM_PROMPT    

    def get_llm_response(self, user_input: str) -> str:
        llm_response = self.client.chat.completions.create(
            model = self.model,
            messages=[
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": user_input,
            }
            ],
            max_completion_tokens = 12000
        )

        return llm_response.choices[0].message.content
