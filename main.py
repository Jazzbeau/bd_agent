import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
CLIENT = genai.Client(api_key=API_KEY)
MODEL = "gemini-2.5-flash"
if API_KEY is None:
    raise RuntimeError("'GEMINI_API_KEY' environment variable not found'")


def get_parser():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser


def get_response(messages):
    # generate_content accepts the list of Content instances; sends GenerateContentResponse back.
    response = CLIENT.models.generate_content(model=MODEL, contents=messages)
    if response.usage_metadata is None:
        raise RuntimeError("API query failure")
    return response


def print_response(query, response, verbose):
    response_text = response.text
    if verbose:
        prompt_token_count = response.usage_metadata.prompt_token_count
        candidates_token_count = response.usage_metadata.candidates_token_count
        print(
            f"User prompt:{query}\nPrompt tokens: {prompt_token_count}\nResponse tokens: {candidates_token_count}\nResponse:\n{response_text}"
        )
    else:
        print(response_text)


def main():
    # Setup
    parser = get_parser()
    args = parser.parse_args()
    query = args.user_prompt

    # List of `genai.types.Content` instance, each contains role + list of parts (text)
    messages = [types.Content(role="user", parts=[types.Part(text=query)])]

    # Error and other logic wrapper over generate_content
    response = get_response(messages)

    print_response(query, response, args.verbose)


if __name__ == "__main__":
    main()
