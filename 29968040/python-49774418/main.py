import pygame
from random import randint
from time import time
from algs import algorithmsDict
import display as display

# Declared in display.py
# 1. global variables : numBars, delay, do_sorting, paused, timer_space_bar
# 2. widgets : sizeBox, delayBox, algorithmBox, playButton, stopButton


def main():
    numbers = []
    running = True
    # print(list(algorithmsDict.keys()))
    algorithmsDictChinese = {
        '插入排序': 'insertion', 
        '冒泡排序': 'bubble',
        '选择排序': 'selection',
        '归并排序': 'merge',
        '快速排序': 'quick',
        '计数排序': 'counting',
        '双向冒泡排序': 'cocktail',
        '循环排序': 'cycle',
        '随机排序': 'bogo',
        '堆排序': 'heap',
        '基数排序': 'radix',
        '希尔排序': 'shell',
        '侏儒排序': 'gnome',
        '梳排序': 'comb',
        '双调排序': 'bitonic',
        '煎饼排序': 'pancake',
        '二分插入排序': 'binary insertion',
        '桶排序': 'bucket',
        'Tim排序': 'tim',
        '臭皮匠排序': 'stooge',
        '链排序': 'strand',
        '奇偶排序': 'odd-even',
        '鸽巢排序': 'pigeonhole',
        '交换排序': 'exchange',
        '树形排序': 'tree'
    }
    display.algorithmBox.add_options(list(algorithmsDictChinese.keys()))

    alg_iterator = None

    timer_delay = time()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and display.do_sorting:
                display.paused = not display.paused
                display.timer_space_bar = time()

            display.updateWidgets(event)

        display.delay = (display.delayBox.value-display.delayBox.rect.x-6)/1000 # delay is in ms

        if display.playButton.isActive: # play button clicked
            display.playButton.isActive = False
            display.do_sorting = True
            current_alg = display.algorithmBox.get_active_option()
            current_alg = algorithmsDictChinese[current_alg]
            display.numBars = int(display.sizeBox.text)
            numbers = [randint(10, 400) for i in range(display.numBars)] # random list to be sorted
            alg_iterator = algorithmsDict[current_alg](numbers, 0, display.numBars-1) # initialize iterator

        if display.stopButton.isActive: # stop button clicked
            display.stopButton.isActive = False
            display.do_sorting = False
            display.paused = False
            try: # deplete generator to display sorted numbers
                while True:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
            except StopIteration:
                pass

        if display.do_sorting and not display.paused: # sorting animation
            try:
                if time()-timer_delay >= display.delay:
                    numbers, redBar1, redBar2, blueBar1, blueBar2 = next(alg_iterator)
                    display.drawInterface(numbers, redBar1, redBar2, blueBar1, blueBar2)
                    timer_delay = time()
            except StopIteration:
                display.do_sorting = False
        elif display.do_sorting and display.paused: # animation paused
            display.drawInterface(numbers, -1, -1, -1, -1)
        else: # no animation
            a_set = set(range(display.numBars))
            display.drawInterface(numbers, -1, -1, -1, -1, greenRows=a_set)


if __name__ == '__main__':
    main()
