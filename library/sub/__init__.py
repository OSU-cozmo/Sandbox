from ..robot import getCurrentBot;

class sub:

    bot = -1;

    def __init__(self):
        self.bot = getCurrentBot();
        print(self.bot);

    def getX(self):
        return self.bot.getX();
