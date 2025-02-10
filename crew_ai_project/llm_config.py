# import os
from dotenv import load_dotenv
from logger import setup_logger
from crewai import LLM
import streamlit as st

logger = setup_logger()
# Load environment variables from .env
load_dotenv()


# Load API key from .env file
# os.environ["OPENAI_API_KEY"] = str(st.secrets["OPENAI_KEY"])
# load_dotenv(dotenv_path=".env")
llm = LLM(model="nvidia_nim/meta/llama-3.1-70b-instruct", base_url="https://integrate.api.nvidia.com/v1", temperature=0, api_key= st.secrets["OPENAI_KEY"])

logger.info("OpenAI client initialized successfully.")
