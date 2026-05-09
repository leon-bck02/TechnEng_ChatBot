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
        self.messages : list[dict[str, str]] = [
            {
                "role": "system",
                "content": self.system_prompt
            },
        ]

    def get_conversation_history(self) -> list[dict[str, str]]:
        return self.messages

    def get_llm_response(self, user_input: str) -> str: 
        
        # This only saves of what the user has said
        self.get_conversation_history().append(
            {
                "role": "user",
                "content": user_input
            }
        )

        llm_response = self.client.chat.completions.create(
            model = self.model,
            messages=self.messages,
            max_completion_tokens = 6000
        )

        response = llm_response.choices[0].message.content

        # This now saves the response of the LLM into the dict
        self.get_conversation_history().append(
            {
                "role": "assistant",
                "content": response
            }
        )

        return response
