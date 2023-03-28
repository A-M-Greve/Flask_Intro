from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    
    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

STATUS = {
    "home": "welcome home",
    "back": "welcome back",
}

@app.route('/welcome/<stat>')
def show_status(stat):

    wel = STATUS[stat]
    return f"<h1> Welcome {wel} </h1>"