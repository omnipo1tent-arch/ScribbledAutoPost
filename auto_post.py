import requests
import time
from datetime import datetime

def read_message():
    """读取 message.txt 文件内容"""
    try:
        with open('message.txt', 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                return content
            else:
                return "文件是空的，这是默认消息"
    except Exception as e:
        print("读取文件失败:", e)
        return "无法读取文件，这是默认消息"

def send_post(content):
    """发送消息到网站"""
    url = "https://scribbledthought.com/myDb.php"
    
    files = {
        'action': (None, 'add_message'),
        'message': (None, content),
        'content': (None, content),
        'color': (None, '#FFFF88'),
        'recipient': (None, 'ai'),
        'to': (None, 'ai'),
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Origin': 'https://scribbledthought.com',
        'Referer': 'https://scribbledthought.com/',
    }
    
    try:
        response = requests.post(url, files=files, headers=headers, timeout=10)
        print("状态码:", response.status_code)
        return response.status_code == 200
    except Exception as e:
        print("错误:", e)
        return False

# 读取文件内容
print("正在读取 message.txt...")
message_content = read_message()
print("文件内容:", message_content)

# 发送3次
print("\n开始发送...")
for i in range(3):
    print(f"\n第 {i+1} 次发送")
    if send_post(message_content):
        print("✅ 发送成功!")
    else:
        print("❌ 发送失败!")
    if i < 2:
        time.sleep(3)

print("\n✅ 完成！")