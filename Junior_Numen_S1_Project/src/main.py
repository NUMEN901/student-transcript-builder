from flask import Flask, redirect, url_for, render_template, request, session,jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib


app = Flask(__name__, template_folder='C:\\Users\\Junior NUMEN\\Junior_Numen_S1_Project\\site\\templates')

 # This line sets the secret key for the Flask application, which is used to keep client-side sessions secure. 

#database connection details

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sc19A0282001@&'
app.config['MYSQL_DB'] = 'epi_db_s1_p'

#initializing MySQL
mysql = MySQL(app)

@app.route('/')
def home():
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select  count(*)  from students s where student_population_year_ref = '2021' group by student_population_code_ref  having student_population_code_ref = 'ISM'")
    data=cursor.fetchall()
    cursor.close()
    cursor2=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor2.execute("select  count(*)  from students s where student_population_year_ref = '2021' group by student_population_code_ref  having student_population_code_ref = 'CS'") 
    data2=cursor2.fetchall()
    cursor2.close()
    cursor3=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor3.execute("select  count(*)  from students s where student_population_year_ref = '2021' group by student_population_code_ref  having student_population_code_ref = 'DSA'")
    data3=cursor3.fetchall()
    cursor3.close()
    cursor4=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor4.execute("select  count(*)  from students s where student_population_year_ref = '2021' group by student_population_code_ref  having student_population_code_ref = 'AIs'")
    data4=cursor4.fetchall()
    cursor4.close()
    cursor5=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor5.execute("select  count(*)  from students s where student_population_year_ref = '2021' group by student_population_code_ref  having student_population_code_ref = 'SE'")
    data5=cursor5.fetchall()
    cursor5.close()
    cursor6=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor6.execute("select  count(*)  from students s where student_population_year_ref = '2020' group by student_population_code_ref  having student_population_code_ref = 'ISM'")
    data6=cursor6.fetchall()
    cursor6.close()
    cursor7=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor7.execute("select  count(*)  from students s where student_population_year_ref = '2020' group by student_population_code_ref  having student_population_code_ref = 'CS'")
    data7=cursor7.fetchall()
    cursor7.close()
    cursor8=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor8.execute("select  count(*)  from students s where student_population_year_ref = '2020' group by student_population_code_ref  having student_population_code_ref = 'DSA'")
    data8=cursor8.fetchall()
    cursor8.close()
    cursor9=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor9.execute("select  count(*)  from students s where student_population_year_ref = '2020' group by student_population_code_ref  having student_population_code_ref = 'AIs'")
    data9=cursor9.fetchall()
    cursor9.close()
    cursor10=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor10.execute("select  count(*)  from students s where student_population_year_ref = '2020' group by student_population_code_ref  having student_population_code_ref = 'SE'")
    data10=cursor10.fetchall()
    cursor10.close()
    query6_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='ISM'and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor6_0_2020 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor6_0_2020.execute(query6_0_2020)
    attendance_ISM_present_2020 = cursor6_0_2020.fetchall()
    query_6_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='ISM' and s.student_population_year_ref='2020'"
    cursor6_1_2020 =mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor6_1_2020.execute(query_6_1_2020)
    attendance_ISM_total_2020 = cursor6_1_2020.fetchall()
    print(attendance_ISM_total_2020)
    attendance_ISM_present_sum_2020 = [
        attendance_ISM_present_2020[i]["count(a.attendance_presence)"]
        for i in range(len(attendance_ISM_present_2020))
    ]
    attendance_ISM_2020 = (
        sum(attendance_ISM_present_sum_2020) / attendance_ISM_total_2020[0]["count(a.attendance_presence)"]
    ) * 100
    query6_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='ISM'and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor6_0_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor6_0_2021.execute(query6_0_2021)
    attendance_ISM_present_2021 = cursor6_0_2021.fetchall()
    query_6_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='ISM' and s.student_population_year_ref='2021'"
    cursor6_1_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor6_1_2021.execute(query_6_1_2021)
    attendance_ISM_total_2021 = cursor6_1_2021.fetchall()
    attendance_ISM_present_sum_2021 = [
        attendance_ISM_present_2021[i]["count(a.attendance_presence)"]
        for i in range(len(attendance_ISM_present_2021))
    ]
    attendance_ISM_2021 = (
        sum(attendance_ISM_present_sum_2021) / attendance_ISM_total_2021[0]["count(a.attendance_presence)"]
    ) * 100
    query7_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='DSA' and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor7_0_2020 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor7_0_2020.execute(query7_0_2020)
    attendance_DSA_present_2020 = cursor7_0_2020.fetchall()
    query7_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='DSA' and s.student_population_year_ref='2020'"
    cursor7_1_2020 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor7_1_2020.execute(query7_1_2020)
    attendance_DSA_total_2020 = cursor7_1_2020.fetchall()
    attendance_DSA_present_sum_2020 = [
        attendance_DSA_present_2020[i]["count(a.attendance_presence)"]
        for i in range(len(attendance_DSA_present_2020))
    ]
    attendance_DSA_2020 = (
        sum(attendance_DSA_present_sum_2020) / attendance_DSA_total_2020[0]["count(a.attendance_presence)"]
    ) * 100
    query7_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='DSA' and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor7_0_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor7_0_2021.execute(query7_0_2021)
    attendance_DSA_present_2021 = cursor7_0_2021.fetchall()
    query7_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='DSA' and s.student_population_year_ref='2021'"
    cursor7_1_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor7_1_2021.execute(query7_1_2021)
    attendance_DSA_total_2021 = cursor7_1_2021.fetchall()
    attendance_DSA_present_sum_2021 = [
        attendance_DSA_present_2021[i]["count(a.attendance_presence)"]
        for i in range(len(attendance_DSA_present_2021))
    ]
    attendance_DSA_2021 = (
        sum(attendance_DSA_present_sum_2021) / attendance_DSA_total_2021[0]["count(a.attendance_presence)"]
    ) * 100
    query8_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='CS' and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor8_0_2020 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor8_0_2020.execute(query8_0_2020)
    attendance_CS_present_2020 = cursor8_0_2020.fetchall()
    query8_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='CS' and s.student_population_year_ref='2020'"
    cursor8_1_2020 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor8_1_2020.execute(query8_1_2020)
    attendance_CS_total_2020 = cursor8_1_2020.fetchall()
    attendance_CS_present_sum_2020 = [
        attendance_CS_present_2020[i]["count(a.attendance_presence)"] for i in range(len(attendance_CS_present_2020))
    ]
    attendance_CS_2020 = (
        sum(attendance_CS_present_sum_2020) / attendance_CS_total_2020[0]["count(a.attendance_presence)"]
    ) * 100
    query8_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='CS' and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor8_0_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor8_0_2021.execute(query8_0_2021)
    attendance_CS_present_2021 = cursor8_0_2021.fetchall()
    query8_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='CS' and s.student_population_year_ref='2021'"
    cursor8_1_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor8_1_2021.execute(query8_1_2021)
    attendance_CS_total_2021 = cursor8_1_2021.fetchall()
    attendance_CS_present_sum_2021 = [
        attendance_CS_present_2021[i]["count(a.attendance_presence)"] for i in range(len(attendance_CS_present_2021))
    ]
    attendance_CS_2021 = (
        sum(attendance_CS_present_sum_2021) / attendance_CS_total_2021[0]["count(a.attendance_presence)"]
    ) * 100
    query9_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='SE' and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor9_0_2020 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor9_0_2020.execute(query9_0_2020)
    attendance_SE_present_2020 = cursor9_0_2020.fetchall()
    query9_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='SE' and s.student_population_year_ref='2020'"
    cursor9_1_2020 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor9_1_2020.execute(query9_1_2020)
    attendance_SE_total_2020 = cursor9_1_2020.fetchall()
    attendance_SE_present_sum_2020 = [
        attendance_SE_present_2020[i]["count(a.attendance_presence)"] for i in range(len(attendance_SE_present_2020))
    ]
    attendance_SE_2020 = (
        sum(attendance_SE_present_sum_2020) / attendance_SE_total_2020[0]["count(a.attendance_presence)"]
    ) * 100
    query9_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='SE' and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor9_0_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor9_0_2021.execute(query9_0_2021)
    attendance_SE_present_2021 = cursor9_0_2021.fetchall()
    query9_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='SE' and s.student_population_year_ref='2021'"
    cursor9_1_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor9_1_2021.execute(query9_1_2021)
    attendance_SE_total_2021 = cursor9_1_2021.fetchall()
    attendance_SE_present_sum_2021 = [
        attendance_SE_present_2021[i]["count(a.attendance_presence)"] for i in range(len(attendance_SE_present_2021))
    ]
    attendance_SE_2021 = (
        sum(attendance_SE_present_sum_2021) / attendance_SE_total_2021[0]["count(a.attendance_presence)"]
    ) * 100
    query10_0_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='AIs' and s.student_population_year_ref='2020' group by s.student_epita_email;"
    cursor10_0_2020 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor10_0_2020.execute(query10_0_2020)
    attendance_AIs_present_2020 = cursor10_0_2020.fetchall()
    query10_1_2020 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='AIs' and s.student_population_year_ref='2020'"
    cursor10_1_2020 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor10_1_2020.execute(query10_1_2020)
    attendance_AIs_total_2020 = cursor10_1_2020.fetchall()
    attendance_AIs_present_sum_2020 = [
        attendance_AIs_present_2020[i]["count(a.attendance_presence)"]
        for i in range(len(attendance_AIs_present_2020))
    ]
    attendance_AIs_2020 = (
        sum(attendance_AIs_present_sum_2020) / attendance_AIs_total_2020[0]["count(a.attendance_presence)"]
    ) * 100
    query10_0_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref where a.attendance_presence=1 and s.student_population_code_ref='AIs' and s.student_population_year_ref='2021' group by s.student_epita_email;"
    cursor10_0_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor10_0_2021.execute(query10_0_2021)
    attendance_AIs_present_2021 = cursor10_0_2021.fetchall()
    query10_1_2021 = "select count(a.attendance_presence) from students s left join attendance a on s.student_epita_email=a.attendance_student_ref and s.student_population_code_ref='AIs' and s.student_population_year_ref='2021'"
    cursor10_1_2021 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor10_1_2021.execute(query10_1_2021)
    attendance_AIs_total_2021 = cursor10_1_2021.fetchall()
    attendance_AIs_present_sum_2021 = [
        attendance_AIs_present_2021[i]["count(a.attendance_presence)"]
        for i in range(len(attendance_AIs_present_2021))
    ]
    attendance_AIs_2021 = (
        sum(attendance_AIs_present_sum_2021) / attendance_AIs_total_2021[0]["count(a.attendance_presence)"]
    ) * 100
    attendance = [
        [
            attendance_ISM_2020,
            attendance_DSA_2020,
            attendance_CS_2020,
            attendance_SE_2020,
            attendance_AIs_2020,
        ],
        [
            attendance_ISM_2021,
            attendance_DSA_2021,
            attendance_CS_2021,
            attendance_SE_2021,
            attendance_AIs_2021
    ]
    ]
    return render_template("index.html",data=data,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,data8=data8,data9=data9,data10=data10,attendance=attendance)

