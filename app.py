from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)



@app.route('/')
def index():
    return render_template ('public/templates/index.html')


@app.route('/list')
def list():
    return render_template ('public/templates/list.html')


@app.route('/Naivas')
def Naivas():
    return render_template ('public/templates/Naivas.html')


@app.route('/Quickmart')
def Quickmart():
    return render_template ('public/templates/Quickmart.html')


@app.route('/Budget')
def Budget():
    return render_template ('public/templates/Budget.html')











if __name__ == '__main__':
    app.run(debug=True)
