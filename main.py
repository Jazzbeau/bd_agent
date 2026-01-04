import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("'GEMINI_API_KEY' environment variable not found'")


def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