@app.route('/population/ISM', methods=['GET', 'POST'])
def ism_population_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"select c.contact_first_name , c.contact_last_name , s.student_contact_ref, count(CASE WHEN g.grade_score >= 10 THEN 1 END) as courses_passed from contacts c inner join students s on c.contact_email = s.student_contact_ref inner join grades g on s.student_epita_email = g.grade_student_epita_email_ref  where student_population_code_ref = 'ISM' and student_population_year_ref='{year}' group by s.student_contact_ref")#return the query for fetching the data email and courses passed. 1st and last names
    print(year)
    data1=cursor.fetchall()
    cursor.close()
    print(data1)
    return jsonify(data1)

@app.route('/population/ISM_courses', methods=['GET', 'POST'])
def ism_courses_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"SELECT s.session_course_ref ,count(s.session_course_ref) as session_count FROM students JOIN grades ON students.student_epita_email = grades.grade_student_epita_email_ref JOIN courses c ON grades.grade_course_code_ref = c.course_code left join sessions s on s.session_course_ref = c.course_code WHERE students.student_population_code_ref = 'ISM' GROUP BY session_course_ref")
    print(year)
    #return the query for fetching the data email and courses passed. 1st and last names
    data1=cursor.fetchall()
    cursor.close()
    print(data1)
    return jsonify(data1)


