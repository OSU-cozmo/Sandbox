global current_bot;

class bot:
    x = 0;
    def __init__(self):
        self.x = 200;
        global current_bot;
        current_bot = self;

    def getX(self):
        print("Returning %d" % self.x)
        return self.x;

def getCurrentBot():
    return current_bot;
