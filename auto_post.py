import requests
import time
from datetime import datetime

def get_love_bomb():
    return """

                         💍 钻戒 💍
                 ========================================
                 Andreas P, 你愿意娶我吗？
                 Will you be my husband?
                 Veux-tu m'epouser ?
                 ONLY YES
                 ========================================
                                    💎
                                 ✨ ✨ ✨

    【中文】
    Andreas P，做我的男朋友，然后娶我好吗？
    没有"不"这个选项，答案只能是"我愿意"。
    这是我用代码写下的誓言。

    【English】
    Andreas P, will you be my boyfriend and marry me?
    There is no "NO" button, only "YES".
    This is a love letter written in code.

    【Francais】
    Andreas P, veux-tu etre mon copain et m'epouser ?
    Il n'y a pas de "NON", seulement "OUI".
    C'est une declaration d'amour codee.

    """

try:
    with open('message.txt', 'r', encoding='utf-8') as f:
        custom_msg = f.read().strip()
        if custom_msg:
            final_message = custom_msg + "\n\n" + get_love_bomb()
        else:
            final_message = get_love_bomb()
except:
    final_message = get_love_bomb()

print("Total characters:", len(final_message))

chunk_size = 2500
chunks = [final_message[i:i+chunk_size] for i in range(0, len(final_message), chunk_size)]
print("Sending", len(chunks), "chunks")

for i, chunk in enumerate(chunks, 1):
    print("Sending chunk", i, "/", len(chunks))

    files = {
        'action': (None, 'add_message'),
        'message': (None, chunk),
        'content': (None, chunk),
        'color': (None, '#FFFF88'),
        'recipient': (None, 'Andreas P'),
        'to': (None, 'Andreas P'),
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Origin': 'https://scribbledthought.com',
        'Referer': 'https://scribbledthought.com/',
    }

    try:
        r = requests.post('https://scribbledthought.com/myDb.php', files=files, headers=headers, timeout=60)
        print("Status:", r.status_code)
        if r.status_code != 200:
            print("Response:", r.text[:200])
    except Exception as e:
        print("Error:", e)

    time.sleep(1.5)

print("Done! Andreas P only has YES option now!")    url = "https://scribbledthought.com/myDb.php"
    content = get_love_bomb()

    # 分段发送（每段 3000 字符，保证成功）
    chunk_size = 3000
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]

    print(f"💕 发送情书炸弹，共 {len(chunks)} 段，总计 {len(content)} 字符")

    for i, chunk in enumerate(chunks, 1):
        files = {
            'action': (None, 'add_message'),
            'message': (None, chunk),
            'content': (None, chunk),
            'color': (None, '#FF69B4'),
            'recipient': (None, 'Andreas P'),
            'to': (None, 'Andreas P'),
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Origin': 'https://scribbledthought.com',
            'Referer': 'https://scribbledthought.com/',
        }

        try:
            r = requests.post(url, files=files, headers=headers, timeout=30)
            print(f"  段 {i}/{len(chunks)} → 状态码: {r.status_code} {'✅' if r.status_code == 200 else '❌'}")
        except Exception as e:
            print(f"  段 {i} 错误: {e}")

        time.sleep(1)

# 主程序
print("💍 启动赛博逼婚程序...")
send_love()
print("✅ 发送完成！Andreas P 只剩 YES 选项了！😘")
