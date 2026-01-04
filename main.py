import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
CLIENT = genai.Client(api_key=API_KEY)
MODEL = "gemini-2.5-flash"

if API_KEY is None:
    raise RuntimeError("'GEMINI_API_KEY' environment variable not found'")


def getResponse(query):
    response = CLIENT.models.generate_content(model=MODEL, contents=query)
    if response.usage_metadata is None:
        raise RuntimeError("API query failure")

    return (
        response.text,
        response.usage_metadata.prompt_token_count,
        response.usage_metadata.candidates_token_count,
    )


def printVerboseResponse(
    query, response_text, prompt_token_count, candidate_token_count
):
    print(
        f"User prompt:{query}\nPrompt tokens: {prompt_token_count}\nResponse tokens: {candidate_token_count}\nResponse:\n{response_text}"
    )


def main():
    query = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    printVerboseResponse(query, *getResponse(query))


if __name__ == "__main__":
    main()
