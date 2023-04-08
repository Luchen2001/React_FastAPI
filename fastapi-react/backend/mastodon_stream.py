from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json
import requests

m = Mastodon(
    api_base_url=f'https://mastodon.world',
    access_token=os.environ['MASTODON_ACCESS_TOKEN']
)

class Listener(StreamListener):
    def on_update(self, status):
        mastodon = {
            "username": status["account"]["username"],
            "content": status["content"],
            "url": status["url"]
        }
        print(mastodon)
        requests.post('http://localhost:8000/update_mastodon', json=mastodon)

def start_mastodon_stream():
    while True:
        try:
            m.stream_public(Listener())
        except (MastodonNotFoundError, MastodonRatelimitError) as e:
            print(f"Error: {e}")
            time.sleep(60)  # Wait 60 seconds before retrying

if __name__ == '__main__':
    start_mastodon_stream()
