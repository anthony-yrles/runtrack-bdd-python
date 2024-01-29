mysql> update etudiant
    -> set age = 20
    -> where nom = 'gertude'
    -> ;
Query OK, 0 rows affected (0.00 sec)
Rows matched: 1  Changed: 0  Warnings: 0

mysql> select *
    -> from etudiant
    -> where nom = 'gertude'
    -> ;
+----+---------+--------+-----+---------------------------------+
| id | nom     | prenom | age | email                           |
+----+---------+--------+-----+---------------------------------+
|  5 | Gertude | Dupuis |  20 | gertrude.dupuis@laplateforme.io |
+----+---------+--------+-----+---------------------------------+
1 row in set (0.00 sec)