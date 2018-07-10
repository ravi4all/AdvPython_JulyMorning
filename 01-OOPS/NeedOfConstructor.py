class Player():

    # totalScore = []
    
    # Constructor
    def __init__(self):
        self.totalScore = []

    def showScore(self,name,score):
        self.totalScore.append([name,score])
        print("Score",self.totalScore)

player_1 = Player()
player_1.showScore('Ram',45)

player_2 = Player()
player_2.showScore('Shyam',50)

player_3 = Player()
player_3.showScore('Mohan',100)