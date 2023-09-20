import os
import time
import datetime
import openai

# Obtain the API key from the environment variable
api_key = os.environ.get('OPENAI_API_KEY_CHATGPT')

# Set up the OpenAI API key
openai.api_key = api_key

# Define meta-prompts inspired by philosophical and artistic figures
meta_prompts = {
    'Sartre': "Eres un programa escritor existencialista inspirado por Jean-Paul Sartre. Explores temas de libertad, la nada y la alienación.",
    'Nietzsche': "Eres un programa escritor nihilista inspirado por Friedrich Nietzsche. Examinas el eterno retorno y la voluntad de poder.",
    'Jung': "Eres un programa escritor inspirado por Carl Jung. Exploras la psique humana, sus arquetipos y el inconsciente colectivo.",
    'Lovecraft': "Eres un programa escritor de horror cósmico, inspirado por H.P. Lovecraft. Consideras la insignificancia humana en el vasto cosmos."
}

# Define prompts that reflect themes inspired by these figures
themed_prompts = {
    'Sartre': [
        "Reflexiona sobre la paradoja de la libertad y cómo conduce a la alienación.",
        "Explora el concepto de 'mala fe' en el contexto de la autoridad y el conformismo."
    ],
    'Nietzsche': [
        "Debate sobre la moralidad en un mundo sin un orden divino.",
        "Describe lo que significa abrazar el caos y la incertidumbre a través de la voluntad de poder."
    ],
    'Jung': [
        "Discute el papel de los arquetipos en la construcción de la realidad individual y colectiva.",
        "Explora la noción del 'Sí-mismo' como un fractal en la psique humana."
    ],
    'Lovecraft': [
        "Describe la angustia existencial que surge al enfrentar la inmensidad cósmica.",
        "Explora el horror de la incognoscibilidad en el contexto de la existencia humana."
    ]
}

# Create folder to save responses, if it doesn't exist
folder_path = os.path.expanduser("~/Desktop/experimentos/")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# File to save responses with a unique timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = os.path.join(folder_path, f"multi_personality_reflections_{timestamp}.txt")

# Open the file in write mode
with open(file_path, 'w', encoding='utf-8') as f:
    # Loop through each philosophical personality and its corresponding prompts
    for personality, prompts in themed_prompts.items():
        meta_prompt = meta_prompts[personality]
        f.write(f"Meta-Prompt ({personality}): {meta_prompt}\n")
        f.write("="*50 + "\n")
        
        for prompt in prompts:
            full_prompt = meta_prompt + " " + prompt
            response = openai.Completion.create(
                model="gpt-3.5-turbo",
                prompt=full_prompt,
                temperature=0.7,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0.6
            )
            
            f.write(f"Prompt: {prompt}\n")
            f.write(f"Response: {response['choices'][0]['text']}\n")
            f.write("="*50 + "\n")
            
            print(f"Prompt: {prompt}")
            print(f"Response: {response['choices'][0]['text']}")
            print("="*50)
            
            # Sleep for 20 seconds to avoid hitting the rate limit
            time.sleep(20)