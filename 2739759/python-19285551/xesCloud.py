import jieba
# import cv2

def xesWord(txt):
    words = jieba.cut(txt)
    newtxt = " ".join(words)
    return newtxt
'''
def addBg(bgImgName,logoImgName,newImgName): # 三个参数为背景图、
    img = cv2.imread(bgImgName)
    logo = cv2.imread(logoImgName)
    #cv2.imshow("Img_Original", img)
    logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    rows, cols, channels = logo.shape
    roi = img[0:rows, 0:cols]
    # binary & mask
    ret, mask = cv2.threshold(logo_gray, 250, 255, cv2.THRESH_BINARY)
    # dst
    dst = roi
    for r in range(rows):
        for c in range(cols):
            if mask[r, c] == 0:
                dst[r, c, :] = logo[r, c, :]
    # add the dst to the img
    img_merge = img[0:rows, 0:cols] = dst
    cv2.imwrite(newImgName, img_merge)
'''
    # #cv2.imshow("Color Logo", logo)
    # #cv2.imshow("Gray Logo", logo_gray)
    # #cv2.imshow("Mask", mask)
    # #cv2.imshow("Dst", dst)
    # #cv2.imshow("Img", img)
    # #cv2.waitKey(0)
    # cv2.destroyAllWindows()