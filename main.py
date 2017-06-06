from flask import Flask

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
    <form action="/change" method="POST">
        <label for="rot">
            Rotate by:
            <input type="text" name="rot" placeholder="0"/>
        </label>
        <br></br>
        <input type="textarea" name="text"/>
        <br></br>
        <input type="submit" value="Submit Query"/>
    </form>
"""


page_footer = """
        <!-- create your form here -->
    </body>
</html>
"""

@app.route("/")
def index():
    return page_header + input_form + page_footer

app.run()
