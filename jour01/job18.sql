mysql> delete from etudiant
    -> where id = 3
    -> ;
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM etudiant;
+----+-----------+----------+-----+---------------------------------+
| ID | NOM       | PRENOM   | AGE | EMAIL                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Betty    |  20 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+-----------+----------+-----+---------------------------------+
5 rows in set (0.00 sec)