GET http://localhost:5000/users/register
# Content-Type: text/html; charset=utf-8
HTTP 200
[Captures]
csrf_token: xpath "string(//input[@name='_csrf']/@value)"

POST http://localhost:5000/users/process-reg
Content-Type: application/x-www-form-urlencoded
[FormParams]
first_name: Master
last_name: Vasiliy
phone: 1234567890
email: master@mail.ru
password: 1234
confirm: 1234
submit: Send
_csrf: {{csrf_token}}
HTTP 302
Location: /users/register

GET http://localhost:5000/
HTTP 200
