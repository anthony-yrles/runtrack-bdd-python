mysql> select count(*)
    -> from etudiant
    -> where age >= 18 and age <= 25
    -> ;
+----------+
| count(*) |
+----------+
|        3 |
+----------+
1 row in set (0.00 sec)