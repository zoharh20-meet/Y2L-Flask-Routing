from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases.py import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/')
def first_route():
	return render_template("home.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/store')
def store():
	products= query_all()
	return render_template("store.html", p=products)


@app.route('/cart')
def cart():
	return render_template("cart.html")


@app.route('/cart/<int:productID>')
def Add_To_Cart(productID):
    Add_To_Cart(productID)
    return render_template(
        'cart.html', id = productID)

#####################


if __name__ == '__main__':
    app.run(debug=True)