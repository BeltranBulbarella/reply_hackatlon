# util functions to interact with OpenAI API
import os
import sys
import openai
from openai import OpenAI


def find_env_file():
    """Find the .env file in the project structure."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

    possible_locations = [
        os.path.join(project_root, '.env'),
        os.path.join(project_root, 'src', '.env'),
        os.path.join(current_dir, '..', '.env'),
        os.path.join(current_dir, '.env'),
    ]

    for location in possible_locations:
        if os.path.exists(location):
            return location

    return None

def get_openai_client():
    """Get the OpenAI client with the API key."""
    # Try to load from .env file
    # Try to get the API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment or .env file.")
        print("Please set the OPENAI_API_KEY environment variable or ensure you have a .env file with the following content:")
        print("OPENAI_API_KEY='your-api-key-here'")
        sys.exit(1)

    return OpenAI(api_key=api_key)

# Initialize the OpenAI client
client = get_openai_client()


# Initialize OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

def call_openai_api(prompt, model="gpt-4", temperature=0):
    """Call the OpenAI API with the given prompt."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert assistant for academic courses."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=temperature,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
