import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
CLIENT = genai.Client(api_key=API_KEY)
MODEL = "gemini-2.5-flash"

if API_KEY is None:
    raise RuntimeError("'GEMINI_API_KEY' environment variable not found'")


def main():
    response = CLIENT.models.generate_content(
        model=MODEL, contents="Does anyone expect the Spanish Inquisition?"
    )
    print(response.text)


if __name__ == "__main__":
    main()
