mysql> UPDATE etudiant
    -> set age = 20
    -> where nom = 'Spaghetti'
    -> ;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM etudiant
    -> WHERE nom = 'Spaghetti'
    -> ;
+----+-----------+--------+-----+---------------------------------+
| ID | NOM       | PRENOM | AGE | EMAIL                           |
+----+-----------+--------+-----+---------------------------------+
|  1 | Spaghetti | Betty  |  20 | betty.Spaghetti@laplateforme.io |
+----+-----------+--------+-----+---------------------------------+
1 row in set (0.00 sec)