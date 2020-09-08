from flask import Flask, jsonify, request
import mysql.connector
from Environ import Env
from Databases import Database

app = Flask(__name__)
app.url_map.strict_slashes = False

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

    val2 =  (request.json['email'], request.json['password'])

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
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        if myresult[0][0] == 0:
            return  jsonify({}), 400
        elif myresult[0][0] >= 1:
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sql2,val2)
            myresult2 = mycursor.fetchall()
            return jsonify(myresult2[0]), 200


    except Exception as error:
        print(error.args)
        return jsonify({}), 500


@app.route('/institution/<id>/student',methods=['GET'])
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
        mycursor.execute(sql,[id])
        myresult = mycursor.fetchall()
        payload = []
        content = {}
        for result in myresult:
            content = {'id': result[0], 'name': result[1], 'email': result[2]}
            payload.append(content)
            content = {}
        if myresult[0][0] == 0:
            return  jsonify({}), 400
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

    val2 =  (request.json['email'], request.json['password'])

    sql2 = "SELECT count(*) FROM institution WHERE email = %s and password = %s"
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
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        if myresult[0][0] == 0:
            return  jsonify({}), 400
        elif myresult[0][0] >= 1:
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sql2,val2)
            myresult2 = mycursor.fetchall()
            return jsonify(myresult2[0]), 200

    except Exception as error:
        print(error.args)
        return jsonify({}), 500



if __name__ == '__main__':
    created = Database()
    created.create()
    app.run()