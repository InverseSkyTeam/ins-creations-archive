import pygame
from tools import *
import checker
import threading as thr
import time

button_font = pygame.font.SysFont('SimHei', 14)
test_case_num_font = pygame.font.SysFont('SimHei', 13)
test_case_font = pygame.font.SysFont('arial', 20)
command_title_font = pygame.font.SysFont('SimHei', 16)
command_font = pygame.font.SysFont('SimHei', 11)
save_font = pygame.font.SysFont('SimHei', 45//2)
command = checker.Command()
command.load_file('robot1.txt')
command.parse_command()


class Button:
    def __init__(self, text, rect):
        self.text = text
        self.rect = rect
        self.state = 0  # 0: 无状态（非选中）  1: 选中  2: 选中 + hover  3: 非选中 + hover
        self.text_sf = button_font.render(text, True, calc_colors((255,)*3, (0, 0, 0, 0.75)))
        self.text_sf_hover = button_font.render(text, True, (0x34, 0x98, 0xdb))
    
    def set_state(self, state):
        self.state = state
    
    def set_hover(self, hover):
        if hover:
            if self.state == 0:
                self.state = 3
            elif self.state == 1:
                self.state = 2
        else:
            if self.state == 3:
                self.state = 0
            elif self.state == 2:
                self.state = 1
    
    def render(self, screen):
        text_sf = self.text_sf_hover if self.state in [1, 2] else self.text_sf
        text_rect = text_sf.get_rect(center=self.rect.center)
        under_line_color = (255,)*3 if not self.state else ((0xbf,)*3 if self.state == 3 else (0x34, 0x98, 0xdb))
        under_line_rect = pygame.Rect(self.rect.x + (8 if self.state == 1 else 0), self.rect.bottom-2, self.rect.w - (16 if self.state == 1 else 0), 2)
        screen.blit(text_sf, text_rect.topleft)
        pygame.draw.rect(screen, under_line_color, under_line_rect, width=0)

    def check_down(self, mouse_pressed, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed:
                self.set_state(2)
                return True
            self.set_hover(True)
            return False
        self.set_hover(False)
        return False


class Buttons:
    def __init__(self):
        self.focus = 0
        self.buttons = [
            Button('测试点信息', pygame.Rect(26,     60, 86+16, 30)), 
            Button('详细信息',   pygame.Rect(26+102, 60, 76+16, 30))
        ]
        self.buttons[self.focus].set_state(1)
    
    def set_focus(self, focus):
        self.focus = focus
        self.buttons[self.focus].set_state(1)
        self.buttons[1-self.focus].set_state(0)
    
    def display(self, screen, mouse_pressed, mouse_pos):
        has_check_botton = False
        for i, button in enumerate(self.buttons):
            if button.check_down(mouse_pressed, mouse_pos):
                self.focus = i
                has_check_botton = True
        for i, button in enumerate(self.buttons):
            if has_check_botton and i != self.focus:
                button.set_state(0)
            button.render(screen)


class TestCase:
    def __init__(self, num):
        self.state = 'Wait'  # AC/WA/Wait
        self.num = num
        self.error = None
        self.time = time.time()
        self.background_color = {
            'Wait': (20, 85, 143), 
            'AC': (82, 196, 26),
            'WA': (231, 76, 60)
        }
        self.animation_sf = pygame.Surface((32*4, 32*4), pygame.SRCALPHA)
        pygame.draw.circle(self.animation_sf, (255,)*3, (32*2, 32*2), 32*2, width=8, 
                           draw_top_right=True, draw_top_left=True, draw_bottom_left=True, draw_bottom_right=False)
        self.animation_sf = pygame.transform.smoothscale(self.animation_sf, (32, 32)).convert_alpha()
        self.num_sf = test_case_num_font.render('#'+str(num), True, (255,)*3)
        self.AC_sf = test_case_font.render("AC", True, (255,)*3)
        self.WA_sf = test_case_font.render("WA", True, (255,)*3)
    
    def render(self, screen, pos):
        pygame.draw.rect(screen, self.background_color[self.state], (pos[0], pos[1], 95, 95))
        screen.blit(self.num_sf, (pos[0] + 6, pos[1] + 6 + (18 - self.num_sf.get_height())//2))
        if self.state == 'Wait':
            new_animation_sf = pygame.transform.rotate(self.animation_sf, (time.time()-self.time)*300)
            sf_w, sf_h = new_animation_sf.get_size()
            screen.blit(new_animation_sf, (pos[0] + (95-sf_w)//2, pos[1] + (95-sf_h)//2))
            return
        elif self.state == 'AC':
            sf_w, sf_h = self.AC_sf.get_size()
            screen.blit(self.AC_sf, (pos[0] + (95-sf_w)//2, pos[1] + (95-sf_h)//2))
            return
        elif self.state == 'WA':
            sf_w, sf_h = self.WA_sf.get_size()
            screen.blit(self.WA_sf, (pos[0] + (95-sf_w)//2, pos[1] + (95-sf_h)//2))
            return
    
    def evaluating(self):
        res = checker.tests[self.num-1].evaluating(command)
        # print(res)
        if res != 'AC':
            self.state = 'WA'
            self.error = res
        else:
            self.state = 'AC'


class TestCases:
    def __init__(self):
        self.test_case = [TestCase(i) for i in range(1, 20+1)]
        self.scroll_y = 0
        self.scroll_max_y = 165
        self.in_rect = None
        self.up_sf = pygame.Surface((56+28, 30), pygame.SRCALPHA)
        self.up_text = button_font.render('提交答案', True, (255,) * 3)
        pygame.draw.rect(self.up_sf, (52, 152, 219), (0, 0, 56+28, 30), border_radius=3)
        self.up_sf.blit(self.up_text, self.up_text.get_rect(center=self.up_sf.get_rect().center))
        self.up_rect = pygame.Rect(300, 11, 56+28, 30)

        self.zh_sf = pygame.Surface((56 + 28, 30), pygame.SRCALPHA)
        self.zh_text = button_font.render('生成正解', True, (255,) * 3)
        pygame.draw.rect(self.zh_sf, (52, 152, 219), (0, 0, 56 + 28, 30), border_radius=3)
        self.zh_sf.blit(self.zh_text, self.zh_text.get_rect(center=self.zh_sf.get_rect().center))
        self.zh_rect = pygame.Rect(600, 11, 56 + 28, 30)

    def display(self, screen, pygame_events, mouse_pos, mouse_pressed):
        screen.blit(self.up_sf, self.up_rect)
        self.in_rect = pygame.Rect(10, 100, 450, 390).collidepoint(mouse_pos)
        self.event(pygame_events, mouse_pos)
        sf = pygame.Surface((410, 390), pygame.SRCALPHA)
        x, y = 0, 20 - self.scroll_y
        error = None
        check_down = 0
        for i, test_case in enumerate(self.test_case):
            if y + 95 > 0 and y < 390:
                test_case.render(sf, (x, y))
                if pygame.Rect(30+x, 100+y, 95, 95).collidepoint(mouse_pos) and self.in_rect:
                    if mouse_pressed:
                        check_down = i + 1
                    else:
                        if test_case.state == 'WA':
                            error = [x+30, y+100, test_case.error]
            x += 10 + 95
            if (i+1) % 4 == 0:
                x = 0
                y += 10 + 95
        screen.blit(sf, (30, 100))
        if error:
            draw_alpha_rect(screen, (51, 51, 51, int(255*0.8)), (error[0]-30, error[1]-15, 155, 25))
            rect_temp = pygame.Rect(error[0]-30, error[1]-15, 155, 25)
            error_sf = button_font.render(error[-1], True, (255,)*3)
            screen.blit(error_sf, error_sf.get_rect(center = rect_temp.center))
        return check_down
    
    def scroll(self, num):
        self.scroll_y += num
        self.scroll_y = min(max(0, self.scroll_y), self.scroll_max_y)
    
    def event(self, pygame_events, mouse_pos):
        for event in pygame_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and self.in_rect:
                    self.scroll(-15)
                elif event.button == 5 and self.in_rect:
                    self.scroll(15)
                elif event.button == 1:
                    if self.up_rect.collidepoint(mouse_pos):
                        self.evaluating()
    
    def _evaluating(self):
        for test_case in self.test_case:
            test_case.evaluating()
    
    def evaluating(self):
        tt = thr.Thread(target=self._evaluating, args=(), name="T1")
        tt.start()


class XiangXiXinXi:
    def __init__(self, num):
        self.num = num
        self.in_rect = None
        self.run = checker.tests[self.num-1].run(command)
        self.X = self.Y = 1
        self.refresh_img = pygame.image.load('重置.png').convert_alpha()
        self.refresh_rect = pygame.Rect(13, 105, self.refresh_img.get_width(), self.refresh_img.get_height())
        self.forward_img = pygame.image.load('前进.png').convert_alpha()
        self.forward_rect = pygame.Rect(13, 135, self.forward_img.get_width(), self.forward_img.get_height())
        self.play_img = pygame.image.load('播放.png').convert_alpha()
        self.stop_img = pygame.image.load('停止.png').convert_alpha()
        self.play_rect = pygame.Rect(13, 165, self.play_img.get_width(), self.play_img.get_height())
        self.play = 0
    
    def set_num(self, num):
        self.num = num
        checker.tests[self.num-1].mp_run = copy.deepcopy(checker.tests[self.num-1].mp_data)
        self.run = checker.tests[self.num-1].run(command)
        self.X = self.Y = 1
        self.play = 0
    
    def render(self, screen, pygame_events, mouse_pos, mouse_pressed):
        self.in_rect = pygame.Rect(10, 100, 450, 390).collidepoint(mouse_pos)
        for event in pygame_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.in_rect:
                    if self.refresh_rect.collidepoint(mouse_pos):
                        self.set_num(self.num)
                    if not self.play and self.forward_rect.collidepoint(mouse_pos):
                        try:
                            lim, self.X, self.Y = next(self.run)
                        except:
                            self.play = 0
                    if self.play_rect.collidepoint(mouse_pos):
                        self.play = not self.play
            if event.type == pygame.KEYDOWN:
                pass
        if self.play:
            try:
                lim, self.X, self.Y = next(self.run)
            except:
                self.play = 0
        checker.tests[self.num-1].render(screen, pygame.Rect(10, 100, 450, 390), self.X, self.Y)
        screen.blit(self.refresh_img, self.refresh_rect)
        screen.blit(self.forward_img, self.forward_rect)
        screen.blit([self.play_img, self.stop_img][self.play], self.play_rect)


class CommandArea:
    def __init__(self):
        self.command_class = command
        self.commands = self.command_class.command
        self.error = None
        self.add_img = pygame.image.load('添加.png').convert_alpha()
        self.add_img_rect = pygame.Rect(656, 70, self.add_img.get_width(), self.add_img.get_height())
        self.edit_img = pygame.transform.smoothscale(pygame.image.load('修改.png'), (16, 16)).convert_alpha()
        self.title_sf = command_title_font.render('指令区', True, calc_colors((255,)*3, (0, 0, 0, 0.75)))
        self.command_ico = pygame.transform.scale(pygame.image.load('指令ico.png'), (16, 17)).convert_alpha()
        self.command_color = calc_colors((255,)*3, (0, 0, 0, 0.75))
        self.scroll_y = 0
        self.in_rect = False
        self.scroll = None  # pygame.Rect(470, 99+220, 5, 0)
        self.scroll_dragging = False
        self.scroll_color_normal = calc_colors((255, 255, 255), (0, 0, 0, 0.25))  # 滚动条颜色
        self.scroll_color_hover = calc_colors((255, 255, 255), (0, 0, 0, 0.4))  # 鼠标悬停颜色
        self.show_edit = False
        self.edit_command = None  # new / commands的索引
    
    def contentScrollLength_scrollbarLength(self, contentScrollLength):
        return contentScrollLength * (386 - self.scroll.height) / (len(self.commands)*37 - 386)

    def scrollbarLength_contentScrollLength(self, scrollbarLength):
        return (len(self.commands)*37 - 386) / (386 - self.scroll.height) * scrollbarLength
        
    def render(self, screen, pygame_events, mouse_pos, mouse_pressed):
        self.in_rect = pygame.Rect(470, 60, 220, 430).collidepoint(mouse_pos)
        for event in pygame_events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.in_rect:
                if event.button == 4 and self.scroll:
                    self.scroll_y -= 15
                    self.scroll_y = max(0, min(len(self.commands) * 37 - 386, self.scroll_y))
                    self.scroll.y = 104 + self.contentScrollLength_scrollbarLength(self.scroll_y)
                elif event.button == 5 and self.scroll:
                    self.scroll_y += 15
                    self.scroll_y = max(0, min(len(self.commands) * 37 - 386, self.scroll_y))
                    self.scroll.y = 104 + self.contentScrollLength_scrollbarLength(self.scroll_y)
                elif event.button == 1:
                    if self.scroll is not None and self.scroll.collidepoint(mouse_pos):
                        self.scroll_dragging = True
                    if not self.scroll_dragging and self.add_img_rect.collidepoint(mouse_pos):
                        self.show_edit = True
                        self.edit_command = 'new'
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.scroll_dragging = False
            if event.type == pygame.MOUSEMOTION and self.scroll_dragging:
                self.scroll.move_ip(0, event.rel[1])
                self.scroll.y = max(104, min(104 + 386 - self.scroll.height, self.scroll.y))
                self.scroll_y = int(self.scrollbarLength_contentScrollLength(self.scroll.y - 104))

        pygame.draw.rect(screen, (187, 222, 251), (470, 60, 220, 44), border_top_left_radius=4, border_top_right_radius=4)
        screen.blit(self.title_sf, (480, 73))
        screen.blit(self.add_img, self.add_img_rect)
        sf = pygame.Surface((220, 386), pygame.SRCALPHA)
        if len(self.commands)*37 > 386:
            self.scroll_y = max(0, min(len(self.commands)*37-386, self.scroll_y))
            if self.scroll is None or self.scroll.h != max((386 / (len(self.commands)*37)) * 386, 10):
                self.scroll = pygame.Rect(690-5, 104, 5, max((386 / (len(self.commands)*37)) * 386, 10))
                self.scroll.y += self.contentScrollLength_scrollbarLength(self.scroll_y)
            pygame.draw.rect(screen, (self.scroll_color_normal, self.scroll_color_hover)[self.scroll_dragging], self.scroll, border_radius=2)
        else:
            self.scroll_y = 0
            self.scroll_dragging = False
            self.scroll = None
        for i in range(max(self.scroll_y//37-1, 0), min(self.scroll_y//37+11, len(self.commands))):
            self.render_one_command(sf, (0, 37*i-self.scroll_y), self.commands[i])
            edit_rect = pygame.Rect(195, 37*i-self.scroll_y+11, 16, 16)
            sf.blit(self.edit_img, edit_rect)
            if not self.scroll_dragging and edit_rect.collidepoint(mouse_pos[0]-470, mouse_pos[1]-104) and mouse_pressed:
                self.show_edit = True
                self.edit_command = i
        screen.blit(sf, (470, 104))
    
    def format_command(self, command):
        return 'S:[{},{},{},{},{}] Z:{} A:{}'.format(*command)
    
    def render_one_command(self, screen, pos, command):
        screen.blit(self.command_ico, (pos[0]+10, pos[1]+10))
        screen.blit(command_font.render(self.format_command(command), True, self.command_color), (pos[0]+30, pos[1]+13))
    
    def clear_command(self):
        self.command_class.command = []
        self.command_class.parse_command()


class EditArea:
    def __init__(self):
        self.text_color = calc_colors((255,)*3, (0, 0, 0, 0.75))
        self.close_img = pygame.image.load('关闭.png')
        self.close_rect = pygame.Rect(700-35-24, 85, self.close_img.get_width(), self.close_img.get_height())

        self.save_img = pygame.Surface((150, 45), pygame.SRCALPHA)
        self.save_text = save_font.render('保存', True, (255,)*3)
        pygame.draw.rect(self.save_img, '#4e6ef2', (0, 0, 150, 45), border_radius=3)
        self.save_img.blit(self.save_text, self.save_text.get_rect(center=self.save_img.get_rect().center))
        self.save_rect = pygame.Rect(150, 403, 150, 45)

        self.del_img = pygame.Surface((150, 45), pygame.SRCALPHA)
        self.del_text = save_font.render('删除', True, '#4e6ef2')
        pygame.draw.rect(self.del_img, (255,)*3, (0, 0, 150, 45), border_radius=3)
        pygame.draw.rect(self.del_img, '#4e6ef2', (0, 0, 150, 45), width=2, border_radius=3)
        self.del_img.blit(self.del_text, self.del_text.get_rect(center=self.save_img.get_rect().center))
        self.del_rect = pygame.Rect(400, 403, 150, 45)

        self.colors = {}
        tmp_size = 40
        tmp_font = pygame.font.SysFont('arial', int(tmp_size//2))
        for color in checker.colors:
            sf = pygame.Surface((tmp_size, tmp_size))
            sf.fill(checker.colors[color])
            if color == -1:
                temp_rect = pygame.Rect(0, 0, tmp_size, tmp_size)
                tl = list(temp_rect.topleft)
                tr = list(temp_rect.topright)
                br = list(temp_rect.bottomright)
                bl = list(temp_rect.bottomleft)
                tr[0] -= 2
                br[0] -= 2
                br[1] -= 2
                bl[1] -= 2
                pygame.draw.line(sf, (255, 0, 0), tl, br, width=2)
                pygame.draw.line(sf, (255, 0, 0), tr, bl, width=2)
            elif color == -2:
                tmp_sf = test_case_num_font.render('边界', True, (230,)*3)
                sf.blit(tmp_sf, tmp_sf.get_rect(center=sf.get_rect().center))
            else:
                tmp_sf = tmp_font.render(str(color), True, (0,)*3)
                sf.blit(tmp_sf, tmp_sf.get_rect(center=sf.get_rect().center))
            pygame.draw.rect(sf, (0,)*3, (0, 0, tmp_size, tmp_size), width=1)
            self.colors[color] = sf
            
        self.rects = pygame.Rect((700-40)//2, 115, 40, 40), \
                     pygame.Rect((700-3*40)//2, 115+40, 40, 40), \
                     pygame.Rect((700-3*40)//2+40, 115+40, 40, 40), \
                     pygame.Rect((700-3*40)//2+80, 115+40, 40, 40), \
                     pygame.Rect((700-40)//2, 115+80, 40, 40)
        self.dpos = 4, 1, 0, 3, 2
        self.focus = 0
        self.command = None
        self.text_sf = command_title_font.render('会把当前格子的颜色改为Z：', True, self.text_color)
        self.sf_text = command_title_font.render('然后执行指令：', True, self.text_color)
        self.fx = {}
        texts = '''H: 停留\nW: 移动到西邻（左边）\nS: 移动到南邻（下方）\nE: 移动到东邻（右边）\nN: 移动到北邻（上方）\nT: 终止程序'''
        for i in texts.split('\n'):
            self.fx[i[0]] = command_title_font.render(i, True, self.text_color)

    @staticmethod
    def format_command_S(command_):
        return '当机器人识别到状态数组S为: [{},{},{},{},{}] 时'.format(*command_[:5])
    
    def render_color_area(self, screen, can_click_negative_color, pos, focus_color, mouse_pressed, mouse_pos):
        x, y = pos
        for i in range(-2, 19+1):
            screen.blit(self.colors[i], (x, y))
            if focus_color == i:
                pygame.draw.rect(screen, (255, 215, 0), (x, y, 40, 40), width=3)
            if mouse_pressed and pygame.Rect(x, y, 40, 40).collidepoint(mouse_pos):
                if not can_click_negative_color and i < 0:
                    print('不可以选择该颜色')
                else:
                    focus_color = i
            x += 40
            if i == 8:
                y += 40
                x = pos[0]
        return focus_color
    
    def set_command(self, commands, command_pos):
        self.command = commands[command_pos] if isinstance(command_pos, int) else [0, 0, 0, 0, 0, 0, 'T']
        self.command = copy.deepcopy(self.command)

    def render_fx(self, screen, focus, pos, mouse_pressed, mouse_pos):
        x, y = pos
        for i in 'HWSENT':
            screen.blit(self.fx[i], (x, y+5))
            if mouse_pressed and pygame.Rect(x-10, y, 180, 26).collidepoint(mouse_pos):
                focus = i
            if focus == i:
                pygame.draw.rect(screen, (255, 215, 0), (x-10, y, 180, 26), width=3)
            y += 26
        return focus
    
    def render(self, screen, mouse_pos, mouse_pressed):
        screen.blit(command_title_font.render(self.format_command_S(self.command), True, self.text_color), (45, 95))
        screen.blit(self.sf_text, (675-self.sf_text.get_width()-190, 127+130))
        screen.blit(self.close_img, self.close_rect)
        screen.blit(self.text_sf, (45, 127+130))
        screen.blit(self.save_img, self.save_rect)
        screen.blit(self.del_img, self.del_rect)
        for i in range(5):
            screen.blit(self.colors[self.command[self.dpos[i]]], self.rects[i])
            if mouse_pressed and self.rects[i].collidepoint(mouse_pos):
                self.focus = i
            if self.focus == i:
                pygame.draw.rect(screen, (255, 215, 0), self.rects[i], width=3)
        screen.blit(self.colors[self.command[5]], (45 + self.text_sf.get_width(), 115+130))
        if mouse_pressed and pygame.Rect(45 + self.text_sf.get_width(), 115+130, 40, 40).collidepoint(mouse_pos):
            self.focus = 5
        if self.focus <= 4:
            self.command[self.dpos[self.focus]] = self.render_color_area(screen, self.focus != 2, (35, 115+130+50), self.command[self.dpos[self.focus]], mouse_pressed, mouse_pos)
        else:
            pygame.draw.rect(screen, (255, 215, 0), pygame.Rect(45 + self.text_sf.get_width(), 115+130, 40, 40), width=3)
            self.command[5] = self.render_color_area(screen, False, (35, 115+130+50), self.command[self.focus], mouse_pressed, mouse_pos)
        self.command[-1] = self.render_fx(screen, self.command[-1], (490, 200), mouse_pressed, mouse_pos)
