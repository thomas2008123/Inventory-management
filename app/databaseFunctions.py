import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "database.db"

# View all items in the database
def view_items():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items")
    items = cursor.fetchall()
    conn.close()
    return items


# Adds a item to the database
def add_item(name, description, instock, price, stock, rating, delivery, item_type):
    print("Add item")

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO Items
            (Name, Description, InStock, Price, StockAmount, Rating, DeliveryDate, ItemType)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (name, description, instock, price, stock, rating, delivery, item_type)
        )
    conn.commit()
    conn.close()

    print("Item added successfully.")
    conn.close()


# Updates an existing item in the database
def update_item(id, instock, stock, price):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
            UPDATE Items
                SET InStock=?, Price=?, StockAmount=?
            WHERE ItemID=?
        """,
        (instock, price, stock, id)
        )
    conn.commit()

    print("Rows affected:", cursor.rowcount)

    print("Item updated successfully.")
    conn.close()


# Deletes an item from the database
def delete_item(id):
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Items WHERE ItemID = ?", (id,))
    conn.commit()
    print("Item deleted successfully.")
    conn.close()




# Views a specific item from the database
def view_specific_item(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Items WHERE ItemID = ?", (id,))
    item = cursor.fetchone()
    
    cursor.execute("SELECT * FROM TechnicalDetails WHERE ItemID = ?", (id,))
    tech_details = cursor.fetchone()
    
    cursor.execute("SELECT * FROM Reviews WHERE ItemID = ?", (id,))
    reviews = cursor.fetchall()
    
    conn.close()

    return {
        "item": item,
        "tech_details": tech_details,
        "reviews": reviews
    }


    

