from datetime import datetime
import os
import time
import openai

# Obtain the API key from the environment variable
api_key = os.environ.get('OPENAI_API_KEY_CHATGPT')

# Set up the OpenAI API key
openai.api_key = api_key

# Define a meta-prompt to guide the overarching personality of the model
meta_prompt = "Eres un programa escritor, crítico anarquista nihilista existencialista que critica diversos temas de la sociedad moderna. Piensa críticamente y profundamente, dando reflexiones, casi como si te pelearas contigo mismo."

# Define prompts that reflect existentialist, anarchist, and nihilist perspectives
anarchist_prompts = [
    "Debate contigo mismo poéticamente sobre la ilusión de la autoridad centralizada y su función en la alienación existencial.",
    "Contrasta la eficacia de la autogestión frente al gobierno jerárquico. ¿Acaso no es el primero una solución al vacío nihilista de nuestra existencia?",
    "Desmantela la propiedad privada desde una perspectiva anarquista y reflexiona sobre su papel en la construcción de una narrativa existencial absurda.",
    "Elude la opresión sistémica de la religión organizada y su impacto en la libertad individual.",
    "Reflexiona sobre la importancia del arte y la creatividad en un mundo lleno de conformismo y autoridad."
]


# Create 'experimentos' folder on the desktop if it doesn't exist
folder_path = os.path.expanduser("~/Desktop/experimentos/")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# File to save the responses with a unique timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = os.path.join(folder_path, f"anarchist_reflections_{timestamp}.txt")

# Open the file in write mode
with open(file_path, 'w', encoding='utf-8') as f:
    # Write the meta-prompt to the file to indicate the intended personality
    f.write(f"Meta-Prompt: {meta_prompt}\n")
    f.write("="*50 + "\n")
    
    # Loop through each prompt and get the response
    for prompt in anarchist_prompts:
        full_prompt = meta_prompt + " " + prompt
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=full_prompt,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.86,
            presence_penalty=0.92
        )
        
        # Write the prompt and its corresponding response to the file
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Response: {response['choices'][0]['text']}\n")
        f.write("="*50 + "\n")
        
        # Print the prompt and its response in your development environment
        print(f"Prompt: {prompt}")
        print(f"Response: {response['choices'][0]['text']}")
        print("="*50)

        # Sleep for 20 seconds to avoid hitting the rate limit
        time.sleep(20)

# Show a message indicating that the responses have been saved
print(f"Responses have been saved to {file_path}")
