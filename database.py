import sqlite3

DB_NAME = "expense.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    # Income table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS income(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL,
        income_date TEXT
    )
    """)

    # Expenses table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        amount REAL,
        category TEXT,
        expense_date TEXT,
        notes TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------------------------------------------
# USER FUNCTIONS
# ---------------------------------------------------

def create_user(username, email, password):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users(username,email,password) VALUES(?,?,?)",
            (username, email, password)
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def get_user(email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cur.fetchone()
    conn.close()

    return user


# ---------------------------------------------------
# INCOME FUNCTIONS
# ---------------------------------------------------

def add_income(user_id, amount, date):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO income(
            user_id,
            amount,
            income_date
        )
        VALUES(?,?,?)
        """,
        (
            user_id,
            amount,
            date
        )
    )

    conn.commit()
    conn.close()


def get_income(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, amount, income_date
        FROM income
        WHERE user_id=?
        ORDER BY income_date DESC
        """,
        (user_id,)
    )

    data = cursor.fetchall()
    conn.close()

    columns = ["id", "amount", "income_date"]

    return [dict(zip(columns, row)) for row in data]


def total_income(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT IFNULL(SUM(amount),0) FROM income WHERE user_id=?",
        (user_id,)
    )

    total = cursor.fetchone()[0]
    conn.close()

    return total


# ---------------------------------------------------
# EXPENSE FUNCTIONS
# ---------------------------------------------------

def add_expense(
    user_id,
    title,
    amount,
    category,
    date,
    notes
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO expenses(
            user_id,
            title,
            amount,
            category,
            expense_date,
            notes
        )
        VALUES(?,?,?,?,?,?)
        """,
        (
            user_id,
            title,
            amount,
            category,
            date,
            notes
        )
    )

    conn.commit()
    conn.close()


def get_expenses(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            title,
            category,
            amount,
            expense_date,
            notes
        FROM expenses
        WHERE user_id=?
        ORDER BY expense_date DESC
        """,
        (user_id,)
    )

    data = cursor.fetchall()
    conn.close()

    columns = [
        "id",
        "title",
        "category",
        "amount",
        "expense_date",
        "notes"
    ]

    return [dict(zip(columns, row)) for row in data]


def total_expense(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT IFNULL(SUM(amount),0) FROM expenses WHERE user_id=?",
        (user_id,)
    )

    total = cursor.fetchone()[0]
    conn.close()

    return total


def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )

    conn.commit()
    conn.close()
    