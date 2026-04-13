# reminder_bot.py

from twilio.rest import Client
from dotenv import load_dotenv
import os
import time


# --- Load environment variables from .env ---
load_dotenv()

# --- Get Twilio credentials from environment ---
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = os.getenv("TWILIO_WHATSAPP_FROM")

if not all([ACCOUNT_SID, AUTH_TOKEN, FROM_WHATSAPP]):
    raise RuntimeError("Missing Twilio credentials in .env file!")

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)


# --- WhatsApp reminder function ---
def send_whatsapp_reminder(to_number, content_sid, vars_dict):
    """
    Send a WhatsApp reminder using Twilio's Content API.
    """
    try:
        # Convert dict to JSON‑style string
        vars_str = str(vars_dict).replace("'", '"')

        message = client.messages.create(
            from_=FROM_WHATSAPP,
            content_sid=content_sid,
            content_variables=vars_str,
            to=to_number
        )
        print(f"[+] Reminder sent: {message.sid}")
        return True
    except Exception as e:
        print(f"[!] Error: {e}")
        return False


# --- Example usage ---
if __name__ == "__main__":
    print("WhatsApp Reminder Bot (with .env)")
    print("----------------------------")

    # --- CONFIGURE ---
    TO_WHATSAPP = "whatsapp:+264858011111"              # your WhatsApp
    CONTENT_SID = "HXb5b62575e6e4ff6129ad7c8efe1f983e"    # your template SID

    # Update variables as needed (e.g., date and time)
    VARS = {"1": "12/1", "2": "3pm"}

    # --- SEND FIRST REMINDER ---
    print("Sending first reminder...")
    send_whatsapp_reminder(TO_WHATSAPP, CONTENT_SID, VARS)

    # --- Optional: send again after X seconds ---
    print("Sending next reminder in 10 seconds...")
    time.sleep(10)
    send_whatsapp_reminder(TO_WHATSAPP, CONTENT_SID, VARS)