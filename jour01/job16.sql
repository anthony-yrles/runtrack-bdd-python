mysql> select nom, prenom, age, email
    -> from etudiant
    -> where prenom like 'b%'
    -> ;
+--------+--------+-----+-------------------------------+
| nom    | prenom | age | email                         |
+--------+--------+-----+-------------------------------+
| Binkie | Barnes |  16 | binkie.barnes@laplateforme.io |
+--------+--------+-----+-------------------------------+
1 row in set (0.00 sec)