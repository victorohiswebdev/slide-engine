import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def list_gemini_models():
    print("Available Gemini API Models:")
    # Iterate through all available models
    for model in genai.list_models():
        print(f"* Name: {model.name}")
        print(f"  Display Name: {model.display_name}")
        print(f"  Description: {model.description}")
        print(f"  Supported Generation Methods: {model.supported_generation_methods}")
        print("-" * 20)

if __name__ == "__main__":
    list_gemini_models()
