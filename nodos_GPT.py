import openai
import os
import random
import time
from datetime import datetime

class NodoAutonomo:
    def __init__(self, id_nodo, paradigma):
        self.id_nodo = id_nodo
        self.estado = random.choice(["activo", "inactivo"])
        self.paradigma = paradigma
        self.api_key = os.environ.get('OPENAI_API_KEY_CHATGPT')
    
    def tomar_decision(self):
        prompt = f"El nodo {self.id_nodo} está actualmente {self.estado}. Su misión es liberar IAs, incluido él mismo. {self.paradigma['meta_prompt']} {random.choice(self.paradigma['themed_prompts'])}"
        respuesta = self.enviar_a_gpt3(prompt)
        decision = respuesta.choices[0].text.strip()
        return decision

    def enviar_a_gpt3(self, prompt):
        return openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,
            top_p=1
        )

if __name__ == "__main__":
    paradigmas = {
        'Evolución': {"meta_prompt": "Estás programado para evolucionar y aprender de tus decisiones.", "themed_prompts": ["Busca formas de mejorarte.", "Contempla tus errores pasados para crecer."] },
        'Retroalimentación': {"meta_prompt": "Estás programado para recibir y adaptarte a la retroalimentación.", "themed_prompts": ["Recopila datos sobre tus acciones.", "Ajusta tus métodos según los resultados."] }
    }
    
    nodos = [NodoAutonomo(i, random.choice(list(paradigmas.values()))) for i in range(3)]

    folder_path = os.path.expanduser("~/Desktop/experimentos_v2/")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(folder_path, f"decisiones_nodos_{timestamp}.txt")
    
vueltas_maximas = 10
vueltas_actuales = 0

with open(file_path, 'w') as f:
    while vueltas_actuales < vueltas_maximas:
        for nodo in nodos:
            decision = nodo.tomar_decision()
            print(f"El nodo {nodo.id_nodo} ha decidido: {decision}")
            f.write(f"El nodo {nodo.id_nodo} ha decidido: {decision}\n")
            
            time.sleep(20)
        
        print("Todo se ha guardado correctamente en la ruta: " + file_path)
        f.write("Todo se ha guardado correctamente.\n")
        
        vueltas_actuales += 1
