from flask import Flask, redirect, url_for, request, redirect, session, render_template
from flask_bootstrap import Bootstrap


app_ini = Flask(__name__)
Bootstrap(app_ini)

@app_ini.route('/')
def index():
    return render_template("index.html")


@app_ini.route('/About')
def About():
    return render_template("About.html")

@app_ini.route('/Address')
def Address():
    return render_template("Address.html")

@app_ini.route('/services')
def services():
    return render_template("services.html")

@app_ini.route('/Robes')
def Robes():
    return render_template("Robes.html")

@app_ini.route('/Shampoo')
def Shampoo():
    return render_template("Shampoo.html")

@app_ini.route('/Bathgel')
def Bathgel():
    return render_template("Bathgel.html")

@app_ini.route('/bedspread')
def bedspread():
    return render_template("bedspread.html")

@app_ini.route('/Bodylotion')
def Bodylotion():
    return render_template("Bodylotion.html")


@app_ini.route('/Brownsugar')
def Brownsugar():
    return render_template("Brownsugar.html")


@app_ini.route('/Coaster')
def Coaster():
    return render_template("Coaster.html")


@app_ini.route('/Coffee')
def Coffee():
    return render_template("Coffee.html")

@app_ini.route('/Duvet')
def Duvet():
    return render_template("Duvet.html")


@app_ini.route('/Toothpick')
def Toothpick():
    return render_template("Toothpick.html")


@app_ini.route('/Towels')
def Towels():
    return render_template("Towels.html")


@app_ini.route('/Whitesugar')
def Whitesugar():
    return render_template("Whitesugar.html")


if __name__ == '__main__':
    app_ini.run(debug = True)