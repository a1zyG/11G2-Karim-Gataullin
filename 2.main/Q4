import sqlite3

base = sqlite3.connect('namber4.db')

cursor = base.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS "polisovateli" (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
login TEXT NOT NULL,
password TEXT NOT NULL,
yroven_dostupa INTEGER NOT NULL
)''')
base.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS "kategorii_polisovateli" (
id INTEGER PRIMARY KEY,
k_yroven_dostupa INTEGER,
where_work TEXT NOT NULL,
FOREIGN KEY("k_yroven_dostupa") REFERENCES polisovateli(yroven_dostupa)
)''')
base.commit()

cursor.execute('''
INSERT INTO 'polisovateli' (name, login, password, yroven_dostupa) VALUES
('Alex', 'Alex123', 'A123', 1),
('Potter', 'Potter', 'password123', 2),
('Petr1', 'tsar', '1', 1),
('Anknown', 'IDomtKnow', 'parol123', 3);
''')
base.commit()

cursor.execute('''
INSERT INTO kategorii_polisovateli (k_yroven_dostupa, where_work) VALUES
(3, 'Moscow'),
(1, 'Sankt_Peterburg'),
(2, 'Los_Angeles'),
(1, 'Rostov')
''')
base.commit()

cursor.execute('''
SELECT * 
FROM 'kategorii_polisovateli' 
INNER JOIN 'polisovateli' ON yroven_dostupa = k_yroven_dostupa
''')
base.commit()

result = cursor.fetchall()
print(result)

base.commit()


# ---------------------------------------------------------------------------------------

import unittest
import sqlite3


class TestTable(unittest.TestCase):
    def setUp(self):
        self.rus = "QWERTYUIOPASDGFHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_-@$!?1234567890 "
        self.login = "QWERTYUIOPASDGFHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_-@$!?1234567890 "
        self.name = 'namber4.db'
        self.base = sqlite3.connect(self.name)
        self.cursor = self.base.cursor()

    def test_connection(self) :
        self.cursor.execute('''
        SELECT *
        FROM kategorii_polisovateli
        INNER JOIN polisovateli ON yroven_dostupa = k_yroven_dostupa
        ''')
        result = self.cursor.fetchall()
        for res in result:
            self.assertEqual(res[1], res[7])

    def test_unique_ids(self) :
        self.cursor.execute('''
        SELECT id
        FROM kategorii_polisovateli
        ''')
        result = self.cursor.fetchall()
        self.assertEqual(len(result), len(set(result)))

        self.cursor.execute('''
        SELECT id
        FROM polisovateli
        ''')
        result = self.cursor.fetchall()
        self.assertEqual(len(result), len(set(result)))

    def test_name_and_login(self) :
        self.cursor.execute('''
        SELECT name
        FROM polisovateli
        ''')
        result = self.cursor.fetchall()
        for name in result:
            name = str(name[0])
            for letter in name:
                self.assertIn(letter.lower(), self.rus)

        self.cursor.execute('''
        SELECT login
        FROM polisovateli
        ''')
        result = self.cursor.fetchall()
        for name in result:
            name = str(name[0])
            for letter in name:
                self.assertIn(letter.lower(), self.login)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
