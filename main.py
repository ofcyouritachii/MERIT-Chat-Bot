from flask import Flask, render_template, request, redirect, url_for
from langchain_ollama.llms import OllamaLLM

app = Flask(__name__)

model = OllamaLLM(model="tinyllama", base_url="http://localhost:11434")

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    if user_message:
        messages.append({'user': 'You', 'text': user_message})
        prompt = f"You are a helpful tutor. Explain {user_message} in English."
        response = model.invoke(prompt)
        messages.append({'user': 'Bot', 'text': response})
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear():
    messages.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
