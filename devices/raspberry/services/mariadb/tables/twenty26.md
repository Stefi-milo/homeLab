MariaDB [twenty26]> show tables;
+--------------------+
| Tables_in_twenty26 |
+--------------------+
| debt               |
| fitness            |
| funtries           |
| lifestyle          |
| sport              |
| weight             |
+--------------------+
6 rows in set (0.000 sec)

MariaDB [twenty26]> describe debt;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| Name      | varchar(255) | NO   |     |         |       |
| Borrowed  | int(11)      | NO   |     | 0       |       |
| Returned  | int(11)      | NO   |     | 0       |       |
| Exception | int(11)      | NO   |     | 0       |       |
| Debt      | int(11)      | NO   |     | 0       |       |
| Date      | date         | NO   |     | NULL    |       |
| Owe       | int(11)      | NO   |     | 0       |       |
+-----------+--------------+------+-----+---------+-------+
7 rows in set (0.001 sec)

MariaDB [twenty26]> describe fitness;
+------------+---------+------+-----+---------+-------+
| Field      | Type    | Null | Key | Default | Extra |
+------------+---------+------+-----+---------+-------+
| Date       | date    | NO   | PRI | NULL    |       |
| Pushups    | int(11) | NO   |     | 0       |       |
| Jumping    | int(11) | NO   |     | 0       |       |
| Excercises | int(11) | NO   |     | 0       |       |
| Stretching | int(11) | NO   |     | 0       |       |
+------------+---------+------+-----+---------+-------+
5 rows in set (0.001 sec)

MariaDB [twenty26]> describe funtries;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| Try1  | int(11) | NO   |     | 0       |       |
| Try2  | int(11) | NO   |     | 0       |       |
| Try3  | int(11) | NO   |     | 0       |       |
| Try4  | int(11) | NO   |     | 0       |       |
| Try5  | int(11) | NO   |     | 0       |       |
| Date  | date    | YES  |     | NULL    |       |
| Try6  | int(11) | NO   |     | 0       |       |
| Try7  | int(11) | NO   |     | 0       |       |
| Try8  | int(11) | NO   |     | 0       |       |
| Try9  | int(11) | NO   |     | 0       |       |
| Try10 | int(11) | NO   |     | 0       |       |
| Try13 | int(11) | NO   |     | 0       |       |
| Try11 | int(11) | NO   |     | 0       |       |
| Try12 | int(11) | NO   |     | 0       |       |
| Try14 | int(11) | NO   |     | 0       |       |
| Try15 | int(11) | NO   |     | 0       |       |
| Try16 | int(11) | NO   |     | 0       |       |
| Try17 | int(11) | NO   |     | 0       |       |
| Try18 | int(11) | NO   |     | 0       |       |
| Try19 | int(11) | NO   |     | 0       |       |
| Try20 | int(11) | NO   |     | 0       |       |
| Try21 | int(11) | NO   |     | 0       |       |
+-------+---------+------+-----+---------+-------+
22 rows in set (0.001 sec)

MariaDB [twenty26]> describe lifestyle;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| Beer  | int(11) | NO   |     | 0       |       |
| Smoke | int(11) | NO   |     | 0       |       |
| Fun   | int(11) | NO   |     | 0       |       |
| Sport | int(11) | NO   |     | 0       |       |
| Date  | date    | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
5 rows in set (0.001 sec)

MariaDB [twenty26]> describe sport;
+-----------+---------+------+-----+---------+-------+
| Field     | Type    | Null | Key | Default | Extra |
+-----------+---------+------+-----+---------+-------+
| Running   | int(11) | NO   |     | 0       |       |
| Gym       | int(11) | NO   |     | 0       |       |
| Swim      | int(11) | NO   |     | 0       |       |
| Karate    | int(11) | NO   |     | 0       |       |
| Date      | date    | YES  | UNI | NULL    |       |
| Badminton | int(11) | NO   |     | 0       |       |
| Squash    | int(11) | NO   |     | 0       |       |
| Walk      | int(11) | NO   |     | 0       |       |
+-----------+---------+------+-----+---------+-------+
8 rows in set (0.001 sec)

MariaDB [twenty26]> describe weight;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| Date        | date         | NO   |     | NULL    |       |
| WeightValue | decimal(5,2) | NO   |     | 0.00    |       |
+-------------+--------------+------+-----+---------+-------+
2 rows in set (0.001 sec)
