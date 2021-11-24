1. UPDATE User SET sign_up_date = SUBSTR(sign_up_date, 7, 4) || '-' || SUBSTR(sign_up_date, 4, 2) || '-' || SUBSTR(sign_up_date, 1, 2);

2. SELECT login FROM User ORDER BY sign_up_date DESC LIMIT 1;

3. SELECT DISTINCT(SUBSTR(birthday, 1, 4)) FROM User;

4. SELECT COUNT(*) AS 'total_items' FROM product;

5. SELECT AVG(CAST((julianday('now') - julianday(birthday)) AS INTEGER) / 365) FROM login WHERE (CAST((julianday('now') - julianday(sign_up_date)) AS INTEGER) <= 61);
