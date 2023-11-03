import sqlite3


def check_login(login, password):
    user = [login, password]

    db = sqlite3.connect("users.db")
    cur = db.cursor()
    combos = cur.execute("SELECT username, password FROM users").fetchall()
    for a in combos:
        if user == list(a):
            db.close()
            return 1
    db.close()
    return 0


def register_user(login, password):
    dab = sqlite3.connect("users.db")
    cursr = dab.cursor()
    if not check_login(login, password):
        dat = (login, password)
        cursr.execute("INSERT INTO users VALUES(?, ?)", dat)
        dab.commit()
    dab.close()
