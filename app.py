from flask import Flask, jsonify, request
import mysql.connector
from Environ import Env
from Databases import Database
from ml import MachineLearning

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/student/<id_institution>/surveys', methods=['GET'])
def list_student_score(id_institution):
    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )

    mycursor = mydb.cursor()
    sql = 'SELECT NAME,IDSURVEY FROM survey'

    sql2 = 'SELECT S.NAME, SS.RESULT FROM  student S INNER JOIN surveystudents SS ON S.IDSTUDENT = SS.IDSTUDENT   WHERE S.ID_INSTITUTION = %s AND IDSURVEY = %s'



    try:
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        payload = []
        payload2 = []
        if len(myresult) == 0:
            return jsonify({}),200
        for result in myresult:
            payload2.clear()
            mycursor.execute(sql2, [id_institution,result[1]])
            myresult2 = mycursor.fetchall()
            for result2 in myresult2:
                content2 = {'name': result2[0],'score':result2[1]}
                payload2.append(content2)
            content = {'name': result[0],'itens':payload2.copy()}
            payload.append(content)
        return jsonify(payload), 200

    except Exception as error:
        print(error.args)
        return jsonify({}), 500



@app.route('/survey', methods=['POST'])
def add_survey():

    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO survey (NAME,JSON_DATA) VALUES (%s, %s)"

    val = (request.json['name'], request.json['json_data'])

    sql2 = "SELECT count(*) FROM survey WHERE name = %s"

    val2 = [request.json['name']]
    try:
        mycursor.execute(sql2, val2)
        myresult = mycursor.fetchall()
        if myresult[0][0] == 0:
            mycursor.execute(sql, val)
            mydb.commit()
            return jsonify({}), 201
        elif myresult[0][0] >= 1:
            return jsonify({}), 400

    except Exception as error:
        print(error.args)
        return jsonify({}), 500


@app.route('/survey/', methods=['GET'])
def list_survey():
    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )
    mycursor = mydb.cursor()
    sql = "SELECT * from survey "
    try:
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        payload = []
        for result in myresult:
            content = {'id': result[0], 'name': result[1], 'survey': result[2]}
            payload.append(content)
        return jsonify(payload), 200

    except Exception as error:
        print(error.args)
        return jsonify({}), 500


@app.route('/surveystudents', methods=['POST'])
def add_surveystudent():

    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO surveystudents (IDSURVEY, IDSTUDENT,JSON_DATA) VALUES (%s, %s, %s)"

    sql2 = "SELECT count(*)  FROM surveystudents WHERE  IDSURVEY = %s AND IDSTUDENT = %s"

    sql3 = "UPDATE surveystudents SET JSON_DATA = %s WHERE IDSURVEY = %s and IDSTUDENT = %s"

    sql4 = "SELECT name FROM survey WHERE IDSURVEY = %s"

    sql5 = "UPDATE surveystudents SET RESULT = %s WHERE IDSURVEY = %s and IDSTUDENT = %s"

    sql6 = "UPDATE survey SET SCORE = %s WHERE IDSURVEY = %s"

    val = (request.json['IDSURVEY'], request.json['IDSTUDENT'], request.json['json_data'])

    val2 = (request.json['IDSURVEY'], request.json['IDSTUDENT'])

    val3 = (request.json['json_data'],request.json['IDSURVEY'],request.json['IDSTUDENT'])

    val4 = [request.json['IDSURVEY']]




    try:
        def pesquisa_nome(data, idSurvey, idStudent):
            mycursor.execute(sql4,val4)
            myresult2 = mycursor.fetchall()
            if myresult2[0][0] == 'Pesquisa studentcare':
                from Avaliacao.Pesquisa1 import Pesquisa1
                x = Pesquisa1()
                z = x.convesao(data)
                model = MachineLearning()
                ml = model.model
                datas = [z]
                y_pred_train = ml.predict(datas)
                print(y_pred_train)
                print(model.acuracia())
                val5 = ("{}".format(y_pred_train.min()), idSurvey, idStudent)
                mycursor.execute(sql5,val5)
                mydb.commit()
                ###val6 = (model.acuracia(), request.json['IDSURVEY'])
        mycursor.execute(sql2,val2)
        myresult = mycursor.fetchall()
        if myresult[0][0] == 1:
            mycursor.execute(sql3,val3)
            mydb.commit()
            pesquisa_nome(request.json['json_data'],request.json['IDSURVEY'],request.json['IDSTUDENT'])
            return jsonify({}), 202
        else:
            mycursor.execute(sql,val)
            mydb.commit()
            pesquisa_nome(request.json['json_data'],request.json['IDSURVEY'],request.json['IDSTUDENT'])
            return jsonify({}), 201

    except Exception as error:
        print(error.args)
        return jsonify({}), 500


