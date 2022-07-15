# Unilime test project
```
Test task for Python Developer position
```

## Dependencies
- .env file with variables in root directory
- installed docker and docker-compose

## Sequencing
```bash
1. cd path/to/cloned_repo
2. put .env file to root directory
3. docker-compose --file docker-compose.demo.yml build
4. docker-compose --file docker-compose.demo.yml up
5. docker-compose --file docker-compose.demo.yml exec unilime-test python application/app/scripts/create_db.py
6. docker-compose --file docker-compose.demo.yml exec unilime-test python application/app/scripts/fill_db.py
7. go by bowser or curl to 'http://localhost:5001/products/get_product_review?product_id=1'
8. curl -X POST 'http://localhost:5001/products/set_review' -H 'Content-Type: application/json' -d '{"product_id":1, "title": "test_title", "review": "Test Review"}
9. do step 7 and compare results
```

For this test project enough just create db
But for another projects need to use Flask-Migrate & Flask-SQLAlchemy
or pure SQLAlchemy & pure Alembic
