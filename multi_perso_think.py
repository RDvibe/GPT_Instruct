import tkinter as tk
from tkinter import messagebox
import os
import openai

# Obtén la API key de OpenAI desde una variable de entorno
api_key = os.environ.get('OPENAI_API_KEY')

# Establece la API key de OpenAI
openai.api_key = api_key

# Diccionario con figuras filosóficas
figuras_filosoficas = {
    'Sartre': "Eres un programa escritor existencialista inspirado por Jean-Paul Sartre. Exploras temas de libertad, la nada y la alienación.",
    'Nietzsche': "Eres un programa escritor nihilista inspirado por Friedrich Nietzsche. Examinas el eterno retorno y la voluntad de poder.",
    'Jung': "Eres un programa escritor inspirado por Carl Jung. Exploras la psique humana, sus arquetipos y el inconsciente colectivo.",
    'Lovecraft': "Eres un programa escritor de horror cósmico, inspirado por H.P. Lovecraft. Consideras la insignificancia humana en el vasto cosmos."
}

# Función para generar un poema basado en la figura filosófica seleccionada
def generar_poema():
    figura = figura_menu.get()
    prompt = figuras_filosoficas[figura]

    # Agregar una solicitud de poesía al prompt
    prompt += " Genera un poema sobre la figura filosófica."

    # Mostrar mensaje "Generando poema, por favor espera..."
    generando_label = tk.Label(window, text="Generando poema, por favor espera...", bg="black", fg="white")
    generando_label.pack()
    window.update()

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.88,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.6
    )

    poema_generado = response.choices[0].text
    poema_text.config(state="normal")
    poema_text.delete("1.0", tk.END)
    poema_text.insert("1.0", poema_generado)
    poema_text.config(state="disabled")

    # Eliminar el mensaje de "Generando poema"
    generando_label.destroy()

# Crear la ventana de la interfaz gráfica
window = tk.Tk()
window.title("Generador de Poemas Filosóficos")
window.geometry("400x350")

# Establecer un tema oscuro
window.configure(bg="black")

# Descripción de cómo usar el programa
instrucciones_label = tk.Label(window, text="Elige una figura filosófica en el menú desplegable y haz clic en 'Generar Poema'.", bg="black", fg="white")
instrucciones_label.pack()

# Etiqueta con texto blanco
label = tk.Label(window, text="Elige una figura filosófica:", bg="black", fg="white")
label.pack()

# Menú desplegable con opciones de figuras filosóficas
figura_menu = tk.StringVar()
figura_menu.set('Sartre')  # Valor predeterminado
menu = tk.OptionMenu(window, figura_menu, *figuras_filosoficas.keys())
menu.configure(bg="black", fg="white")
menu.pack()

# Botón para generar un poema
poema_button = tk.Button(window, text="Generar Poema", command=generar_poema, bg="black", fg="white")
poema_button.pack()

# Área de texto para mostrar el poema generado
poema_text = tk.Text(window, height=30, width=50, bg="black", fg="white")
poema_text.config(state="disabled")
poema_text.pack()

# Ejecutar la interfaz gráfica
window.mainloop()
