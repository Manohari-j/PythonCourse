from flask import Flask, request, redirect, url_for, render_template,jsonify

app = Flask(__name__)

cart = []

@app.route('/')
def index():
    return render_template('index.html', cart=cart)

@app.route('/api/add', methods=['POST'])
def add_to_cart():
    product = {
        'name': request.form['name'],
    }
    cart.append(product)
    return jsonify({'message': 'Product added to cart', 'cart': cart}), 201

    #return redirect(url_for('index')) # dont go to html

@app.route('/api/delete/<string:product_name>', methods=['DELETE']) # DELETE can be done with JS
def delete_from_cart(product_name):
    global cart
    cart = [product for product in cart if product['name'] != product_name]
    return jsonify({'message': 'Product deleted ', 'cart': cart}), 201

    #return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

# curl -X POST -d "name=ProductA" http://127.0.0.1:5000/api/add
# curl -X DELETE  http://127.0.0.1:5000/api/delete/ProductA