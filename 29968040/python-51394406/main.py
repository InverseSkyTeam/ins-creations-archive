# 广告：鸿蒙图标库
# https://developer.huawei.com/consumer/cn/design/harmonyos-icon/

import pygame
import sys
from tools import *

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("[IOI2023] 机器人比赛")
clock = pygame.time.Clock()
font_title = pygame.font.SysFont("SimHei", 25)

import ui
Buttons = ui.Buttons()
TestCases = ui.TestCases()
XiangXiXinXi = ui.XiangXiXinXi(1)
CommandArea = ui.CommandArea()
EditArea = ui.EditArea()
screen_cache = None
close_edit = False

while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_pos = pygame.mouse.get_pos()
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if CommandArea.show_edit and EditArea.close_rect.collidepoint(mouse_pos):
                    CommandArea.show_edit = False
                    close_edit = True
                if not CommandArea.show_edit and TestCases.zh_rect.collidepoint(mouse_pos):
                    ui.command.load_file('正正解.py')
                    ui.command.parse_command()
    if close_edit:
        if not pygame.mouse.get_pressed()[0]:
            close_edit = False
        mouse_pressed = 0
        mouse_pos = [-10, -10]
        pygame_events = []
    if not CommandArea.show_edit:
        screen.fill((239, 239, 239))
        render_linear_gradient_rect(screen, (35, 37, 38), (65, 67, 69), pygame.Rect(0, 0, 700, 50))
        screen.blit(font_title.render('[IOI2023] 机器人比赛', True, (255,)*3), (25, 12))
        pygame.draw.rect(screen, (255,)*3, (10, 60, 450, 30), border_radius=4)
        pygame.draw.rect(screen, (255,)*3, (470, 60, 220, 430), border_radius=4)
        pygame.draw.rect(screen, (255,)*3, (10, 100, 450, 390), border_radius=4)
        Buttons.display(screen, mouse_pressed, mouse_pos)
        screen.blit(TestCases.zh_sf, TestCases.zh_rect)
        if Buttons.focus == 0:
            ti_num = TestCases.display(screen, pygame_events, mouse_pos, mouse_pressed)
            if ti_num:
                XiangXiXinXi.set_num(ti_num)
                Buttons.set_focus(1)
        else:
            XiangXiXinXi.render(screen, pygame_events, mouse_pos, mouse_pressed)
        CommandArea.render(screen, pygame_events, mouse_pos, mouse_pressed)
        if CommandArea.show_edit:
            draw_alpha_rect(screen, (0, 0, 0, 100), (23, 73, 700-40-6, 500-90-6))
            screen_cache = screen.copy()
            EditArea.set_command(CommandArea.commands, CommandArea.edit_command)
    else:
        screen.blit(screen_cache, (0, 0))
        pygame.draw.rect(screen, (255,)*3, (25, 75, 700-50, 500-100), border_radius=3)
        EditArea.render(screen, mouse_pos, mouse_pressed)
        if mouse_pressed and EditArea.save_rect.collidepoint(mouse_pos):
            a, b, c, d, e, Z, A = EditArea.command
            a += 2
            b += 2
            c += 2
            d += 2
            e += 2
            if CommandArea.edit_command != 'new' and EditArea.command[:5] == CommandArea.commands[CommandArea.edit_command][:5]:
                CommandArea.command_class.tp[a][b][c][d][e][0] = Z
                CommandArea.command_class.tp[a][b][c][d][e][1] = ord(A)
                CommandArea.commands[CommandArea.edit_command] = EditArea.command
                CommandArea.show_edit = False
                close_edit = True
            elif CommandArea.command_class.tp[a][b][c][d][e][1]:
                print('已经有这条指令了！')
            else:
                CommandArea.command_class.tp[a][b][c][d][e][0] = Z
                CommandArea.command_class.tp[a][b][c][d][e][1] = ord(A)
                CommandArea.show_edit = False
                close_edit = True
                if CommandArea.edit_command == 'new':
                    CommandArea.commands.append(EditArea.command)
                else:
                    _a, _b, _c, _d, _e, _Z, _A = CommandArea.commands[CommandArea.edit_command]
                    _a += 2
                    _b += 2
                    _c += 2
                    _d += 2
                    _e += 2
                    CommandArea.command_class.tp[_a][_b][_c][_d][_e][:] = 0
                    CommandArea.commands[CommandArea.edit_command] = EditArea.command
        if mouse_pressed and EditArea.del_rect.collidepoint(mouse_pos):
            if CommandArea.edit_command != 'new':
                _a, _b, _c, _d, _e, _Z, _A = CommandArea.commands[CommandArea.edit_command]
                _a += 2
                _b += 2
                _c += 2
                _d += 2
                _e += 2
                CommandArea.command_class.tp[_a][_b][_c][_d][_e][:] = 0
                del CommandArea.commands[CommandArea.edit_command]
            CommandArea.show_edit = False
            close_edit = True
    pygame.display.update()
    clock.tick(114514)
