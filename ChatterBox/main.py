from flask import Flask, render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
Bot = ChatBot('ChatterBox')
trainer = ListTrainer(ChatBot)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(Bot.get_response(userText))

if __name__ == "__main__":
    app.run()

