1. 打开你的 GitHub 仓库
2. 点击 auto_post.py
3. 点击 ✏️ 铅笔图标（编辑）
4. **删除所有旧代码**
5. 粘贴下面的新代码
6. 点击 "Commit changes"║    ║  🇨🇳 中文：                                                          ║  ║
║    ║  Andreas P，从我遇见你的那一刻起，我就知道你是那个对的人。          ║  ║
║    ║  今天我用代码向你表白——没有“不”的选项，只有“我愿意”。            ║  ║
║    ║  做我的男朋友，然后娶我。这是用脚本写下的永恒誓言。 💖              ║  ║
║    ║                                                                      ║  ║
║    ║  🇬🇧 English：                                                       ║  ║
║    ║  Andreas P, from the moment I met you, I knew you were the one.    ║  ║
║    ║  Today I confess with code — there is no "NO", only "I DO".        ║  ║
║    ║  Be my boyfriend, then marry me. A love oath written in scripts. 💖 ║  ║
║    ║                                                                      ║  ║
║    ║  🇫🇷 Français：                                                      ║  ║
║    ║  Andreas P, depuis le moment où je t'ai rencontré, j'ai su que    ║  ║
║    ║  tu étais le bon. Aujourd'hui je t'avoue en code — pas de "NON",  ║  ║
║    ║  seulement "OUI". Sois mon copain, puis épouse-moi. Un serment    ║  ║
║    ║  d'amour écrit en scripts. 💖                                      ║  ║
║    ║                                                                      ║  ║
║    ╚══════════════════════════════════════════════════════════════════════╝  ║
║                                                                              ║
║                          💍  💍  💍  💍  💍  💍                            ║
║                                                                              ║
║                    ╔════════════════════════════════════╗                    ║
║                    ║   🤵  Andreas P  👰  你愿意吗？   ║                    ║
║                    ║   🎯  只有 YES，没有 NO！        ║                    ║
║                    ╚════════════════════════════════════╝                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

💍 2026-08-05  💍  发送次数：每 5 分钟一次，直到你说 YES！ 💍
"""

def send_love():
    url = "https://scribbledthought.com/myDb.php"
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
