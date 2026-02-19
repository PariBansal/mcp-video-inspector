# src/llm_summary.py

import openai
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(features: dict) -> str:
    """
    Uses OpenAI's GPT to summarize the editing style, mood, and tone
    based on extracted video features.

    Args:
        features (dict): Extracted video features.

    Returns:
        str: AI-generated summary or error message.
    """
    if not features:
        return "⚠️ No features provided to summarize."

    # Prepare prompt
    prompt = (
        "You're a video editing assistant. Based on the following features "
        "extracted from a YouTube video, describe the editing style, mood, and tone:\n\n"
        f"{features}\n\n"
        "Provide a creative, clear summary that helps a video editor understand the essence of the video."
    )

    try:
        # ChatCompletion API call
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a video editing assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        summary = response['choices'][0]['message']['content'].strip()
        return summary

    except Exception as e:
        return f"❌ Error generating summary: {str(e)}"
