import json
import time
from threading import Thread
import urllib.request
import urllib.error
from app import app

def run_server():
    app.run(host="127.0.0.1", port=5001, debug=False)

def test_endpoints():
    server_thread = Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(1)

    base_url = "http://127.0.0.1:5001"

    print("=" * 60)
    print("STEP 1: Testing GET /books (List all books)")
    print("=" * 60)
    req = urllib.request.Request(f"{base_url}/books", method="GET")
    with urllib.request.urlopen(req) as resp:
        print(f"Status Code: {resp.status}")
        data = json.loads(resp.read().decode("utf-8"))
        print("Response JSON:")
        print(json.dumps(data, indent=2))

    print("\n" + "=" * 60)
    print("STEP 2: Testing POST /books (Add a new book - Success)")
    print("=" * 60)
    payload = {
        "title": "Designing Data-Intensive Applications",
        "author": "Martin Kleppmann",
        "year": 2017
    }
    req = urllib.request.Request(
        f"{base_url}/books",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        print(f"Status Code: {resp.status}")
        data = json.loads(resp.read().decode("utf-8"))
        print("Response JSON:")
        print(json.dumps(data, indent=2))

    print("\n" + "=" * 60)
    print("STEP 3: Testing POST /books (Validation Failure - Missing author)")
    print("=" * 60)
    invalid_payload = {
        "title": "Incomplete Book Record"
    }
    req = urllib.request.Request(
        f"{base_url}/books",
        data=json.dumps(invalid_payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(f"Status Code: {e.code}")
        data = json.loads(e.read().decode("utf-8"))
        print("Response JSON:")
        print(json.dumps(data, indent=2))

    print("\n" + "=" * 60)
    print("STEP 4: Testing GET /books (Verifying persistence after insertion)")
    print("=" * 60)
    req = urllib.request.Request(f"{base_url}/books", method="GET")
    with urllib.request.urlopen(req) as resp:
        print(f"Status Code: {resp.status}")
        data = json.loads(resp.read().decode("utf-8"))
        print(f"Total books: {data['total']}")
        print("Response JSON:")
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    test_endpoints()
