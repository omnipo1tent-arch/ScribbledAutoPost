import requests
import time

def get_proposal():
    return """

C’est l’été, les journées ont ton visage, les pierres ta tiédeur
Et la vie avec toi, l’hiver brûlera, il fera chaud en novembre, tu es ma chaleur, l’été perpétuel, mon amour inépuisable.
Je t'aime d'une façon déraisonnable,
et c'est la seule qui vaille.
je veux coucher avec toi
Je déteste la distance l'ombre la douleur la pluie Je veux des jours ensoleillés avec toi près de la mer et du sable Je veux encierre le fantastique le pays que j'aime mais avec toi
🥺


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
