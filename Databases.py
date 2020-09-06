import mysql.connector


class Database:

    def create(self):
        mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Darkicesky466')

        mycursor = mydb.cursor()

        mycursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'studantcare'")
        myresult = mycursor.fetchall()
        if myresult [0][0] == 0:
            mycursor.execute("CREATE DATABASE if not exists studantcare")
            self.execute()

    def execute(self):
        mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Darkicesky466',
        database="studantcare")

        mycursor = mydb.cursor()


        mycursor.execute("CREATE TABLE if not exists  institution (IDINSTITUTION INT PRIMARY KEY AUTO_INCREMENT  ,EMAIL VARCHAR(255) NOT NULL , NAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(64) NOT NULL)")

        mycursor.execute("CREATE TABLE if not exists  survey (IDSURVEY INT PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(255) NOT NULL, JSON_DATA BLOB)")

        mycursor.execute("CREATE TABLE if not exists  student (IDSTUDENT INT PRIMARY KEY AUTO_INCREMENT, EMAIL VARCHAR(255) NOT NULL , NAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(64) NOT NULL,ID_INSTITUTION INT)")

        mycursor.execute("CREATE TABLE if not exists surveystudents (IDSURVEY INT, IDSTUDENT INT, JSON_DATA BLOB)")

        mycursor.execute("ALTER TABLE  student  ADD CONSTRAINT FK_INSTITUTION_STUDENT FOREIGN KEY(ID_INSTITUTION) REFERENCES institution(IDINSTITUTION)")

        mycursor.execute("ALTER TABLE  surveystudents  ADD CONSTRAINT FK_SURVEY FOREIGN KEY(IDSURVEY) REFERENCES survey(IDSURVEY)")

        mycursor.execute("ALTER TABLE  surveystudents  ADD CONSTRAINT FK_STUDENT FOREIGN KEY(IDSTUDENT) REFERENCES student(IDSTUDENT)")
