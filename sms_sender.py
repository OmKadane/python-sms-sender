from twilio.rest import Client

# Taking credentials input from user
account_sid = input("Enter your Twilio Account SID: ")
auth_token = input("Enter your Twilio Auth Token: ")
twilio_number = input("Enter your Twilio Phone Number: ")
receiver_number = input("Enter recipient's phone number (with country code): ")

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Sending SMS
try:
    message = client.messages.create(
        body="Hello! This is a test SMS sent using Twilio API.",
        from_=twilio_number,
        to=receiver_number
    )
    print("SMS sent successfully! Message SID:", message.sid)
except Exception as e:
    print("Error:", e)