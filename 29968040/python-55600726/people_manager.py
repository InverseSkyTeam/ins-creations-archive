from people import People
from xes_api import CloudVariable
import time
import threading as thr


class PeopleManager:
    def __init__(self, message, project):
        self.exit = False
        self.max_players = 4
        self.my_player = 0
        self.control = None
        self.peoples = []
        self.cloud_variable = CloudVariable(self.max_players, project)
        self.message = message

        # self.cloud_variable.init_cloud()

    def init(self):
        self.setup()
        self.join()
        if self.my_player > 0:
            pass
        else:
            raise Exception('人数已满')
        tt = thr.Thread(target=self.begin, args=(), name="T1")
        tt.setDaemon(True)
        tt.start()

    def setup(self):
        player = 1
        for i in range(self.max_players):
            self.peoples.append(People(player))
            player += 1

    def join(self):
        ws = self.cloud_variable

        ws.open()
        variable = ws.get_variable_all()
        ws.close()

        for people in self.peoples:
            if f'P{people.player}_c' in variable:
                people.last_value = variable[f'P{people.player}_c']
        time.sleep(3)

        ws.open()
        variable = ws.get_variable_all()
        ws.close()

        for people in self.peoples:
            if people.last_value == variable[f'P{people.player}_c']:
                print('当前玩家:', people.player)
                self.my_player = people.player
                break

    def begin(self):
        ws = self.cloud_variable

        ws.open()
        ws.send_variable(self.my_player, self.control.get_cloud_data())
        ws.close()

        while not self.exit:
            if self.my_player > 0:
                try:
                    total_players = 1
                    ws.open()
                    variable = ws.get_variable()
                    self.control.set_hp(variable[f'P{self.my_player}_b'])
                    if self.control.spwan:
                        self.control.start_spwan()
                    ws.send_variable(self.my_player, self.control.get_cloud_data())
                    
                    for people in self.peoples:
                        if people.player == self.my_player:
                            people.is_show = False
                        else:
                            people.set_cloud_data(variable[f'P{people.player}_a'],
                                                  variable[f'P{people.player}_b'])
                            if people.last_value == variable[f'P{people.player}_c']:
                                people.offline += 1
                                if people.offline == 5:
                                    people.is_show = False
                                    self.message.add_message(f'{people.get_name()}退出游戏')
                            else:
                                people.last_value = variable[f'P{people.player}_c']
                                if people.offline > 4:
                                    people.is_show = True
                                    self.message.add_message(f'{people.get_name()}进入游戏')
                                people.offline = 0
                            total_players += int(people.is_show)
                            if people.send_hp:
                                people.hp = max(people.hp - self.control.get_attack_hp(), 0)
                                ws.send_variable_hp(people.player, people.get_cloud_data())
                                people.send_hp = False
                    ws.close()
                    self.control.total_players = total_players
                except Exception as eeee:
                    print(eeee)
