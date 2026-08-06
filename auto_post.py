import requests
import time
from pathlib import Path

URL = "https://scribbledthought.com/myDb.php"

def get_proposal():
    return Path("message.txt").read_text(encoding="utf-8")

def send_one():
    final_message = get_proposal()

    files = {
        "color": (None, "#FFFF88"),
        "recipient": (None, "test"),   # 改成你需要的对象
        "message": (None, final_message),
        "to": (None, "test"),          # 改成你需要的对象
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0",
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
        print("Sent bytes:", len(final_message.encode("utf-8")))

    except Exception as e:
        print(e)

if __name__ == "__main__":
    send_one()
