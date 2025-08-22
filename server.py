from flask import Flask, request, jsonify
from flask_cors import CORS
import requests  # <-- needed to send to Discord

app = Flask(__name__)
CORS(app)  # Allow frontend to call backend

# Replace with your Discord Webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1408483674650972231/cWs0t0oBSndxTCkvSFCF6f3Bd7YwgbvzSL3F8sOpC9JhTBcvV5j4QbyPBqnQvckF3CC6"


@app.route("/submit", methods=["POST", "GET"])
def submit():
    name = request.form.get("name")
    mobile = request.form.get("mobile")
    location = request.form.get("location")
    calltime = request.form.get("calltime")

    # Format the message for Discord
    content = (
        f"📌 **New Form Submission**\n"
        f"👤 Name: {name}\n"
        f"📞 Mobile: {mobile}\n"
        f"📍 Location: {location}\n"
        f"⏰ Call Time: {calltime}"
    )

    # Send to Discord
    response = requests.post(DISCORD_WEBHOOK_URL, json={"content": content})

    if response.status_code == 204:
        return jsonify({"message": "Form submitted successfully"})
    else:
        return jsonify({"message": "Form submitted, but failed to send to company!"}), 500

if __name__ == "__main__":
    app.run()
