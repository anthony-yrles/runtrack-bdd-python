mysql> select nom, prenom, age, email
    -> from etudiant
    -> order by nom
    -> ;
+---------+-----------+-----+---------------------------------+
| nom     | prenom    | age | email                           |
+---------+-----------+-----+---------------------------------+
| Betty   | Spaghetti |  23 | betty.Spaghetti@laplateforme.io |
| Binkie  | Barnes    |  16 | binkie.barnes@laplateforme.io   |
| Chuck   | Steack    |  45 | chuck.steak@laplateforme.io     |
| Dupuis  | Martin    |  18 | martin.dupuis@laplateforme.io   |
| Gertude | Dupuis    |  20 | gertrude.dupuis@laplateforme.io |
| John    | Doe       |  18 | john.doe@laplateforme.io        |
+---------+-----------+-----+---------------------------------+
6 rows in set (0.00 sec)