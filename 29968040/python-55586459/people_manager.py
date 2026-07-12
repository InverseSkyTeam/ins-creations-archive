from people import People
from xes_api import get_variable, send_variable
import time
import threading as thr


class PeopleManager:
    def __init__(self):
        self.exit = False
        self.max_players = 4
        self.my_player = 0
        self.control = None
        self.peoples = []

    def init(self):
        self.setup()
        self.join()
        if self.my_player > 0:
            pass
        else:
            raise Exception('人数已满')
        tt = thr.Thread(target=self.begin, args=(), name="T1")
        tt.start()

    def setup(self):
        player = 1
        for i in range(self.max_players):
            self.peoples.append(People(player))
            player += 1

    def join(self):
        variable = get_variable()
        for people in self.peoples:
            if f'P{people.player}_b' in variable:
                people.last_value = variable[f'P{people.player}_b']
            else:
                people.last_value = '0'
                send_variable(f'P{people.player}_a', '0', f'P{people.player}_b', '0', f'P{people.player}_c', '0')
        time.sleep(3)
        variable = get_variable()
        for people in self.peoples:
            if people.last_value == variable[f'P{people.player}_b']:
                print('当前玩家:', people.player)
                self.my_player = people.player
                break

    def begin(self):
        while not self.exit:
            if self.my_player > 0:
                a, b, c = self.control.get_cloud_data()
                send_variable(f'P{self.my_player}_a', a, f'P{self.my_player}_b', b, f'P{self.my_player}_c', c)

                variable = get_variable()
                for people in self.peoples:
                    if people.player == self.my_player:
                        people.is_show = False
                    else:
                        if people.last_value == variable[f'P{people.player}_b']:
                            people.offline += 1
                            if people.offline == 100:
                                people.is_show = False
                        else:
                            people.last_value = variable[f'P{people.player}_b']
                            if people.offline > 99:
                                people.is_show = True
                            people.offline = 0
                        people.set_cloud_data(variable[f'P{people.player}_a'],
                                              variable[f'P{people.player}_b'],
                                              variable[f'P{people.player}_c'])


