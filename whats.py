from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/led", methods=['POST'])
def sms_reply():
    
    msg = request.form.get('Body')

    resp = MessagingResponse()
    if(msg == "Acender"):
    	resp.message("Led ON")
    	os.system("python on.py")

    if(msg == "Apagar"):
    	resp.message("Led Off")
    	os.system("python off.py")

    if(msg != "Acender" and msg != "Apagar"):
    	resp.message("Digite Acender para LED ON\nE Apagar para LED OFF")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
