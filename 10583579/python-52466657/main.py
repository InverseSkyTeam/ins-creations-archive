from functools import reduce
import pygame

pygame.init()
pygame.display.set_caption("Tupper's self referential formula")
screen = pygame.display.set_mode((1280,720))

def Tuppers_Self_Referential_Formula():
    k = 4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300
    # k = 211349867467970855799412332199742853901876369115226871761118110007277662019229085785695350304797918244395561989957829456443077743544588012318077591618459522972418041923064114623775168829135014645230156246415448583032980130253292699648
    def fn(x, y):
        d = ((-17 * x) - (y % 17))
        e = reduce(lambda x, y: x * y, [2 for x in range(-d)]) if d else 1
        g = ((y // 17) // e) % 2
        return 0.5 < g

    screen.fill((255,255,255))
    pos_x,pos_y = 100,200 # 绘制的初始位置
    for y in range(k + 16, k - 1, -1):
        pos_x = 100
        for x in range(0, 107):
            if fn(x, y):
                pygame.draw.rect(screen,(0,0,0),((pos_x,pos_y),(10,10)))
                pygame.display.update()
            pos_x += 10
        pos_y += 10

if __name__ == '__main__':
    Tuppers_Self_Referential_Formula()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()

# 生成k值的懒得写了，可以用`tuppers-formula.ovh`里的
# 虽然似乎他做的显示也比我好
# 注：公式里的`⌊ ⌋`并不是`[]`，是楼层符号！！！