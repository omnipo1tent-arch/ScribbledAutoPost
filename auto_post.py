import requests
import time

def get_proposal():
    return """

感谢这个有你的世界。
	
你出现的那么突然，朦胧的你，潮汐般的你。
	
我很喜欢海馆里的这段话
「无论时光荏苒，无论荆棘几度，无论你的颜姿，将化作何形，我都将与你相迎，纵沧海桑田，我必归矣，所以，请你，等着我，这具支离破碎的躯壳，再一次，回归于里。」
	
我突然觉得爱是没有要求的，你以什么样的姿态靠近我，我就爱着什么样的你。你变成什么样，我都有自信说我爱你。你让我走进了你的心，甚至允许了我有伤害你的权利。
我不要求你怎么样，因为你仅仅存在就让人如此欢喜。
	
明明知道你自己一个人也可以却还是忍不住把你当小孩心疼，哪怕是小事我都觉得很心疼，我好想为你做点什么。
虽然我也不是多坚强的人但却还是想分担你的情绪。
你问我喜欢你哪一点我每次都说你怎么样都很喜欢…
但果然还是应该仔细想想告诉你，喜欢你唱歌给我听，喜欢你的细腻，喜欢你的敏感，喜欢你不厌其烦地询问我，喜欢你和我讲各种各样的话，喜欢你害羞的脸。
（远不止这些哦）
即使你不这样，我也好喜欢你。
见面的时候你总问我看你干嘛，我就说看看嘛，其实我好爱你。
喜欢对着你笑，也是因为我好喜欢你。
	
你比我勇敢，能先表达对我的爱，又能袒露自己的脆弱，如果我是坏人怎么办呢。
也许是因为这样我才不轻易说出口我的情绪，哪怕你对我很好我还是不能安心，我才是最害怕被伤害的那个人。
	
但现在我不害怕了，我想着你，默念着你，就能生出好多好多勇气。
	
想和你在一起，什么都不做也好。
我爱你这件事，每每想到都有点想哭。
    """

def send_one():
    final_message = get_proposal()
    chunk_size = 2500
    chunks = [final_message[i:i+chunk_size] for i in range(0, len(final_message), chunk_size)]
    
    for chunk in chunks:
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
        except Exception as e:
            print("Error:", e)
        
        time.sleep(1)

# 连续发送 10 次，每次间隔 5 秒
for i in range(1, 11):
    print(f"\n=== 第 {i} 次轰炸 ===")
    send_one()
    print("✅ 发送完成！")
    if i < 10:
        time.sleep(5)

print("\n💍 10 条求婚已送达！Andreas P 无处可逃！")
