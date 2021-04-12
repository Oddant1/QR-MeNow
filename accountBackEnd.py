import sqlite3 as sql
import bcrypt


def add_account_to_data_base(username, password):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
            cur.execute("INSERT INTO users (username,password) VALUES (?,?)",
                        (username, hashed))
            con.commit()
            userId = cur.execute("SELECT userid "
                                 "FROM users WHERE username = ?", (username,)).fetchone()[0]
            print(userId)
            print('account made')

    except Exception as e:
        print(e)
