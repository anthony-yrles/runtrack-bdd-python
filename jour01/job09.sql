mysql> select nom, prenom, age, email
    -> from etudiant
    -> order by age
    -> ;
+---------+-----------+-----+---------------------------------+
| nom     | prenom    | age | email                           |
+---------+-----------+-----+---------------------------------+
| Binkie  | Barnes    |  16 | binkie.barnes@laplateforme.io   |
| John    | Doe       |  18 | john.doe@laplateforme.io        |
| Gertude | Dupuis    |  20 | gertrude.dupuis@laplateforme.io |
| Betty   | Spaghetti |  23 | betty.Spaghetti@laplateforme.io |
| Chuck   | Steack    |  45 | chuck.steak@laplateforme.io     |
+---------+-----------+-----+---------------------------------+