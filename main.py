import requests

TOKEN = "360729900:nkuhQxqh3Xt0fLqgo-9ABBbxWBbgi8yobsE"  # اینجا توکن بله رو بذار

url = f"https://tapi.bale.ai/bot{TOKEN}/getMe"

try:
    r = requests.get(url, timeout=10)
    print("Status Code:", r.status_code)
    print("Response:", r.text)
except Exception as e:
    print("Error:", e)
