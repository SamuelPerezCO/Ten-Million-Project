import sqlite3
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

DB_PATH = Path(__file__).with_name("ten_million.db")


def _get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db() -> None:
    with _get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                amount INTEGER NOT NULL CHECK(amount > 0),
                type TEXT NOT NULL CHECK(type IN ('deposit', 'withdraw')),
                category TEXT,
                note TEXT,
                created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
            );
            """
        )
        conn.execute("CREATE INDEX IF NOT EXISTS idx_transactions_created_at ON transactions(created_at);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_transactions_type ON transactions(type);")


def create_savings(
    title: str,
    amount: int,
    tx_type: str = "deposit",
    category: Optional[str] = None,
    note: Optional[str] = None,
) -> int:
    title = (title or "").strip()
    if not title:
        raise ValueError("title is required")

    if not isinstance(amount, int):
        raise ValueError("amount must be int")
    if amount <= 0:
        raise ValueError("amount must be > 0")

    if tx_type not in ("deposit", "withdraw"):
        raise ValueError("type must be 'deposit' or 'withdraw'")

    category = (category.strip() if category else None)
    note = (note.strip() if note else None)

    with _get_conn() as conn:
        cur = conn.execute(
            """
            INSERT INTO transactions (title, amount, type, category, note)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, amount, tx_type, category, note),
        )
        return int(cur.lastrowid)


def read_savings(
    limit: int = 200,
    offset: int = 0,
    search: Optional[str] = None,
    tx_type: Optional[str] = None,
) -> List[Dict[str, Any]]:
    if limit <= 0:
        raise ValueError("limit must be > 0")
    if offset < 0:
        raise ValueError("offset must be >= 0")

    params: List[Any] = []
    where: List[str] = []

    if search:
        s = f"%{search.strip()}%"
        where.append("(title LIKE ? OR category LIKE ? OR note LIKE ?)")
        params.extend([s, s, s])

    if tx_type:
        if tx_type not in ("deposit", "withdraw"):
            raise ValueError("tx_type must be 'deposit' or 'withdraw'")
        where.append("type = ?")
        params.append(tx_type)

    where_sql = (" WHERE " + " AND ".join(where)) if where else ""

    with _get_conn() as conn:
        rows = conn.execute(
            f"""
            SELECT id, title, amount, type, category, note, created_at
            FROM transactions
            {where_sql}
            ORDER BY datetime(created_at) DESC, id DESC
            LIMIT ? OFFSET ?
            """,
            (*params, limit, offset),
        ).fetchall()

    return [dict(r) for r in rows]


def update_savings(
    tx_id: int,
    title: Optional[str] = None,
    amount: Optional[int] = None,
    tx_type: Optional[str] = None,
    category: Optional[str] = None,
    note: Optional[str] = None,
) -> bool:
    if not isinstance(tx_id, int) or tx_id <= 0:
        raise ValueError("tx_id must be a positive int")

    fields: List[str] = []
    params: List[Any] = []

    if title is not None:
        t = title.strip()
        if not t:
            raise ValueError("title cannot be empty")
        fields.append("title = ?")
        params.append(t)

    if amount is not None:
        if not isinstance(amount, int):
            raise ValueError("amount must be int")
        if amount <= 0:
            raise ValueError("amount must be > 0")
        fields.append("amount = ?")
        params.append(amount)

    if tx_type is not None:
        if tx_type not in ("deposit", "withdraw"):
            raise ValueError("type must be 'deposit' or 'withdraw'")
        fields.append("type = ?")
        params.append(tx_type)

    if category is not None:
        c = category.strip() if category.strip() else None
        fields.append("category = ?")
        params.append(c)

    if note is not None:
        n = note.strip() if note.strip() else None
        fields.append("note = ?")
        params.append(n)

    if not fields:
        return False

    params.append(tx_id)

    with _get_conn() as conn:
        cur = conn.execute(
            f"""
            UPDATE transactions
            SET {", ".join(fields)}
            WHERE id = ?
            """,
            params,
        )
        return cur.rowcount > 0


def delete_savings(tx_id: int) -> bool:
    if not isinstance(tx_id, int) or tx_id <= 0:
        raise ValueError("tx_id must be a positive int")

    with _get_conn() as conn:
        cur = conn.execute("DELETE FROM transactions WHERE id = ?", (tx_id,))
        return cur.rowcount > 0


def totals() -> Dict[str, int]:
    with _get_conn() as conn:
        dep = conn.execute(
            "SELECT COALESCE(SUM(amount), 0) AS s FROM transactions WHERE type = 'deposit'"
        ).fetchone()["s"]
        wd = conn.execute(
            "SELECT COALESCE(SUM(amount), 0) AS s FROM transactions WHERE type = 'withdraw'"
        ).fetchone()["s"]

    dep_i = int(dep or 0)
    wd_i = int(wd or 0)
    return {
        "deposits": dep_i,
        "withdrawals": wd_i,
        "balance": dep_i - wd_i,
        "goal": 10_000_000,
        "remaining": max(0, 10_000_000 - (dep_i - wd_i)),
    }