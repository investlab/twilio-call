# Twilio call
# by thaopt@nextsec.vn
# date 12/12/2023

from fastapi import FastAPI, HTTPException
from twilio.rest import Client
import json

app = FastAPI()

# Load Twilio credentials from credentials.json
with open("credentials.json") as f:
    twilio_credentials = json.load(f)

client = None  # Initialize the Twilio client outside the route handler

# Define a route to handle GET requests
@app.post("/make_call/{credential_name}")
async def make_call(credential_name: str):
    # Check if the specified credential exists
    if credential_name not in twilio_credentials:
        raise HTTPException(status_code=404, detail="Credential not found")

    # Use the selected Twilio credential
    credential = twilio_credentials[credential_name]
    global client  # Use the global client variable
    client = Client(credential["account_sid"], credential["auth_token"])

    # Make a Twilio call
    call = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to=credential["to_phone_number"],
        from_=credential["from_phone_number"]
    )

    return {"message": "Call initiated", "call_sid": call.sid}