@app.route('/population/CS', methods=['GET', 'POST'])
def cs_population_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"select c.contact_first_name , c.contact_last_name , s.student_contact_ref, count(CASE WHEN g.grade_score >= 10 THEN 1 END) as courses_passed from contacts c inner join students s on c.contact_email = s.student_contact_ref inner join grades g on s.student_epita_email = g.grade_student_epita_email_ref  where student_population_code_ref = 'CS' and student_population_year_ref='{year}' group by s.student_contact_ref")
    print(year)
    #return the query for fetching the data email and courses passed. 1st and last names
    data2=cursor.fetchall()
    cursor.close()
    print(data2)
    return jsonify(data2)

@app.route('/population/CS_courses', methods=['GET', 'POST'])
def cs_courses_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"SELECT s.session_course_ref ,count(s.session_course_ref) as session_count FROM students JOIN grades ON students.student_epita_email = grades.grade_student_epita_email_ref JOIN courses c ON grades.grade_course_code_ref = c.course_code left join sessions s on s.session_course_ref = c.course_code WHERE students.student_population_code_ref = 'CS' GROUP BY session_course_ref")
    print(year)
    #return the query for fetching the data email and courses passed. 1st and last names
    data2=cursor.fetchall()
    cursor.close()
    print(data2)
    return jsonify(data2)

