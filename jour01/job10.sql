mysql> select nom, prenom, age, email
    -> from etudiant
    -> order by age desc
    -> ;
+---------+-----------+-----+---------------------------------+
| nom     | prenom    | age | email                           |
+---------+-----------+-----+---------------------------------+
| Chuck   | Steack    |  45 | chuck.steak@laplateforme.io     |
| Betty   | Spaghetti |  23 | betty.Spaghetti@laplateforme.io |
| Gertude | Dupuis    |  20 | gertrude.dupuis@laplateforme.io |
| John    | Doe       |  18 | john.doe@laplateforme.io        |
| Binkie  | Barnes    |  16 | binkie.barnes@laplateforme.io   |
+---------+-----------+-----+---------------------------------+
5 rows in set (0.00 sec)