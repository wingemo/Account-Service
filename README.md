git clone https://github.com/ditt-anvandarnamn/account-services.git

cd account-services

mvn clean install

mvn spring-boot:run

python scripts/create_database.py

python scripts/populate_database.py

mvn test
