import sqlite3
from pathlib import Path
from setupDB import setup_db, seed_db
from databaseFunctions import view_items, add_item, update_item, delete_item, view_specific_item
from flask import Flask, request, render_template

app = Flask(__name__, static_folder='../static')

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('name.html')
    

@app.route('/view_all', methods=['GET', 'POST'])
def view_all():
    items = None
    if request.method == 'GET':
        items = view_items()
        if not items:
            return render_template('specific.html', error="No items found in the database.")
    return render_template('view_all.html', items=items)


@app.route('/view_specific', methods=['GET', 'POST'])
def view_specific():
    message = None
    if request.method == 'POST':
        id_val = request.form.get('idInput')
        message = view_specific_item(id_val)
        
        if not message:
            return render_template('view_specific.html', error="No data found for the specified ItemID.")
    
    return render_template('view_specific.html', message=message)


@app.route('/add_item', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        instock = int(request.form.get('instock', '0'))
        price = float(request.form.get('price', '0.0'))
        stock = int(request.form.get('stock', '0'))
        rating = float(request.form.get('rating', '0.0'))
        delivery = request.form.get('delivery')
        item_type = request.form.get('item_type')

        add_item(name, description, instock, price, stock, rating, delivery, item_type)
        return render_template('add.html', success=True)
    return render_template('add.html', success=False)


@app.route('/update_item', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        id = request.form.get('idInput')
        stock = int(request.form.get('newStock', '0'))
        instock = int(request.form.get('in_stock', '0'))
        price = float(request.form.get('price', '0.0'))

        update_item(id, instock, stock, price)
        return render_template('update.html', success=True)
    return render_template('update.html', success=False)


@app.route('/delete_item', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        id = request.form.get('IdInput')
        delete_item(id)
        return render_template('delete.html', success=True)
    return render_template('delete.html', success=False)


def start_database():
    file_path = Path("database/database.db")

    if not file_path.exists():
        print("Database file does not exist. Setting up the database...")
        setup_db()
        seed_db()
        print(f"Database ready at: {file_path}")
    else:
        print(f"Database already exists at: {file_path}")



if __name__ == "__main__":
    start_database()
    app.run(debug=True)