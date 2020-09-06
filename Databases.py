import mysql.connector


class Database:

    def create(self):
        mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Darkicesky466')

        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE if not exists studantcare")

    def execute(self):
        mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Darkicesky466',
        database="studantcare")

        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE if not exists  institution (IDINSTITUTION INT PRIMARY KEY AUTO_INCREMENT  ,EMAIL VARCHAR(255) NOT NULL , NAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(64) NOT NULL, ID_STUDENT INT, ID_SURVEY INT)")

        mycursor.execute("CREATE TABLE if not exists  survey (IDSURVEY INT PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(255) NOT NULL, JSON_DATA BLOB)")

        mycursor.execute("CREATE TABLE if not exists  student (IDSTUDENT INT PRIMARY KEY AUTO_INCREMENT, EMAIL VARCHAR(255) NOT NULL , NAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(64) NOT NULL, ID_SURVEY INT)")


        mycursor.execute("ALTER TABLE  student  ADD CONSTRAINT FK_SURVEY_STUDENT FOREIGN KEY(ID_SURVEY) REFERENCES survey(IDSURVEY)")

        mycursor.execute("ALTER TABLE institution ADD CONSTRAINT FK_STUDENT_INSTITUTION FOREIGN KEY(ID_STUDENT) REFERENCES student(IDSTUDENT)")

        mycursor.execute("ALTER TABLE institution ADD CONSTRAINT FK_SURVEY_INSTITUTION FOREIGN KEY(ID_SURVEY) REFERENCES survey(IDSURVEY)")