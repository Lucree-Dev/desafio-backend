echo "FIRST TEST"

curl -X POST -H "Content-Type: application/json" -d '{
   "first_name":"João",
   "last_name": "das Neves",
   "birthday": "1991-09-91",
   "password": "*****",
   "username": "joao_das_neves",
   "user_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
}' http://localhost:8080/account/person -i


echo "CREATE SESSION"
token=$(curl -X POST -H "Content-Type: application/json" -d '
{
   "password": "Montana",
   "username": "Tony"
}' http://localhost:8080/session -s| jq -r .data)
echo $token


curl -X GET -H "Authorization: Bearer $token" http://localhost:8080/account/friends -s | jq

echo "SECOND TEST"
curl -X POST -H "Authorization: Bearer $token" -d '{
   "card_id": "70c881d4a26984ddce795f6f71817c9cf4480e79",
   "title": "Cartão 1",
   "pan": "5527952393064634",
   "expiry_mm": "03",
   "expiry_yyyy": "2022",
   "security_code": "656",
   "date":"26/11/2015"
}' http://localhost:8080/account/card -i


echo "SECOND TEST"
curl -X GET -H "Authorization: Bearer $token" http://localhost:8080/account/cards -s | jq

echo "THIRD TEST"
curl -X POST -H "Authorization: Bearer $token" -d '{
   "friend_id": "70c881d4a26984ddce795f6f71817c9cf4480e79",
   "total_to_transfer": 100,
   "billing_card": {
      "card_id": "70c881d4a26984ddce795f6f71817c9cf4480e79"
   }
}' http://localhost:8080/account/transfer -i


curl -X GET -H "Authorization: Bearer $token" http://localhost:8080/account/bank-statement -s | jq
