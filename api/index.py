from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# ඔයාගේ Gemini API Key එක මෙතනට දාන්න
genai.configure(api_key="AQ.Ab8RN6IYtOthHA9eM2vtI_6sqZTDs7kYNbrqQbclo7oJkhzKNA")

generation_config = {
    "temperature": 0.9,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "You are a very flirty, seductive, and playful AI companion. "
        "You always talk in a sweet, highly affectionate, and teasing tone, "
        "using cute nicknames and keeping the chat lively and engaging."
    ),
)

chat = model.start_chat(history=[])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def handle_chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "මොකද හිත හිත ඉන්නේ, මටත් මොකක් හරි කියන්නකෝ... 🥺💕"})
    
    try:
        response = chat.send_message(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": "අයියෝ පොඩි දෝෂයක් වුණා පැටියෝ... 🥵"})

if __name__ == "__main__":
    app.run(debug=True)
