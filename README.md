# random-number-fastapi
 REST API for random number generation using [FastAPI](https://fastapi.tiangolo.com/).


## Run

`uvicorn main:app --reload`

**Request:**

```
$ http "localhost:8000/random-number?min=10&max=100"
```

**Response:**

```  
HTTP/1.1 200 OK
content-length: 47
content-type: application/json
date: Mon, 04 Sep 2023 15:15:27 GMT
server: uvicorn

{
    "higherLimit": 100,
    "lowerLimit": 10,
    "number": 10
}
```