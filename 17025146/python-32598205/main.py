import requests
import base64
import json
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import hashlib

def upload(repo,file,path,msg,token,owner):
	pt = file
	with open(pt,"rb") as f:
		ct = base64.b64encode(f.read())
	data = {
		"access_token":token,
		"owner":owner,
		"repo":repo,
		"path":pt,
		"content":str(ct)[2:-1],
		"message":msg
	}
	status = requests.post('https://gitee.com/api/v5/repo' + owner + '/{}/contents/{}'.format(repo,path),data = data)
	if "#<V5::Entities::Contents::CommitContent:" not in str(status.text):
		return json.loads(status.text)['content']['download_url']
	else:
		return "该文件已存在"

def addnewrepo(token,name,intro = "",is_private = False):
	data = {
		"access_token":token,
		"name":name,
		"description":intro,
		"private":is_private,
		"auto_init":True
	}
	status = requests.post("https://gitee.com/api/v5/user/repos",data = data)

def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(text,key):
	key = add_to_16(key)
	
	mode = AES.MODE_ECB
	text = add_to_16(text)
	cryptos = AES.new(key, mode)

	cipher_text = cryptos.encrypt(text)
	return b2a_hex(cipher_text)

def decrypt(text,key):
	key = add_to_16(key)

	mode = AES.MODE_ECB
	cryptor = AES.new(key, mode)
	plain_text = cryptor.decrypt(a2b_hex(text))
	return bytes.decode(plain_text).rstrip('\0')


def encryptfile(file,key):
	with open(file,"rb") as f:
		a = f.read()
	x = base64.b64encode(a)
	hashz = encrypt(str(x),key)
	return str(hashz)[2:-1]

def decryptfile(word,key):
	word = eval("b'" + word + "'")
	hashz = eval(decrypt(word,key))
	x = base64.b64decode(hashz)
	return x

def addnewdisk(diskname):
	addnewrepo(diskname + "-public",is_private=False)
	addnewrepo(diskname + "-private",is_private=True)

def upsource(diskname,file,pwd):
	x = upload(diskname + "-private",file,"XesAPI4.txt","123")
	name = encrypt(file.split("/")[-1],pwd)
	with open(f"./{name}.txt","w",encoding = "utf-8") as file:
		file.write(str(encrypt(x,pwd)))
	upload(diskname + "-public","./password.txt","password.txt","123")
	

def setrepopwd(reponm,pwd):
	with open(f"./password.txt","w",encoding = "utf-8") as f:
		f.write(hashlib.sha256(str(encrypt(pwd,pwd)).encode('utf-8')).hexdigest())
	upload(diskname + "-public",f"{name}.txt",f"{name}.txt","123")