# Unilime test project
```
Test task for Python Developer position
```

## Dependencies
- .env file with variables in root directory
- installed docker and docker-compose

## Sequencing by docker
```bash
1. cd path/to/cloned_repo
2. put .env file to root directory
3. docker-compose --file docker-compose.demo.yml build
4. docker-compose --file docker-compose.demo.yml up
5. docker-compose --file docker-compose.demo.yml exec unilime-test python application/app/scripts/create_db.py
6. docker-compose --file docker-compose.demo.yml exec unilime-test python application/app/scripts/fill_db.py
7. go by bowser or curl to 'http://localhost:5001/products/get_product_review?product_id=1&limit=2&offset=2'
8. curl -X POST 'http://localhost:5001/products/set_review' -H 'Content-Type: application/json' -d '{"product_id":1, "title": "test_title", "review": "Test Review"}
9. do step 7 and compare results
```

## Sequencing by local

### Dependencies
- .env file with variables in root directory
- installed postgresql local
- installed python 3.10 local or installed pyenv with few python versions
- installed pip
- installed pipenv
- created db in postgresql by name from .env["DB_NAME"]
- created postgresql user by name from .env["DB_USER"] and by password from .env["DB_PASSWORD"]
- started postgresql on host:port from .env["DB_SERVER"]
- installed curl

```bash
1. cd path/to/cloned_repo
2. put .env file to root directory
3. pipenv shell
4. pipenv install
5. python application/app/scripts/create_db.py  # creating tables
6. python application/app/scripts/fill_db.py  # filling tables
7. python application/server.py
8. go by bowser or curl to 'http://localhost:5000/products/get_product_review?product_id=1&limit=2&offset=2'
9.curl -X POST 'http://localhost:5000/products/set_review' -H 'Content-Type: application/json' -d '{"product_id":1, "title": "test_title", "review": "Test Review"}
10. do step 8 and compare results
```

For this test project enough just create db
But for another projects need to use Flask-Migrate & Flask-SQLAlchemy
or pure SQLAlchemy & pure Alembic
