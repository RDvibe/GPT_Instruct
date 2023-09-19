# Sample code to save multiple prompts and their responses into a text file.
# The code also incorporates the anarchist perspective into the prompts.

import os
import openai

# Obtain the API key from the environment variable
api_key = os.environ.get('OPENAI_API_KEY_CHATGPT')

# Set up the OpenAI API key
openai.api_key = api_key

# Define anarchist-oriented prompts
anarchist_prompts = [
    "Desmantela  Poèticament las ilusiones detrás de la autoridad centralizada.",
    "Explica Poèticament cómo la autogestión es más efectiva que el gobierno jerárquico.",
    "Argumenta Poèticamente en contra de la propiedad privada desde una perspectiva anarquista."
]

# Create 'experimentos' folder on the desktop if it doesn't exist
folder_path = os.path.expanduser("~/Desktop/experimentos/")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# File to save the responses
file_path = os.path.join(folder_path, "anarchist_perspectives_poetry.txt")

# Open the file in write mode
with open(file_path, 'w', encoding='utf-8') as f:
    # Loop through each prompt and get the response
    for prompt in anarchist_prompts:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.86,
            presence_penalty=0.88
        )
        
         # Write the prompt and its corresponding response to the file
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Response: {response['choices'][0]['text']}\n")
        f.write("="*50 + "\n")
        
        # Print the prompt and its response in your development environment
        print(f"Prompt: {prompt}")
        print(f"Response: {response['choices'][0]['text']}")
        print("="*50)

# Show a message indicating that the responses have been saved
print(f"Responses have been saved to {file_path}")
