mysql> select count(*)
    -> from etudiant
    -> where age < 18
    -> ;
+----------+
| count(*) |
+----------+
|        1 |
+----------+
1 row in set (0.00 sec)