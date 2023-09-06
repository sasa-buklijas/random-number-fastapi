
import random
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/random-number")
async def rng(min: int, max: int):
    min_n = min
    max_n = max 

    if min_n > max_n:
        raise HTTPException(status_code=400, detail=f'{min=} is larger than {max=}')

    number = random.randint(min_n, max_n)
    return {'lowerLimit': min_n, 'higherLimit': max_n, 'number': number}

