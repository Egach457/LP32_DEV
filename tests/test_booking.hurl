GET http://127.0.0.1:5000
Content-Type: application/json

HTTP 200

POST http://127.0.0.1:5000/users/process-reg
Content-Type: application/json
{
  "first_name": "Master",
  "last_name": "Vasiliy",
  "phone": 1234567890,
  "email": "master@mail.ru",
  "password": 1234,
  "confirm": 1234
}
HTTP 302
Location: http://127.0.0.1:5000/users/register
POST http://127.0.0.1:5000/users/register
HTTP 200



POST http://127.0.0.1:5000/users/apartmens

{
  "user_id": 5,
  "country": "Belarus",
  "city": "Minsk",
  "address": "Kolasa 1",
  "title": "My apartment",
  "description": "My apartment in Minsk",
  "payment_type": "cash",
  "rent_type": "monthly",
  "image_path": "sdfasdfoasdnfasdf",
  "apartment_id": 4,
  "wi_fi": true,
  "hair_dryer": true,
  "towels": true,
  "balcony": false,
  "air_conditioner": false,
  "tv": true,
  "apartmens_id": 4,
  "floor": 5,
  "apartment_number": 20,
  "number_of_beds": 3,
  "number_of_guests": 2,
  "room_area": 20,
  "no_children": false,
  "no_parties": true,
  "no_smoking": false,
  "no_pets": false
}

[FormParams]
"user_id": 5,
"country": "Belarus",
"city": "Minsk",
"address": "Kolasa 1",
"title": "My apartment",
"description": "My apartment in Minsk",
"payment_type": "cash",
"rent_type": "monthly",
"image_path": "sdfasdfoasdnfasdf",
"apartment_id": 4,
"wi_fi": true,
"hair_dryer": true,
"towels": true,
"balcony": false,
"air_conditioner": false,
"tv": true,
"apartmens_id": 4,
"floor": 5,
"apartment_number": 20,
"number_of_beds": 3,
"number_of_guests": 2,
"room_area": 20,
"no_children": false,
"no_parties": true,
"no_smoking": false
"no_pets": false

HTTP 200
