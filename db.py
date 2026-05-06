import sqlite3

DB_PATH = "feather.db"


def init_db():
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        CREATE TABLE IF NOT EXISTS feathered (
            user_id INTEGER PRIMARY KEY
        )
    """)
    con.commit()
    con.close()


def is_feathered(user_id: int) -> bool:
    con = sqlite3.connect(DB_PATH)
    row = con.execute(
        "SELECT 1 FROM feathered WHERE user_id = ?", (user_id,)
    ).fetchone()
    con.close()
    return row is not None


def add_feather(user_id: int):
    con = sqlite3.connect(DB_PATH)
    con.execute(
        "INSERT OR IGNORE INTO feathered (user_id) VALUES (?)", (user_id,)
    )
    con.commit()
    con.close()


def remove_feather(user_id: int):
    con = sqlite3.connect(DB_PATH)
    con.execute("DELETE FROM feathered WHERE user_id = ?", (user_id,))
    con.commit()
    con.close()


def list_feathered() -> list[int]:
    """Вернуть список всех user_id с баффом (для отладки)."""
    con = sqlite3.connect(DB_PATH)
    rows = con.execute("SELECT user_id FROM feathered").fetchall()
    con.close()
    return [r[0] for r in rows]
