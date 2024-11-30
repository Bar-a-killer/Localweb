from flask import Flask, render_template , request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = 'messages.json'

def load_messages():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_message(name, message):
    messages = load_messages()
    messages.append({'name': name, 'message': message})
    with open(DATA_FILE, 'w') as f:
        json.dump(messages,f)


@app.route('/', methods=['GET', 'POST'])
def home():
    name = ""
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        save_message(name, message)
        return redirect(url_for('home', name=name))
    
    name = request.args.get('name', "")
    messages = load_messages()
    return render_template('index.html', messages=messages,name=name)

if __name__ == '__main__':
    app.run(debug=True)
    
