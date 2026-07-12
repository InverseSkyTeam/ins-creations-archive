import webbrowser as w
print('我同学要求的，既然这样我就做福利吧。看了下network，找到了对应的md5.(素材区有直接的exe文件)')
print('UI就后期加吧。')
url = input('请在下面粘贴网址\n(格式: https://www.zxx.edu.cn/tchMaterial/detail?contentType=assets_document&contentId=6e764703-6e5e-4ea3-9462-34652c2678ef&catalogType=tchMaterial&subCatalog=dzjc)\n请输入:')
key = url.split('&')[1]
md5 = key.split('=')[1]
pdf_left = 'https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/'
pdf_right = '.pkg/pdf.pdf'
pdf_url = pdf_left + md5 + pdf_right
print('获取链接:',pdf_url,sep='\n')
w.open('INS_web.zip')
w.open(pdf_url)