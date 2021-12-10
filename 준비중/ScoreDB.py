class ScoreDB:
    def __init__(self):
        self.lst1 = {0, 7, 8, 15}


    def addList(self,n):
        j = self.lst1
        j |= {n}
        print(self.lst1)
        self.lst1 = j


#if row in [0, 7, 8, 15]:
    #return
