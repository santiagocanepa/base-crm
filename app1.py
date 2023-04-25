import subprocess
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Configurar cliente de Twilio
account_sid = 'AC30e0c303d2242d17de8c6d875be00712'
auth_token = '7a343bfc02705fb368b03bba873acf2c'
client = Client(account_sid, auth_token)

app1 = Flask(__name__)

# Definir endpoint para que Twilio envíe mensajes
@app1.route('/bot', methods=['POST'])
def bot():
    
    user_msg = request.values.get('Body', '').lower()

    # Aquí puedes reemplazar esta sección con tu propio código para procesar y generar respuestas a las preguntas

    # Enviar respuesta utilizando Twilio
    message = client.messages.create(
        from_='whatsapp:+5491125167377',
        to='whatsapp:+14155238886'
    )

    # Devolver respuesta al usuario
    return formatted_response

if __name__ == '__main__':
    app1.run()
