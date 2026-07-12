import random
import image_manager
from anim_manager import NumberAnimation, remove
from rotate_lib import rotate


class MergePic:
    def __init__(self, x, y, img):
        angle = random.random() * 90
        self.source, self.width, self.height = rotate(img, angle)
        self.pointX, self.pointY = x, y
        self.transform = False
        self.rotate = 0

        image_manager.add(self)
    
    def destroy(self):
        image_manager.remove(self)


class MergeAnimal:
    def __init__(self, x, y, merge_img):
        self.id = 'merge'
        self.img = [MergePic(x, y, i) for i in merge_img.data]
        
        self._t = 0
        self.timer = NumberAnimation(self, '_t', 300 / 1000, None, None, self.destroy)
        self.timer.start(_from=0, _to=300)  # 定时器拿动画充当（

    def destroy(self):
        for i in self.img:
            i.destroy()
        remove(self.timer)
