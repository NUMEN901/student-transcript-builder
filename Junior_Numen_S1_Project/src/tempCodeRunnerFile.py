select  count(*)  from students s where student_population_year_ref = '2021' group by student_population_code_ref  having student_population_code_ref = 'ISM'")
    data=cursor.fetchall()