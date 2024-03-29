from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/thankyou')
def thankyou():
    name = request.args.get('username')
    email = request.args.get('email')
    address = request.args.get('address')
    phone = request.args.get('phone')
    props = {
        "name": name,
        "email": email,
        "address": address,
        "phone": phone
    }
    return render_template("thankyou.html", data=props)

if __name__ == '__main__':
    app.run(debug=True)