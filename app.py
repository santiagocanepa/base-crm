import subprocess
import time
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import openai

# Configurar cliente de Twilio
account_sid = 'AC30e0c303d2242d17de8c6d875be00712'
auth_token = '7a343bfc02705fb368b03bba873acf2c'
client = Client(account_sid, auth_token)
status_callback = 'https://a14c-181-4-118-241.sa.ngrok.io/bot'

openai.api_key = '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'

# Definir función para generar respuesta utilizando OpenAI
def generate_response(query):
    prompt = f"Answer the following question: {query}\n\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

# Definir función para formatear la respuesta generada por OpenAI
def format_response(response):
    response = response.replace('\n', ' ') # reemplazar saltos de línea por espacios
    response = response.replace('"', '') # eliminar comillas dobles
    response = response.replace("'", '') # eliminar comillas simples
    response = response.strip() # eliminar espacios en blanco al principio y al final
    return response

app = Flask(__name__)

# Definir endpoint para que Twilio envíe mensajes
@app.route('/bot', methods=['POST'])
def bot():
    # Obtener mensaje del usuario
    user_msg = request.values.get('Body', '').lower()

    # Generar respuesta utilizando OpenAI
    response = generate_response(user_msg)

    # Formatear respuesta generada por OpenAI
    formatted_response = format_response(response)

    # Enviar respuesta utilizando Twilio
    message = client.messages.create(
        from_='whatsapp:+5491125167377',
        body=formatted_response,
        to='whatsapp:+14155238886',
        status_callback=status_callback

    )

    # Devolver respuesta al usuario
    return formatted_response

if __name__ == '__main__':
    port = 5000
    app.run(port=port)

    
