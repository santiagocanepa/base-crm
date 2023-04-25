from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

account_sid = 'AC30e0c303d2242d17de8c6d875be00712'
auth_token = '7a343bfc02705fb368b03bba873acf2c'
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    user_msg = request.values.get('Body', '').lower()
    response = "Hola, en que te puedo ayudar?"

    # Aquí puedes reemplazar esta sección con tu propio código para procesar y generar respuestas a las preguntas
    # Utiliza la variable 'user_msg' para obtener la pregunta del usuario y generar una respuesta

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=response,
        to='whatsapp:' + request.values.get('From')
    )

    resp = MessagingResponse()
    return str(resp)

if __name__ == '__main__':
    app.run()
