from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('kansas_mart.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Products.ProductID, Products.Name, Products.Price, Products.StockQuantity, Suppliers.SupplierName FROM Products JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID")
    products = cursor.fetchall()
    conn.close()
    return render_template('index.html', products=products)

# Add new product
@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    stock = request.form['stock']
    supplier_id = request.form['supplier_id']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Products (Name, Description, Price, StockQuantity, SupplierID) VALUES (?, ?, ?, ?, ?)", (name, description, price, stock, supplier_id))
    conn.commit()
    conn.close()
    return redirect('/')

# Update product stock
@app.route('/update_stock/<int:product_id>', methods=['POST'])
def update_stock(product_id):
    quantity = int(request.form['quantity'])
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Products SET StockQuantity = StockQuantity - ? WHERE ProductID = ?", (quantity, product_id))
    conn.commit()
    conn.close()
    return redirect('/')

# Delete customer with no orders
@app.route('/delete_customers')
def delete_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Customers WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders)")
    conn.commit()
    conn.close()
    return redirect('/')

# View customers without orders (Subquery)
@app.route('/view_customers_no_orders')
def view_customers_no_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customers WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders)")
    customers = cursor.fetchall()
    conn.close()
    return render_template('customers.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
