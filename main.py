from flask import Flask,request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
"""
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
            textarea {[]
                margin: 10px 0;
                width: 500px;
                height: 120px;
            }]
        </style>
    </head>
    <body>"""
form ="""
      <form  method="post">
        <label>
        Rotate by:
            <input type="text" name="rot" />   
        </label>
        <br />
        <textarea  name="text">{0}</textarea>
        <br />
        <input type="submit" value="Submit Query"/>
    </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")
@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    rot=int(rot)
    encrypted=rotate_string(text,rot)
    enc = '<h1>' + encrypted + '<h1>'
    return form.format(enc)
app.run()
.vscode/
