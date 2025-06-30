import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

    try:
        text = response.candidates[0].content.parts[0].text
    except (AttributeError, IndexError):
        text = "[ERROR] Failed to extract text from response."

    print("Generated Text:\n")
    print(text)

    usage = getattr(response, "usage_metadata", None)
    if usage:
        print("\nToken Usage:")
        print(f"  Prompt tokens: {usage.prompt_token_count}")
        print(f"  Response tokens: {usage.candidates_token_count}")
        print(f"  Total tokens: {usage.total_token_count}")
    else:
        print("\n[WARNING] Token usage metadata not available.")

if __name__ == "__main__":
    main()
