import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age TEXT,
                doj TEXT,
                email TEXT,
                gender TEXT,
                contact TEXT,
                address TEXT
            )
        """)
        self.conn.commit()

    def insert(self, name, age, doj, email, gender, contact, address):
        try:
            self.cur.execute(
                "INSERT INTO employees VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                (name, age, doj, email, gender, contact, address)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Insert error: {e}")
            return False

    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        try:
            self.cur.execute("DELETE FROM employees WHERE id = ?", (id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Delete error: {e}")
            return False

    def update(self, id, name, age, doj, email, gender, contact, address):
        try:
            self.cur.execute("""
                UPDATE employees SET 
                    name = ?, 
                    age = ?, 
                    doj = ?, 
                    email = ?, 
                    gender = ?, 
                    contact = ?, 
                    address = ?
                WHERE id = ?
            """, (name, age, doj, email, gender, contact, address, id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Update error: {e}")
            return False

    def close(self):
        self.conn.close()
