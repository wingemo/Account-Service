git clone https://github.com/wingemo/Account-Service.git

cd account-services

mvn clean install

mvn spring-boot:run

 pip install sqlalchemy

python scripts/create_database.py

python scripts/populate_database.py

mvn test
