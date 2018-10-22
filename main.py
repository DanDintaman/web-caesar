from flask import Flask, request
import caesar

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
<html>
   <head>
       <style>
           form {{
               background-color: #eee;
               padding: 20px;
               margin: 0 auto;
               width: 540px;
               font: 16px sans-serif;
               border-radius: 10px;
               }}
           textarea {{
               margin: 10px 0;
               width: 540px;
               height: 120px;
               }}
         
       </style>
   </head>
   <body>
       <form id="app" method="post">
       <h1>Web-Caesar</h1>
           <label>
               Rotate By: <input type="number" value={rot} id="rot-input" name="rot"/>
               <textarea id="text-input" name="text-input">{text}</textarea>
               <input type="submit" value="Encrypt"/>
           </label>
       </form>
   </body>
</html>
"""

@app.route("/")
def index():
   return form.format(text='', rot=0)


@app.route("/", methods=['POST'])
def encrypt():
   user_string = request.form['text-input']
   rotation = request.form['rot']
   content = caesar.encrypt(user_string, int(rotation))

   return form.format(text=content, rot=rotation)

app.run()