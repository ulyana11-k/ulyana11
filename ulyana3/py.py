from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "<h1>Страница про игру <h1\>"

@app.route('/inform')
def inform():
    return "<h1>Информация про нас т<h1\>"

if __name__ =="__main__":
    app.run()