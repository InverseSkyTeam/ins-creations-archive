class Screen:
    def __init__(self, size: int, sizey: int):
        self.size = size
        self.sizey = sizey
        self.text = [[" " for i in self.sizey] for j in self.size]
        self.color = [["\033[1;0m" for i in self.sizey] for j in self.size]


    def fill(self, text: list[list[str]], color: list[list[str]]):
        self.text, self.color = text, color