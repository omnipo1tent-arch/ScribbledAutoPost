import requests
import time
from datetime import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder

def read_message():
    try:
        with open('message.txt', 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return "文件是空的，这是默认消息"
            return content
    except Exception as e:
        print("读取文件失败:", e)
        return "无法读取文件，这是默认消息"

def send_post_large(content):
    url = "https://scribbledthought.com/myDb.php"
    
    # 使用 MultipartEncoder 流式上传（支持大文件）
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
        response = requests.post(
            url,
            data=encoder,
            headers=headers,
            timeout=120
        )
        print("状态码:", response.status_code)
        print("响应:", response.text[:200])
        return response.status_code == 200
    except Exception as e:
        print("错误:", e)
        return False

def split_and_send(content, chunk_size=5000):
    """分段发送大文件（如果还是 413）"""
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
    
    if len(chunks) == 1:
        # 文件不大，直接发送
        return send_post_large(content)
    
    print(f"文件较大，分成 {len(chunks)} 段发送")
    success_count = 0
    
    for i, chunk in enumerate(chunks[:3]):  # 最多发3段
        print(f"\n发送第 {i+1}/{len(chunks)} 段")
        if send_post_large(chunk):
            success_count += 1
            print(f"✅ 第 {i+1} 段成功")
        else:
            print(f"❌ 第 {i+1} 段失败")
        if i < len(chunks) - 1 and i < 2:
            time.sleep(2)
    
    print(f"\n成功发送 {success_count} 段")
    return success_count > 0

# 主程序
print("📂 正在读取 message.txt...")
content = read_message()
print(f"📝 文件大小: {len(content)} 字符")

print("\n🚀 开始发送...")

# 尝试发送
for i in range(3):
    print(f"\n第 {i+1} 次完整发送")
    if split_and_send(content):
        print("✅ 发送成功!")
    else:
        print("❌ 发送失败!")
    if i < 2:
        print("⏳ 等待3秒...")
        time.sleep(3)

print("\n✅ 完成！")    
    # 添加 content 字段
    parts.append(f'--{boundary}\r\n')
    parts.append('Content-Disposition: form-data; name="content"\r\n\r\n')
    parts.append(content + '\r\n')
    
    # 添加 color 字段
    parts.append(f'--{boundary}\r\n')
    parts.append('Content-Disposition: form-data; name="color"\r\n\r\n')
    parts.append('#FFFF88\r\n')
    
    # 添加 recipient 字段
    parts.append(f'--{boundary}\r\n')
    parts.append('Content-Disposition: form-data; name="recipient"\r\n\r\n')
    parts.append('ai\r\n')
    
    # 添加 to 字段
    parts.append(f'--{boundary}\r\n')
    parts.append('Content-Disposition: form-data; name="to"\r\n\r\n')
    parts.append('ai\r\n')
    
    # 结束边界
    parts.append(f'--{boundary}--\r\n')
    
    # 组合成完整的请求体
    body = ''.join(parts)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Origin': 'https://scribbledthought.com',
        'Referer': 'https://scribbledthought.com/',
        'Accept': '*/*',
        'Content-Type': f'multipart/form-data; boundary={boundary}',
        'Content-Length': str(len(body.encode('utf-8'))),
    }
    
    try:
        # 使用流式上传
        response = requests.post(
            url, 
            data=body.encode('utf-8'), 
            headers=headers,
            timeout=60  # 增加超时时间
        )
        print("状态码:", response.status_code)
        print("响应:", response.text[:200])
        return response.status_code == 200
    except Exception as e:
        print("错误:", e)
        return False

def send_post_stream(content):
    """使用生成器流式上传（更节省内存）"""
    url = "https://scribbledthought.com/myDb.php"
    
    def generate_multipart():
        boundary = '----WebKitFormBoundary' + ''.join([str(hex(ord(c)))[2:] for c in str(time.time())])
        
        # 生成各个部分
        parts = [
            f'--{boundary}\r\n',
            'Content-Disposition: form-data; name="action"\r\n\r\n',
            'add_message\r\n',
            f'--{boundary}\r\n',
            'Content-Disposition: form-data; name="message"\r\n\r\n',
            content + '\r\n',
            f'--{boundary}\r\n',
            'Content-Disposition: form-data; name="content"\r\n\r\n',
            content + '\r\n',
            f'--{boundary}\r\n',
            'Content-Disposition: form-data; name="color"\r\n\r\n',
            '#FFFF88\r\n',
            f'--{boundary}\r\n',
            'Content-Disposition: form-data; name="recipient"\r\n\r\n',
            'ai\r\n',
            f'--{boundary}\r\n',
            'Content-Disposition: form-data; name="to"\r\n\r\n',
            'ai\r\n',
            f'--{boundary}--\r\n',
        ]
        
        for part in parts:
            yield part.encode('utf-8')
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Origin': 'https://scribbledthought.com',
        'Referer': 'https://scribbledthought.com/',
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data; boundary=' + '----WebKitFormBoundary' + ''.join([str(hex(ord(c)))[2:] for c in str(time.time())]),
    }
    
    try:
        response = requests.post(
            url,
            data=generate_multipart(),
            headers=headers,
            timeout=60
        )
        print("状态码:", response.status_code)
        print("响应:", response.text[:200])
        return response.status_code == 200
    except Exception as e:
        print("错误:", e)
        return False

# 主程序
print("📂 正在读取 message.txt...")
content = read_message()
print(f"📝 文件大小: {len(content)} 字符")
print(f"📝 文件内容预览: {content[:100]}...")

print("\n🚀 开始发送...")

# 使用流式上传
for i in range(3):
    print(f"\n第 {i+1} 次发送")
    if send_post_chunked(content):
        print("✅ 发送成功!")
    else:
        print("❌ 发送失败!")
    if i < 2:
        print("⏳ 等待3秒...")
        time.sleep(3)

print("\n✅ 完成3次发送！")
