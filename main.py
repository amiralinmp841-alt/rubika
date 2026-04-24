import requests
import time

TOKEN = "360729900:nkuhQxqh3Xt0fLqgo-9ABBbxWBbgi8yobsE"  # ← توکن ربات بله‌ات را اینجا بگذار
BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}/"


def get_updates(offset=None, timeout=20):
    url = BASE_URL + "getUpdates"
    params = {
        "timeout": timeout,
    }
    if offset is not None:
        params["offset"] = offset
    try:
        resp = requests.get(url, params=params, timeout=timeout + 5)
        data = resp.json()
        return data.get("result", [])
    except Exception as e:
        print("get_updates error:", e)
        return []


def send_message(chat_id, text):
    url = BASE_URL + "sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    try:
        resp = requests.post(url, json=payload, timeout=10)
        if resp.status_code != 200:
            print("send_message failed:", resp.status_code, resp.text)
    except Exception as e:
        print("send_message error:", e)


def handle_text(text: str) -> str:
    t = text.strip().lower()

    if t in ["سلام", "salam", "hi", "hello"]:
        return "سلام 👋"
    if "چطوری" in t or "چطوري" in t:
        return "خوبم، تو چطوری؟"
    if "خوبی" in t or "خوبي" in t:
        return "مرسی، خوبم 😊"

    return "من یک ربات تست ساده‌ام. منو امیرعلی((@amiralinmp)) ساختههههههه!. بگو «سلام» یا «چطوری» 🙂"


def main():
    print("Bale test bot started...")
    last_update_id = None

    while True:
        updates = get_updates(offset=last_update_id, timeout=20)
        for upd in updates:
            # update_id
            update_id = upd.get("update_id")
            if update_id is not None:
                last_update_id = update_id + 1

            message = upd.get("message")
            if not message:
                continue

            chat = message.get("chat", {})
            chat_id = chat.get("id")
            text = message.get("text")

            if chat_id is None or text is None:
                continue

            print(f"Received from {chat_id}: {text}")
            reply = handle_text(text)
            send_message(chat_id, reply)

        # برای اینکه لوپ دیوانه‌وار سریع نچرخد
        time.sleep(1)


if __name__ == "__main__":
    main()
