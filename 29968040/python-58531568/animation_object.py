import time
from renderer import render
import pygame


class BaseObject:
    def __init__(self, data, texture_manager):
        self.data = data
        self.texture_manager = texture_manager

        self.action_index = 0
        self.animation_start_time = 0  # 动画开始播放的时间

        self.use_interpolation = True
        self.del_last_frame = False  # 删除最后一帧

        self.set_action(0)

    def get_action_data(self):
        s, e = list(self.data.action.values())[self.action_index]
        return s, e - self.del_last_frame

    def set_action(self, name):
        if isinstance(name, int):
            self.action_index = name
            self.action_index %= len(self.data.action)
        else:
            self.action_index = list(self.data.action.keys()).index(name)
        self.animation_start_time = time.time()

    def next_action(self):
        self.set_action(self.action_index + 1)

    def can_use_interpolation(self, frame_index, e_frame):
        for track in self.data.track:
            _data = track.data[int(frame_index)]
            if _data[-1] == -1 or _data[-2] == -1:  # 当前帧为隐藏帧或者没有图片
                continue

            # 开启了插值选项
            # 当前帧不是最后一帧
            # 下一帧是显示的
            # 下一帧和这一帧的图片是同一张（暂时取消）
            interpolation = (
                self.use_interpolation and
                int(frame_index) < e_frame - 1 and
                track.data[int(frame_index) + 1][-1] == 0
            )
            #  and track.data[int(frame_index) + 1][-2] == _data[-2]
            if not interpolation:
                return False
        return True

    def render(self, screen, x, y):
        s_frame, e_frame = self.get_action_data()

        offset_frame = (time.time() - self.animation_start_time) / (1 / self.data.fps)  # 距离动画开始时已经过去的帧数

        frame_index = s_frame + offset_frame % (e_frame - s_frame)  # 当前的帧索引

        t = offset_frame % 1  # 获取 offset_frame 的小数部分

        interpolation = self.can_use_interpolation(frame_index, e_frame)
        for track in self.data.track:
            _data = track.data[int(frame_index)]
            if _data[-1] == -1 or _data[-2] == -1:  # 当前帧为隐藏帧或者没有图片
                continue

            if interpolation:
                _data_next = track.data[int(frame_index) + 1]
                _data = _data + (_data_next - _data) * t

            render(
                pygame.surfarray.pixels2d(screen),
                self.texture_manager.data.get_data(),
                self.texture_manager.index.get_data(),
                self.texture_manager.size.get_data(),
                x, y, _data
            )


class Plant(BaseObject):
    def render(self, screen, x=100, y=100):
        super().render(screen, x, y)


class Item(BaseObject):
    def render(self, screen, x=0, y=0):
        super().render(screen, x, y)
