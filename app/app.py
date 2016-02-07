# Import libraries
from flask import Flask, render_template, request, redirect, url_for
import numpy as np

# Make an instance as app
app = Flask(__name__)

# Get messages at rondom using NumPy
def picked_up():
    messages = [
        "What is your favourite song?",
        "Please tell me what your favourite song is.",
        "Could you share your fabvourite song?"
    ]
    return np.random.choice(messages)

# Make a routing process
# Render messages to index.html
@app.route('/')
def index():
    title = "Question"
    message = picked_up()
    return render_template('index.html', message=message, title=title)

# Display the answer on "/post"
@app.route('/post', methods=['POST', 'GET'])
def post():
    title = "Answer"
    if request.method == 'POST':
        answer = request.form['answer']
        return render_template('index.html', answer=answer, title=title)
    else:
        return redirect(url_for('index'))

# Set the debug mode and the access authorisation
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')