@app.route('/population/DSA', methods=['GET', 'POST'])
def dsa_population_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"select c.contact_first_name , c.contact_last_name , s.student_contact_ref, count(CASE WHEN g.grade_score >= 10 THEN 1 END) as courses_passed from contacts c inner join students s on c.contact_email = s.student_contact_ref inner join grades g on s.student_epita_email = g.grade_student_epita_email_ref  where student_population_code_ref = 'DSA' and student_population_year_ref='{year}' group by s.student_contact_ref")
    print(year)
    #return the query for fetching the data email and courses passed. 1st and last names
    data3=cursor.fetchall()
    cursor.close()
    print(jsonify(data3))
    return jsonify(data3)


@app.route('/population/DSA_courses', methods=['GET', 'POST'])
def dsa_courses_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"SELECT s.session_course_ref ,count(s.session_course_ref) as session_count FROM students JOIN grades ON students.student_epita_email = grades.grade_student_epita_email_ref JOIN courses c ON grades.grade_course_code_ref = c.course_code left join sessions s on s.session_course_ref = c.course_code WHERE students.student_population_code_ref = 'DSA' GROUP BY session_course_ref")
    print(year)
    #return the query for fetching the data email and courses passed. 1st and last names
    data3=cursor.fetchall()
    cursor.close()
    print(data3)
    return jsonify(data3)

