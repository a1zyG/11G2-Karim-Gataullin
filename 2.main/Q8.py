import sqlite3

name = 'n6.db'
db = sqlite3.connect(name)

cur = db.cursor()

query = ('''
CREATE TABLE "users" (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
login TEXT NOT NULL,
rank INTEGER NOT NULL
);''')

cur.execute(query)

add1 = ('''
INSERT INTO 'users' ('name', 'login', 'rank') VALUES
('Владислав', 'Vladragone', 1),
('Петр', 'Polter', 1),
('ТН', 'voroshilova@', 2),
('Морозов ', '3d_printer', 3);
''')

cur.execute(add1)

indexing = ('''
CREATE UNIQUE INDEX 'name_rank_index' ON users(name, rank)
''')

cur.execute(indexing)

db.commit()

# ---------------------------------------------------------------------------------------


import unittest
import sqlite3


class TestTable(unittest.TestCase):
    def setUp(self):
        self.rus = "йцукенгшщзхъфывапролджэячсмитьбю "
        self.login = "qwertyuiopasdfghjklzxcvbnm_-@$!?1234567890 "
        self.name = 'n6.db'
        self.db = sqlite3.connect(self.name)
        self.cur = self.db.cursor()

    def test_unique_ids(self):
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
