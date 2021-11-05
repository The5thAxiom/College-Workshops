# API-Development-Workshop
A workshop held back in May, I went through the old code, spruced it up a bit and now will upload it
# Python
- Used flask to create the models and controllers
- http://127.0.0.1:5000/
  - students:[GET] Gives the json list of all students
  - students:[POST] Adds the student to the db 

post request body:
```javascript
{
    "firstName": "",
    "middleName": "",
    "lastName": "",
    "roll": ""
}
```
# DotNet
- ASP.Net Core API
- https://localhost:5001/api/students/
  - getStudent?id=1: returns the json of the student with the id, 1
  - getAllStudents: Gives the json list of all students
