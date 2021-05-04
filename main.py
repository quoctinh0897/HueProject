from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
async def read_item( message: str = ''):
    if message:
        return {"data" : compress(message)}


def compress(string):
    if string is None or not string:
        return string
    result = ''
    prev_char = string[0]
    count = 0
    for char in string:
        if char == prev_char:
            count += 1
        else:
            result += _calc_partial_result(prev_char, count)
            prev_char = char
            count = 1
    result += _calc_partial_result(prev_char, count)
    return result if len(result) < len(string) else string

def _calc_partial_result(prev_char, count):
    return prev_char + (str(count) if count > 1 else '')
