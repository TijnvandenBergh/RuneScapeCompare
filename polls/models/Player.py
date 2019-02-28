class Player:
    def __init__(self, data):
         self.dataParser(data)

    def dataParser(self, data):
        data = str(data, 'utf-8')
        result = [fragment.split(',') for fragment in data.split('\n')]
        self.total_lvl = result[0][1]
        print(self.total_lvl)



