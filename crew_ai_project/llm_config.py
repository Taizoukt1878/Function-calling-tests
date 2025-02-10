import os
from dotenv import load_dotenv
from logger import setup_logger
from crewai import LLM

logger = setup_logger()
# Load environment variables from .env
load_dotenv()


# load_dotenv(dotenv_path=".env")
llm = LLM(model="nvidia_nim/meta/llama-3.1-70b-instruct", base_url="https://integrate.api.nvidia.com/v1", temperature=0)

logger.info("OpenAI client initialized successfully.")
