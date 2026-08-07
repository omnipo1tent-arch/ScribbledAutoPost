import requests
import time
from pathlib import Path

URL = "https://scribbledthought.com/myDb.php"


def get_message():
    return Path("message.txt").read_text(encoding="utf-8")


def send_one():

    final_message = get_message()

    files = {
        "color": (None, "#FFFF88"),
        "recipient": (None, "test"),
        "message": (None, final_message),
        "to": (None, "test"),
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://scribbledthought.com",
        "Referer": "https://scribbledthought.com/",
    }

    try:
        r = requests.post(
            URL,
            files=files,
            headers=headers,
            timeout=120
        )

        print("Status:", r.status_code)
        print("Response:", r.text)

    except Exception as e:
        print("Error:", e)



if __name__ == "__main__":

    for i in range(20):
        print(f"Sending {i+1}/20")

        send_one()

        time.sleep(2)
