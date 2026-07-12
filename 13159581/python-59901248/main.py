import requests
response = requests.get("https://livefile.xesimg.com/programme/python_assets/d3d3394521fc5688eaf744241d6154d3.py",headers={"User-Agent":"1145141919810"},stream=True)
with open('downloaded_file.txt', 'wb') as file:
    aaa = 0
    for chunk in response.iter_content(chunk_size=1024):
        file.write(chunk)
        aaa+=1
        print(str(aaa)+"KB")