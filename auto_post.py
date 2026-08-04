import requests
import time
from datetime import datetime

def post_message():
    """发送消息到网站"""
    
    url = "https://scribbledthought.com/myDb.php"
    
    # 直接在这里写你要发送的内容
    content = "Hello! This is an automated message from GitHub Actions."
    
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
        'Accept': '*/*',
        'DNT': '1',
    }
    
    try:
        response = requests.post(url, files=files, headers=headers, timeout=30)
        print(f"状态码: {response.status_code}")
        print(f"响应: {response.text[:200]}")
        
        if response.status_code == 200:
            print(f"✅ 发送成功: {content}")
            return True
        else:
            print(f"❌ 发送失败")
            return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def post_three_times():
    """发送3次"""
    for i in range(3):
        print(f"\n第 {i+1} 次发送")
        success = post_message()
        
        if success:
            print(f"✅ 第 {i+1} 次发送成功")
        else:
            print(f"❌ 第 {i+1} 次发送失败")
        
        if i < 2:
            print("等待3秒...")
            time.sleep(3)
    
    print("\n✅ 完成3次发送！")

if __name__ == "__main__":
    print("🚀 开始自动发帖...")
    post_three_times()
    print("🎉 程序执行完毕！")            return True
        else:
            print(f"❌ 发送失败")
            return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def post_three_times():
    """发送3次"""
    for i in range(3):
        print(f"\n第 {i+1} 次发送")
        success = post_message()
        
        if success:
            print(f"✅ 第 {i+1} 次发送成功")
        else:
            print(f"❌ 第 {i+1} 次发送失败")
        
        if i < 2:
            print("等待3秒...")
            time.sleep(3)
    
    print("\n✅ 完成3次发送！")

if __name__ == "__main__":
    print("🚀 开始自动发帖...")
    post_three_times()
    print("🎉 程序执行完毕！")        'Accept': '*/*',
        'DNT': '1',
    }
    
    try:
        response = requests.post(url, files=files, headers=headers, timeout=30)
        print(f"状态码: {response.status_code}")
        print(f"响应: {response.text[:200]}")
        
        if response.status_code == 200:
            print(f"✅ 发送成功: {content[:50]}...")
            return True
        else:
            print(f"❌ 发送失败")
            return False
    except Exception as e:
        print(f"❌ 请求错误: {e}")
        return False

def post_three_times():
    """发送3次，每次清除cookie（通过新建session）"""
    
    # 文件路径
    file_path = r"C:\Users\Administrator\Downloads\message.txt"
    
    print(f"📂 读取文件: {file_path}")
    content = read_message_from_file(file_path)
    print(f"📝 消息内容: {content[:100]}...")
    
    for i in range(3):
        print(f"\n{'='*40}")
        print(f"第 {i+1} 次发送")
        print(f"{'='*40}")
        
        # 每次稍作修改避免重复
        if i > 0:
            modified_content = f"{content} [{i+1}]"
        else:
            modified_content = content
        
        success = post_to_scribbled(modified_content, color="#FFFF88", recipient="ai", to="ai")
        
        if success:
            print(f"✅ 第 {i+1} 次发送成功")
        else:
            print(f"❌ 第 {i+1} 次发送失败")
        
        # 等待3秒再发下一次
        if i < 2:
            print("⏳ 等待3秒...")
            time.sleep(3)
    
    print("\n✅ 完成3次发送！")

if __name__ == "__main__":
    print("🚀 开始自动发帖...")
    post_three_times()
    print("🎉 程序执行完毕！")
