#coding:utf-8
import requests

def ask_question(content):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    
    data = {
        'content': content,
    }
    response = requests.post('https://api.texttools.cn/api/chat/stream', headers=headers, json=data, stream = True)
    response.encoding = "utf-8"
    for i in response.iter_content(decode_unicode=True):
        print(i,end="")
    print()

def main():
    while True:
        question = input("输入你要问的问题（输入exit退出）：")
        if question == "exit":
            break
        ask_question(question)

if __name__ == '__main__':
    main()