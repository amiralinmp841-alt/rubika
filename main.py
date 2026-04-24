import socket
import requests

HOST = "messengerapi.ir"
PORT = 443

print("=== PHASE 1: DNS RESOLUTION TEST ===")
try:
    ip = socket.gethostbyname(HOST)
    print(f"DNS OK → {HOST} resolved to {ip}")
except Exception as e:
    print(f"DNS FAILED ❌ → {e}")

print("\n=== PHASE 2: RAW TCP CONNECTION TEST ===")
try:
    sock = socket.create_connection((HOST, PORT), timeout=8)
    print(f"TCP OK → able to connect to {HOST}:{PORT}")
    sock.close()
except Exception as e:
    print(f"TCP FAILED ❌ → {e}")

print("\n=== PHASE 3: HTTPS API TEST ===")
try:
    url = "https://messengerapi.ir/api/v3/getUserInfo"
    payload = {"username": "rubika"}

    r = requests.post(url, json=payload, timeout=8)
    print("HTTPS OK → status:", r.status_code)
    print("Response:", r.text[:300])
except Exception as e:
    print(f"HTTPS FAILED ❌ → {e}")
