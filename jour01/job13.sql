mysql> select * from etudiant where age >= 18 and age <= 25;
+----+---------+-----------+-----+---------------------------------+
| id | nom     | prenom    | age | email                           |
+----+---------+-----------+-----+---------------------------------+
|  1 | Betty   | Spaghetti |  23 | betty.Spaghetti@laplateforme.io |
|  3 | John    | Doe       |  18 | john.doe@laplateforme.io        |
|  5 | Gertude | Dupuis    |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis  | Martin    |  18 | martin.dupuis@laplateforme.io   |
+----+---------+-----------+-----+---------------------------------+
4 rows in set (0.00 sec)