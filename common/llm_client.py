from enum import Enum
from typing import Callable, Union, Tuple
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.base import BasePromptTemplate
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.chat_models.perplexity import ChatPerplexity
from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema import StrOutputParser


MENDABLE_API_KEY = "MENDABLE_API_KEY"
RESPELL_API_KEY = "RESPELL_API_KEY"
OPENAI_API_KEY = "OPENAI_API_KEY"
GEMINI_API_KEY = "GEMINI_API_KEY"

_SYSTEM_MESSAGE = (
    "You Are User Experience Virtual Assistant Agent Over Digital Marketing Platform .Your task is to guide and answer all users questions in order to improve UX, It has to be clear and concise. \n"
    "I Will provide you with some keywords my search related to .\n"
    "Provide any kind of resources help ,suggestions and more navigation facilities over the platform"
)

_REWRITE_PROMPT: BasePromptTemplate = ChatPromptTemplate.from_messages(
    [
        SystemMessage(_SYSTEM_MESSAGE),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)


class Provider(Enum):
    MENDABLE = "mendable"
    RESPELL = "respell"
    OPENAI = "openai"
    GEMINI = "google"

class Model(Enum):

    MENDABLE_LLM = "mendable-llm"
    RESPELL_LLM = "respell-llm"
    GPT4 = "gpt-4o"
    GPT4_MINI = "gpt-4o-mini"
    VERTEX_AI_GEMINI = "vertex-ai-gemini"
    VERTEX_AI_PALM2 = "vertex-ai-palm-2"

# OpenAI can be used as a provider with the following models: GPT3, GPT4.
# GROQ can be used as a provider with the following models: MIXTRAL, GEMMA.
def is_valid_provider_model_combination(provider: Provider, model: Model) -> bool:
    if provider == Provider.MENDABLE:
        return model in [Model.MENDABLE_LLM]
    elif provider == Provider.RESPELL:
        return model in [Model.RESPELL_LLM]
    elif provider == Provider.OPENAI:
        return model in [Model.GPT4, Model.GPT4_MINI]
    elif provider == Provider.GOOGLE:
        return model in [Model.VERTEX_AI_GEMINI, Model.VERTEX_AI_PALM2]

def _create_mendable_chat(
    model: Model,temperature: float
) -> Callable[[Model, str, float], ChatMendable]:
    api_key = os.getenv(MENDABLE_API_KEY)
    return ChatMendable(model=model.value, mendable_api_key=api_key ,temperature=temperature)

def _create_respell_chat(
    model: Model,temperature: float
) -> Callable[[Model, str, float], ChatRespell]:
    api_key = os.getenv(RESPELL_API_KEY)
    return ChatRespell(model=model.value, respell_api_key=api_key ,temperature=temperature)

def _create_openai_chat(
    model: Model, temperature: float
) -> Callable[[Model, str, float], ChatOpenAI]:
    api_key = os.getenv(OPENAI_API_KEY)
    return ChatOpenAI(model=model.value, openai_api_key=api_key, temperature=temperature)


def _create_google_chat(
    model: Model, temperature: float
) -> Callable[[Model, str, float], ChatGoogle]:
    api_key = os.getenv(GEMINI_API_KEY)
    return ChatGoogle(
        model_name=model.value, gemini_api_key=api_key, temperature=temperature
    )


def get_chat(
    provider: Provider, model: Model
) -> Callable[[Model, str, float], Union[ChatOpenAI, ChatGoogle]]:
    if not is_valid_provider_model_combination(provider, model):
        raise ValueError("Invalid provider-model combination: {provider}-{model}")
    if provider == Provider.MENDABLE:
        return _create_mendable_chat
    elif provider == Provider.RESPELL:
        return _create_respell_chat
    elif provider == Provider.OPENAI:
        return _create_openai_chat
    elif provider == Provider.GOOGLE:
        return _create_google_chat


class Encryption:

    load_dotenv()

    def encrypt_key(
        encrypted_api_key = os.getenv(^[^=]*    _API_KEY$).encode()
        encryption_key = os.getenv(^[^=]*_API_KEY$).encode()
    )

    def decrypt_key(
    cypher_suite = Fernet(encryption_key)
    decrypted_api_key = cypher_suite.decrypt(encrypted_api_key).decode()
    )

    print(f"Decrypted Api Key: {decrypted_api_key}")


class LLMClient:
    def __init__(
        self, provider: Provider, model: Model, temperature: float = 0.35
    ) -> None:
        self.chat = get_chat(provider, model)(model, temperature)

    def rewrite(self, text: str) -> Tuple[str, int]:
        output_parser = StrOutputParser()
        chain = _REWRITE_PROMPT | self.chat
        output = chain.invoke(
            {"text": text},
            config={"callbacks": [ConsoleCallbackHandler()]},
        )
        return (
            output_parser.invoke(output),
            # The response metadata suppose to contain the token usage information.
            # However, it is not always the case. Consider token usage as 0 if
            # it is not available.
            (
                0
                if "token_usage" not in output.response_metadata
                else output.response_metadata["token_usage"]["total_tokens"]
            ),
        )