@app.route('/student/<id_student>/survey', methods=['GET'])
def list_suverystudents(id_student):
    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )
    mycursor = mydb.cursor()
    sql = "SELECT surveystudents.IDSURVEY, NAME, surveystudents.JSON_DATA  FROM surveystudents, survey WHERE IDSTUDENT = %s and survey.IDSURVEY=surveystudents.IDSURVEY"
    try:
        mycursor.execute(sql, [id_student])
        myresult = mycursor.fetchall()
        payload = []
        for result in myresult:
            content = {'id': result[0], 'name': result[1], 'survey': result[2]}
            payload.append(content)

        return jsonify(payload), 200

    except Exception as error:
        print(error.args)
        return jsonify({}), 500


@app.route('/student', methods=['POST'])
def add_student():

    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO student (email, password,name,id_institution) VALUES (%s, %s, %s,%s)"

    val = (request.json['email'], request.json['password'], request.json['name'],request.json['id_institution'])

    val2 = (request.json['email'], request.json['password'])

    sql2 = "SELECT count(*) FROM student WHERE email = %s and password = %s"
    try:
        mycursor.execute(sql2, val2)
        myresult = mycursor.fetchall()
        if myresult[0][0] == 0:
            mycursor.execute(sql,val)
            mydb.commit()
            return jsonify({}), 201
        elif myresult[0][0] >= 1:
            return jsonify({}), 400

    except Exception as error:
        print(error.args)
        return jsonify({}), 500


@app.route('/student-login', methods=['POST'])
def login_student():

    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )

    mycursor = mydb.cursor()
    val = (request.json['email'], request.json['password'])
    sql = "SELECT count(*) FROM student WHERE email = %s and password = %s"
    sql2 = "SELECT IDSTUDENT as id, NAME as name, EMAIL as email FROM student WHERE EMAIL = %s"
    val2=[request.json['email']]
    try:
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if myresult[0][0] == 0:
            return jsonify({}), 400
        elif myresult[0][0] >= 1:
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sql2, val2)
            myresult2 = mycursor.fetchall()
            return jsonify(myresult2[0]), 200

    except Exception as error:
        print(error.args)
        return jsonify({}), 500


@app.route('/institution/<id>/student', methods=['GET'])
def list_student(id):
    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )
    mycursor = mydb.cursor()
    sql = "SELECT IDSTUDENT as id, NAME as name, EMAIL as email FROM student WHERE ID_INSTITUTION = %s"
    try:
        mycursor.execute(sql, [id])
        myresult = mycursor.fetchall()
        payload = []
        for result in myresult:
            content = {'id': result[0], 'name': result[1], 'email': result[2]}
            payload.append(content)
        if myresult[0][0] == 0:
            return jsonify({}), 400
        elif myresult[0][0] >= 1:
            return jsonify(payload), 200

    except Exception as error:
        print(error.args)
        return jsonify({}), 500


@app.route('/institution', methods=['POST'])
def add_institution():

    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO institution (email, password,name) VALUES (%s, %s, %s)"

    val = (request.json['email'], request.json['password'], request.json['name'])

    val2 = (request.json['email'], request.json['password'])

    sql2 = "SELECT count(*) FROM institution WHERE email = %s and password = %s"
    try:
        mycursor.execute(sql2, val2)
        myresult = mycursor.fetchall()
        if myresult[0][0] == 0:
            mycursor.execute(sql, val)
            mydb.commit()
            return jsonify({}), 201
        elif myresult[0][0] >= 1:
            return jsonify({}), 400

    except Exception as error:
        print(error.args)
        return jsonify({}), 500


@app.route('/institution-login', methods=['POST'])
def login_institution():

    mydb = mysql.connector.connect(
        host=f'{Env.host}',
        user=f'{Env.user}',
        password=f'{Env.password}',
        database=f'{Env.database}'
    )

    mycursor = mydb.cursor()
    val = (request.json['email'], request.json['password'])
    sql = "SELECT count(*) FROM institution WHERE email = %s and password = %s"
    sql2 = "SELECT IDINSTITUTION as id, NAME as name , EMAIL as email FROM institution WHERE EMAIL = %s"
    val2 = [request.json['email']]
    try:
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if myresult[0][0] == 0:
            return  jsonify({}), 400
        elif myresult[0][0] >= 1:
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sql2, val2)
            myresult2 = mycursor.fetchall()
            return jsonify(myresult2[0]), 200

    except Exception as error:
        print(error.args)
        return jsonify({}), 500



if __name__ == '__main__' or __name__ != '__main__':
    created = Database()
    created.create()
    app.run()

