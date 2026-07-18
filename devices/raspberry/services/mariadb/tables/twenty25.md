MariaDB [twenty26]> use twenty25;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [twenty25]> show tables;
+--------------------+
| Tables_in_twenty25 |
+--------------------+
| debt               |
| funtries           |
| lifestyle          |
| sport              |
| weight             |
+--------------------+
5 rows in set (0.000 sec)

MariaDB [twenty25]> describe debt;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| Name      | varchar(255) | YES  |     | NULL    |       |
| Borrowed  | int(11)      | YES  |     | NULL    |       |
| Returned  | int(11)      | YES  |     | NULL    |       |
| Exception | int(11)      | YES  |     | NULL    |       |
| Debt      | int(11)      | YES  |     | NULL    |       |
| Date      | date         | YES  |     | NULL    |       |
| Owe       | int(11)      | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
7 rows in set (0.001 sec)

MariaDB [twenty25]> describe funtries;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| Try1  | int(11) | YES  |     | NULL    |       |
| Try2  | int(11) | YES  |     | NULL    |       |
| Try3  | int(11) | YES  |     | NULL    |       |
| Try4  | int(11) | YES  |     | NULL    |       |
| Try5  | int(11) | YES  |     | NULL    |       |
| Try6  | int(11) | YES  |     | NULL    |       |
| Try7  | int(11) | YES  |     | NULL    |       |
| Try8  | int(11) | YES  |     | NULL    |       |
| Try9  | int(11) | YES  |     | NULL    |       |
| Try10 | int(11) | YES  |     | NULL    |       |
| Try11 | int(11) | YES  |     | NULL    |       |
| Try12 | int(11) | YES  |     | NULL    |       |
| Try13 | int(11) | YES  |     | NULL    |       |
| Try14 | int(11) | YES  |     | NULL    |       |
| Try15 | int(11) | YES  |     | NULL    |       |
| Try16 | int(11) | YES  |     | NULL    |       |
| Try17 | int(11) | YES  |     | NULL    |       |
| Try18 | int(11) | YES  |     | NULL    |       |
| Try19 | int(11) | YES  |     | NULL    |       |
| Try20 | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
20 rows in set (0.005 sec)

MariaDB [twenty25]> describe lifestyle;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| Beer  | int(11) | YES  |     | NULL    |       |
| Smoke | int(11) | YES  |     | NULL    |       |
| Fun   | int(11) | YES  |     | NULL    |       |
| Sport | int(11) | YES  |     | NULL    |       |
| Date  | date    | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
5 rows in set (0.001 sec)

MariaDB [twenty25]> describe sport;
+-----------+---------+------+-----+---------+-------+
| Field     | Type    | Null | Key | Default | Extra |
+-----------+---------+------+-----+---------+-------+
| Walk      | int(11) | YES  |     | NULL    |       |
| Gym       | int(11) | YES  |     | NULL    |       |
| Swim      | int(11) | YES  |     | NULL    |       |
| Karate    | int(11) | YES  |     | NULL    |       |
| Date      | date    | YES  | UNI | NULL    |       |
| Badminton | int(11) | YES  |     | NULL    |       |
+-----------+---------+------+-----+---------+-------+
6 rows in set (0.000 sec)

MariaDB [twenty25]> describe weight;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| Date        | date         | YES  |     | NULL    |       |
| WeightValue | decimal(5,2) | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
2 rows in set (0.001 sec)
