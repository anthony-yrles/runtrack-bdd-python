mysql> select count(*)
    -> FROM etudiant
    -> WHERE AGE BETWEEN 18 AND 25;
+----------+
| count(*) |
+----------+
|        3 |
+----------+
1 row in set (0.00 sec)