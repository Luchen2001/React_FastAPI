import subprocess
import sys

def main():
    fastapi_server = subprocess.Popen(["uvicorn", "fastapi_server:app", "--reload"])
    mastodon_stream = subprocess.Popen([sys.executable, "mastodon_stream.py"])

    try:
        fastapi_server.wait()
        mastodon_stream.wait()
    except KeyboardInterrupt:
        fastapi_server.terminate()
        mastodon_stream.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()
