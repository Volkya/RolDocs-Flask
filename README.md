This is my first CRUD using Flask from Python

Im not use an ORM, this create query in the database.

#Stack

| Language | Backend | Fronted | Database | Platform | Author |
| -------- | -------- |--------|--------|--------|--------|
| Python 3.8 | Flask | Jinga2 | MySQL | Machine | Volkya |

# Init database

`docker run --name wordsApp -d -p 3319:3306 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=wordsApp mariadb`
