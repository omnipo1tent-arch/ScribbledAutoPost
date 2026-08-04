import requests
import time
from datetime import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder

def read_message():
    try:
        with open('message.txt', 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return "文件是空的"
            return content
    except Exception as e:
        print("读取文件失败:", e)
        return "无法读取文件"

def send_post(content):
    url = "https://scribbledthought.com/myDb.php"
    
    encoder = MultipartEncoder(
        fields={
            'action': 'add_message',
            'message': content,
            'content': content,
            'color': '#FFFF88',
            'recipient': 'ai',
            'to': 'ai',
        }
    )
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Origin': 'https://scribbledthought.com',
        'Referer': 'https://scribbledthought.com/',
        'Content-Type': encoder.content_type,
    }
    
    try:
        response = requests.post(url, data=encoder, headers=headers, timeout=120)
        print("状态码:", response.status_code)
        print("响应:", response.text[:200])
        return response.status_code == 200
    except Exception as e:
        print("错误:", e)
        return False

print("读取文件...")
content = read_message()
print("文件大小:", len(content), "字符")

for i in range(3):
    print("\n第", i+1, "次发送")
    if send_post(content):
        print("成功!")
    else:
        print("失败!")
    if i < 2:
        time.sleep(3)

print("\n完成!")