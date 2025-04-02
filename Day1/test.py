import numpy as np
import openai
from dotenv import load_dotenv
load_dotenv
import os
openai.api_key = os.environ.get("OPENAI_API_KEY")

print("Hello world")