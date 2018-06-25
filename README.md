# Neighbors 

> Application for adding peoples and searching neighbors

## About

For search is used extension PostGIS for Postgresql.
Based on the framework Falcon, sqlalchemy, geoalchemy2, marshmallow for validate request and response parameters and alembic for database migrations.

## Usage
```
Run application on 8000 port:
    docker-compose up --build

Run tests:
    cd /tests
    docker-compose up --build
```

## Api
```
Add user:
    coord_x - latitude
    coord_y - longitude

    POST  http://127.0.0.1:8000/user
    body: {
        "name": "Marcus Aurelius",
        "coord_x": "41.903013", 
        "coord_y": "12.467022"
    }

    
    curl http://127.0.0.1:8000/user -XPOST -d '{"name": "Marcus Aurelius", "coord_x": "41.903013", "coord_y": "12.467022"}'
```

```
Find neighbors:
    GET  http://127.0.0.1:8000/neighbors/61.465245,33.670114?limit=100
```
