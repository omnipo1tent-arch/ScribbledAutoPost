import requests
import time
from datetime import datetime

url = "https://scribbledthought.com/myDb.php"

def send_post(content):
    files = {
        'action': (None, 'add_message'),
        'message': (None, content),
        'content': (None, content),
        'color': (None, '#FFFF88'),
        'recipient': (None, 'ai'),
        'to': (None, 'ai'),
    }
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Origin': 'https://scribbledthought.com',
        'Referer': 'https://scribbledthought.com/',
    }
    try:
        r = requests.post(url, files=files, headers=headers, timeout=10)
        print("状态:", r.status_code)
        return r.status_code == 200
    except:
        return False

print("开始发帖...")
for i in range(3):
    msg = "Auto post " + str(i+1) + " at " + datetime.now().strftime('%H:%M:%S')
    print("发送:", msg)
    if send_post(msg):
        print("成功!")
    else:
        print("失败!")
    if i < 2:
        time.sleep(3)
print("完成!")