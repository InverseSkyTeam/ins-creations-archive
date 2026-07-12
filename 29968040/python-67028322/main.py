import pygame 
import sys
from INS_Transition import State, TransitionGroup, TransitionData, ease

# 颜色常量（模拟 CSS 变量）
THEME_COLOR = pygame.Color(112, 192, 0)           # --theme-color
THEME_COLOR_ACTIVE = pygame.Color(97, 166, 0)     # --theme-color-active
TRACK_OFF = pygame.Color(215, 215, 215)           # #d7d7d7
TRACK_OFF_ACTIVE = pygame.Color(200, 200, 200)    # #c8c8c8
TRACK_OFF_DARK = pygame.Color(68, 68, 68)         # #444
TRACK_OFF_ACTIVE_DARK = pygame.Color(85, 85, 85)  # #555

def color_lerp(t, color1: pygame.Color, color2: pygame.Color):
    """颜色插值函数，用于过渡"""
    return color1.lerp(color2, t)

class Switch:
    def __init__(self, center):
        self.center = center
        self.dark = False
        self.checked = False
        self.active = False

        # 轨道尺寸（36x20，滑块16x16，边距2px）
        self.track_width = 36
        self.track_height = 20
        self.slider_size = 16
        self.margin = 2
        self.scale = 4

        # 滑块过渡
        self.slider_left_start = self.margin
        self.slider_left_end = self.track_width - self.slider_size - self.margin
        
        self.slider_left = self.slider_left_start
        default_slider_state = State.create(
            slider_left=(self.slider_left_start, TransitionData('0.25s', ease))
        )
        checked_slider_state = State.create(
            slider_left=(self.slider_left_end, TransitionData('0.25s', ease))
        )
        self.slider_transition = TransitionGroup(
            self, default_slider_state,
            checked=checked_slider_state
        )
        
        # 轨道颜色过渡
        self.track_color = TRACK_OFF  # 初始颜色
        default_state = State.create(
            track_color=(TRACK_OFF, TransitionData('0.25s', ease))
        )
        dark_default_state = State.create(
            track_color=(TRACK_OFF_DARK, TransitionData('0.25s', ease))
        )
        default_active_state = State.create(
            track_color=(TRACK_OFF_ACTIVE, TransitionData('0.25s', ease))
        )
        dark_default_active_state = State.create(
            track_color=(TRACK_OFF_ACTIVE_DARK, TransitionData('0.25s', ease))
        )
        checked_state = State.create(
            track_color=(THEME_COLOR, TransitionData('0.25s', ease))
        )
        checked_active_state = State.create(
            track_color=(THEME_COLOR_ACTIVE, TransitionData('0.25s', ease))
        )
        self.track_transition = TransitionGroup(
            self, default_state,
            lerp_funcs={'track_color': color_lerp},
            dark_default=dark_default_state,
            default_active=default_active_state,
            dark_default_active=dark_default_active_state,
            checked=checked_state,
            checked_active=checked_active_state
        )

    def _get_tracked_state_name(self):
        """获取轨道状态字符串"""
        if self.checked:
            return 'checked' + self.active * '_active'
        return self.dark * 'dark_' + 'default' + self.active * '_active'

    def _get_slider_state_name(self):
        """获取滑块状态字符串"""
        return 'checked' if self.checked else 'default'
    
    def get_rect(self):
        rect = pygame.Rect(0, 0, self.track_width, self.track_height)
        rect.center = self.center
        return rect.scale_by(self.scale)

    def handle_event(self, event):
        rect = self.get_rect()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rect.collidepoint(event.pos):
                self.active = True
                
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.active:
            self.checked = not self.checked
            self.active = False

        elif event.type == pygame.MOUSEMOTION and self.active:
            # 如果按下后移出开关，清除 active 并恢复颜色
            if not rect.collidepoint(event.pos):
                self.active = False

    def update(self):
        self.slider_transition.set_state(self._get_slider_state_name())
        self.track_transition.set_state(self._get_tracked_state_name())
        self.slider_transition.update()
        self.track_transition.update()

    def render(self, surface):
        # 轨道
        track_rect = self.get_rect()
        pygame.draw.rect(surface, self.track_color, track_rect, border_radius=10 * self.scale)

        # 滑块
        slider_x = track_rect.x + self.slider_left * self.scale
        slider_y = track_rect.y + self.margin * self.scale
        slider_size = self.slider_size * self.scale
        
        slider_center_pos = int(slider_x + slider_size/2), int(slider_y + slider_size/2)
        pygame.draw.circle(screen, (255, 255, 255), slider_center_pos, slider_size//2)


class UI:
    DEFAULT = pygame.Color(255, 255, 255)
    DARK = pygame.Color(40, 40, 40)
    def __init__(self):
        self.dark = False
        self.bg_color = UI.DEFAULT
        
        default_state = State.create(
            bg_color=(UI.DEFAULT, TransitionData('0.25s', ease))
        )
        dark_state = State.create(
            bg_color=(UI.DARK, TransitionData('0.25s', ease))
        )
        self.transition = TransitionGroup(
            self, default_state,
            lerp_funcs={'bg_color': color_lerp},
            dark=dark_state
        )
        
        self.switch = Switch((400, 200))
        self.switch_dark = Switch((400, 400))
    
    def update(self):
        self.dark = self.switch.dark = self.switch_dark.dark = self.switch_dark.checked
        self.transition.set_state('dark' if self.dark else 'default')
        self.switch.update()
        self.switch_dark.update()
        self.transition.update()
    
    def handle_event(self, event):
        self.switch.handle_event(event)
        self.switch_dark.handle_event(event)
    
    def render(self, surface):
        surface.fill(self.bg_color)
        self.switch.render(screen)
        self.switch_dark.render(screen)


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
ui = UI()

# 主循环
while True:
    fps = str(round(clock.get_fps()))
    pygame.display.set_caption(f'Switch Demo - FPS: {fps}')
    
    events = pygame.event.get()
    for _event in events:
        if _event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ui.handle_event(_event)
    
    ui.update()
    ui.render(screen)
    
    pygame.display.flip()
    clock.tick(60)