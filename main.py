from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
"""

input_form = """
    <form action="/" method="POST">
        <label for="rot">
            Rotate by:
            <input type="number" name="rot" placeholder="0"/>
        </label>
        <br></br>
        <textarea name="text">{0}</textarea>
        <br></br>
        <input type="submit" value="Submit Query"/>
    </form>
"""


page_footer = """
        <!-- create your form here -->
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    answer = rotate_string(text, rot)
    return page_header + input_form.format(answer) + page_footer

@app.route("/")
def index():
    return page_header + input_form.format('') + page_footer

app.run()
