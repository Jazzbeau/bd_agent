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


def make_parser():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    return parser


def get_response(messages):
    response = CLIENT.models.generate_content(model=MODEL, contents=messages)
    if response.usage_metadata is None:
        raise RuntimeError("API query failure")

    return (
        response.text,
        response.usage_metadata.prompt_token_count,
        response.usage_metadata.candidates_token_count,
    )


def print_verbose_response(
    query, response_text, prompt_token_count, candidate_token_count
):
    print(
        f"User prompt:{query}\nPrompt tokens: {prompt_token_count}\nResponse tokens: {candidate_token_count}\nResponse:\n{response_text}"
    )


def main():
    parser = make_parser()
    args = parser.parse_args()
    # A list of messages, which take the form of a `types.Content` instance, containing a role, and in our case, a series of
    # text parts
    query = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=query)])]
    print_verbose_response(query, *get_response(messages))


if __name__ == "__main__":
    main()
