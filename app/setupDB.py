import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database', 'database.db')

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def setup_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Items (
                ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Description TEXT,
                InStock INTEGER NOT NULL,
                Price REAL NOT NULL,
                StockAmount INTEGER,
                Rating REAL,
                DeliveryDate TEXT,
                ItemType TEXT
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Reviews (
                ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
                ItemID INTEGER NOT NULL,
                Name TEXT,
                Rating INTEGER CHECK(Rating BETWEEN 1 AND 5),
                Comment TEXT,
                FOREIGN KEY (ItemID) REFERENCES Items(ItemID) ON DELETE CASCADE
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS TechnicalDetails (
                TechDetailsID INTEGER PRIMARY KEY AUTOINCREMENT,
                ItemID INTEGER NOT NULL UNIQUE,
                Weight REAL,
                Dimensions TEXT,
                Supplier TEXT,
                Manufacturer TEXT,
                FOREIGN KEY (ItemID) REFERENCES Items(ItemID) ON DELETE CASCADE
            );
        """)
        
        conn.commit()

def seed_db():
    seed_path = os.path.join(BASE_DIR, 'database', 'seed.sql')

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("SELECT COUNT(*) FROM Items;")
        if cursor.fetchone()[0] > 0:
            print("Database already seeded. Skipping seed.")
            return

        with open(seed_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()

        cursor.executescript(sql_script)
        conn.commit()


