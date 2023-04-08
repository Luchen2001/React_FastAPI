import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json

app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

mastodon = {"username": "", "content":'', "url":""}

m = Mastodon(
        api_base_url=f'https://mastodon.world',
        access_token=os.environ['MASTODON_ACCESS_TOKEN']
    )

class Listener(StreamListener):
    def on_update(self, status):
        #print(json.dumps(status, indent=2, sort_keys=True, default=str))
        #print('------------------------------')
        mastodon["username"] = status["account"]["username"]
        mastodon["content"] = status["content"]
        mastodon["url"] = status["url"]


async def start_mastodon_stream():
    while True:
        try:
            await m.stream_public(Listener(), run_async=True)
        except (MastodonNotFoundError, MastodonRatelimitError) as e:
            print(f"Error: {e}")
            await asyncio.sleep(60)  # Wait 60 seconds before retrying


@app.get('/')
async def root():
    return {'example': 'this is an example', 'data': 0}

@app.get('/mastodon')
async def get_mastodon():
    return mastodon

@app.on_event("startup")
async def start_streaming():
    asyncio.create_task(start_mastodon_stream())