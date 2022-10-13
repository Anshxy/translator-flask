from flask import Flask, render_template, request # include the flask library 
from main import translation

app = Flask(__name__) 

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       tr = request.form.get("translate-src")

       print(tr)
       return render_template("index.html", translation=translation(tr)[0])
    return render_template("index.html")



if __name__ == '__main__': 
   app.run(port=5000, debug=True) # application will start listening for web request on port 5000