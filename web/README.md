# 인증서 생성 방법
openssl genrsa -out CA.key 2048
openssl req -x509 -new -nodes -key CA.key -days 3650 -out CA.pem
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -in server.csr -CA CA.pem -CAkey CA.key -CAcreateserial -out server.crt -days 3650
