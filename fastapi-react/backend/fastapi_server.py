from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://172.26.132.211:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def root():
    return {'example': 'this is an example', 'data': 0}

mastodon = {"username": "", "content": '', "url": ""}
@app.get('/mastodon')
async def get_mastodon():
    return mastodon

@app.post('/update_mastodon')
async def update_mastodon(data: dict = Body(...)):
    global mastodon
    mastodon = data
