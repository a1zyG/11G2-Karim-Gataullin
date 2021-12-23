```import sqlite3

name = 'n7.db'
db = sqlite3.connect(name)

cur = db.cursor()

query = ('''
CREATE TABLE "users" (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
login TEXT NOT NULL,
rank INTEGER NOT NULL,
korpus INTEGER NOT NULL
);''')

query1 = ('''
CREATE TABLE "kategory" (
id INTEGER PRIMARY KEY,
people_rank INTEGER,
people_korpus INTEGER,
FOREIGN KEY("people_rank") REFERENCES users(rank),
FOREIGN KEY("people_korpus") REFERENCES users(korpus)
);''')

cur.execute(query)
cur.execute(query1)

add1 = ('''
INSERT INTO 'users' ('name', 'login', 'rank', 'korpus') VALUES
('Владислав', 'Vladragone', 1, 1),
('Петя', 'Polter', 1, 1),
('Танк', 'voroshilova@', 2, 3),
('Арматура', '3d_printer', 3, 2);
''')

cur.execute(add1)

add2 = ('''
INSERT INTO 'kategory' ('people_rank', 'people_korpus') VALUES
(3, 2),
(3, 1),
(3, 3),
(2, 1),
(2, 2),
(2, 3),
(1, 2),
(1, 1),
(1, 3);
''')

cur.execute(add2)

query = ('''
        SELECT *
        FROM 'kategory'
        INNER JOIN 'users' ON rank = people_rank
        ''')
cur.execute(query)

result = cur.fetchall()
print(result)

db.commit()

# ---------------------------------------------------------------------------------------


import unittest
import sqlite3


class TestTable(unittest.TestCase):
    def setUp(self):
        self.rus = "йцукенгшщзхъфывапролджэячсмитьбю "
        self.login = "qwertyuiopasdfghjklzxcvbnm_-@$!?1234567890 "
        self.name = 'n7.db'
        self.db = sqlite3.connect(self.name)
        self.cur = self.db.cursor()

    def test_connection(self):
        query = ('''
        SELECT rank, people_rank
        FROM 'kategory'
        INNER JOIN 'users' ON rank = people_rank
        ''')
        self.cur.execute(query)
        result = self.cur.fetchall()
        for res in result:
            self.assertEqual(res[0], res[1])

    def test_unique_ids(self):
        query = ('''
        SELECT id
        FROM 'kategory'
        ''')
        self.cur.execute(query)
        result = self.cur.fetchall()
        self.assertEqual(len(result), len(set(result)))

        query = ('''
                SELECT id
                FROM 'users'
                ''')
        self.cur.execute(query)
        result = self.cur.fetchall()
        self.assertEqual(len(result), len(set(result)))

    def test_name_and_login(self):
        query = ('''
        SELECT name
        FROM 'users'
        ''')
        self.cur.execute(query)
        result = self.cur.fetchall()
        for name in result:
            name = str(name[0])
            for letter in name:
                self.assertIn(letter.lower(), self.rus)

        query = ('''
                SELECT login
                FROM 'users'
                ''')
        self.cur.execute(query)
        result = self.cur.fetchall()
        for name in result:
            name = str(name[0])
            for letter in name:
                self.assertIn(letter.lower(), self.login)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
