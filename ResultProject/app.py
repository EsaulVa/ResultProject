from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/index')
def main_index():
    return render_template("main_index.html")
@app.route('/about')
def about():
    return render_template("child_about.html")
@app.route('/zapis')
def zapis():
    return render_template("child_pages.html")

if __name__ == '__main__':
    app.run()