@app.route('/population/AIs', methods=['GET', 'POST'])
def ais_population_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"select c.contact_first_name , c.contact_last_name , s.student_contact_ref, count(CASE WHEN g.grade_score >= 10 THEN 1 END) as courses_passed from contacts c inner join students s on c.contact_email = s.student_contact_ref inner join grades g on s.student_epita_email = g.grade_student_epita_email_ref  where student_population_code_ref = 'AIs' and student_population_year_ref='{year}' group by s.student_contact_ref")
    print(year)
    #return the query for fetching the data email and courses passed. 1st and last names
    data4=cursor.fetchall()
    cursor.close()
    print(jsonify(data4))
    return jsonify(data4)

@app.route('/population/AIs_courses', methods=['GET', 'POST'])
def ais_courses_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"SELECT s.session_course_ref ,count(s.session_course_ref) as session_count FROM students JOIN grades ON students.student_epita_email = grades.grade_student_epita_email_ref JOIN courses c ON grades.grade_course_code_ref = c.course_code left join sessions s on s.session_course_ref = c.course_code WHERE students.student_population_code_ref = 'AIs' GROUP BY session_course_ref")
    print(year)
    #return the query for fetching the data email and courses passed. 1st and last names
    data4=cursor.fetchall()
    cursor.close()
    print(data4)
    return jsonify(data4)

@app.route('/population/SE', methods=['GET', 'POST'])
def se_population_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"select c.contact_first_name , c.contact_last_name , s.student_contact_ref, count(CASE WHEN g.grade_score >= 10 THEN 1 END) as courses_passed from contacts c inner join students s on c.contact_email = s.student_contact_ref inner join grades g on s.student_epita_email = g.grade_student_epita_email_ref  where student_population_code_ref = 'SE' and student_population_year_ref='{year}' group by s.student_contact_ref")
    print(year)
    #return the query for fetching the data email and courses passed. 1st and last names
    data5=cursor.fetchall()
    cursor.close()
    print(jsonify(data5))
    return jsonify(data5)

@app.route('/population/SE_courses', methods=['GET', 'POST'])
def se_courses_fetch():
    year=request.args.get('year')
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"SELECT s.session_course_ref ,count(s.session_course_ref) as session_count FROM students JOIN grades ON students.student_epita_email = grades.grade_student_epita_email_ref JOIN courses c ON grades.grade_course_code_ref = c.course_code left join sessions s on s.session_course_ref = c.course_code WHERE students.student_population_code_ref = 'SE' GROUP BY session_course_ref")
    print(year)
    #return the query for fetching the data email and courses passed. 1st and last names
    data5=cursor.fetchall()
    cursor.close()
    print(data5)
    return jsonify(data5)


@app.route('/CS.html', methods=['GET'])
def cs_population():
    year=request.args.get('year')
    return render_template("CS.html",year=year)

@app.route('/DSA.html', methods=['GET', 'POST'])
def dsa_population():
    year=request.args.get('year')
    return render_template("DSA.html",year=year)

@app.route('/AIs.html', methods=['GET', 'POST'])
def ais_population():
    year=request.args.get('year')   
    return render_template("AIs.html",year=year)

@app.route('/SE.html', methods=['GET', 'POST'])
def se_population():
    year=request.args.get('year')
    return render_template("SE.html",year=year)  

@app.route('/ISM.html', methods=['GET', 'POST'])
def ism_population():
    year=request.args.get('year')
    return render_template("ISM.html",year=year)   

@app.route("/student.html", methods=['GET', 'POST'])
def students():
    return render_template("student.html")
@app.route("/student", methods=['GET', 'POST'])
def student_fetch():
    email=request.args.get('email')
    print(email)
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"select s.student_contact_ref, c.contact_first_name , c.contact_last_name ,g.grade_course_code_ref,g.grade_score from contacts c inner join students s on c.contact_email = s.student_contact_ref inner join grades g on s.student_epita_email = g.grade_student_epita_email_ref  where s.student_contact_ref='{email}'" )
    data=cursor.fetchall()
    cursor.close()
    print(jsonify(data))
    return jsonify(data)


if __name__ == "__main__":
    app.run()