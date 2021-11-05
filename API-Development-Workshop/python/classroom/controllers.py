from classroom import app, db
from flask import jsonify, request
from classroom.models import Student

@app.route('/')
def home():
    return "Hello, World!<br><a href = \"/abc\">abc</a><br><a href = \"/getName\">get name</a>"

@app.route('/abc')
def hola():
    return "<h1>HOLA</h1>hello<br><a href = \"/\">back</a>"

@app.route('/getName')
def getName():
    name = {"firstName": "Samridh", "middleName": "Anand", "lastName": "Paatni"}
    return jsonify(name)

# there will be 2 urls:
#       /students/ => GET and POST
#       /student/<index> => GET, PUT, DELETE

@app.route('/students', methods = ['GET', 'POST'])
def students():
    if request.method == 'GET':
        students = Student.query.all()
        st = []
        for i in students:
            st.append({
                "id": i.id,
                "firstName" : i.firstName,
                "middleName": i.middleName,
                "lastName": i.lastName,
                "roll": i.roll
            })
        return jsonify({
            "status": "success",
            "data": st
        })
    elif request.method == 'POST':
        newStudent = request.get_json()
        newStudent = Student(**newStudent) # is used for passing a dictionary as the parameters for the object
        db.session.add(newStudent)
        db.session.commit()
        return "success"
    else:
        return "ye galt ae"