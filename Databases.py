import mysql.connector
from Environ import Env


class Database:

    def create(self):
        mydb = mysql.connector.connect(
            host=f'{Env.host}',
            user=f'{Env.user}',
            password=f'{Env.password}'
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'studentcare'")
        myresult = mycursor.fetchall()
        if myresult [0][0] == 0:
            mycursor.execute("CREATE DATABASE if not exists studentcare")
            self.execute()

    def execute(self):
        mydb = mysql.connector.connect(
            host=f'{Env.host}',
            user=f'{Env.user}',
            password=f'{Env.password}',
            database=f'{Env.database}'
        )

        mycursor = mydb.cursor()


        mycursor.execute("CREATE TABLE if not exists  institution (IDINSTITUTION INT PRIMARY KEY AUTO_INCREMENT  ,EMAIL VARCHAR(255) NOT NULL , NAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(64) NOT NULL, CONSTRAINT UC_institution UNIQUE (EMAIL))")

        mycursor.execute("CREATE TABLE if not exists  survey (IDSURVEY INT PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(255) NOT NULL, JSON_DATA JSON, SCORE INT DEFAULT 0 )")

        mycursor.execute("CREATE TABLE if not exists  student (IDSTUDENT INT PRIMARY KEY AUTO_INCREMENT, EMAIL VARCHAR(255) NOT NULL , NAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(64) NOT NULL,ID_INSTITUTION INT,CONSTRAINT UC_student UNIQUE (EMAIL))")

        mycursor.execute("CREATE TABLE if not exists surveystudents (IDSURVEY INT NOT NULL, IDSTUDENT INT NOT NULL, JSON_DATA JSON, RESULT INT DEFAULT 0)")

        mycursor.execute("ALTER TABLE  student  ADD CONSTRAINT FK_INSTITUTION_STUDENT FOREIGN KEY(ID_INSTITUTION) REFERENCES institution(IDINSTITUTION)")

        mycursor.execute("ALTER TABLE  surveystudents  ADD CONSTRAINT FK_SURVEY FOREIGN KEY(IDSURVEY) REFERENCES survey(IDSURVEY)")

        mycursor.execute("ALTER TABLE  surveystudents  ADD CONSTRAINT FK_STUDENT FOREIGN KEY(IDSTUDENT) REFERENCES student(IDSTUDENT)")