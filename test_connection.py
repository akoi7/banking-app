from database import Database

def test_connection():
    try:
        db = Database()
        print("✅ Successfully connected to MySQL!")
        db.execute("SHOW TABLES", fetch=True)  # Test query
        print("✅ Database tables:", db.execute("SHOW TABLES", fetch=True))
        db.close()
    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    test_connection()
