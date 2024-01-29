mysql> delete from etudiant
    -> where id = 6
    -> ;
Query OK, 1 row affected (0.00 sec)

mysql> select * from etudiant
    -> ;
+----+---------+-----------+-----+---------------------------------+
| id | nom     | prenom    | age | email                           |
+----+---------+-----------+-----+---------------------------------+
|  1 | Betty   | Spaghetti |  23 | betty.Spaghetti@laplateforme.io |
|  2 | Chuck   | Steack    |  45 | chuck.steak@laplateforme.io     |
|  3 | John    | Doe       |  18 | john.doe@laplateforme.io        |
|  4 | Binkie  | Barnes    |  16 | binkie.barnes@laplateforme.io   |
|  5 | Gertude | Dupuis    |  20 | gertrude.dupuis@laplateforme.io |
+----+---------+-----------+-----+---------------------------------+
5 rows in set (0.00 sec)