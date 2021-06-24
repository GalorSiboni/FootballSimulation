import random
from abc import ABC, abstractmethod

class Human(ABC):
    
    @abstractmethod
    def getName(self):
        pass
    
    @abstractmethod    
    def getAge(self):
        pass

class Person(Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # overriding abstract method
    def getName(self):
        return self.name

    # overriding abstract method
    def getAge(self):
        return self.age
    

class Player(Person):

    def __init__(self, name = "", age = 0, pos = "", goalRate = 0):
        super().__init__(name, age)
        self.pos = pos
        self.goalRate = 0
        self.setGoalRate(goalRate)
        self.goalScored = 0

    def getPos(self):
        return self.pos

    def setGoalRate(self, goalRate):
        if goalRate >= 0 and goalRate < 100:
            self.goalRate = goalRate
        else:
            raise(Exception("Invalid Goal Rate"))

    def getGoalRate(self):
        return self.goalRate

    def kickBall(self):
        return random.randint(self.goalRate, 100)


class GoalKeeper(Player):
    def __init__(self, name, age, goalRate = 0, defRate = 0):
        super().__init__(name, age, "GK", goalRate)
        self.defRate = 0
        self.setDefRate(defRate)

    def setDefRate(self, defRate):
        if defRate >= 0 and defRate < 100:
            self.defRate = defRate
        else:
            raise(Exception("Invalid defense Rate"))

    def getDefRate(self):
        return self.defRate

    def defendeBall(self):
        return random.randint(self.defRate, 100)


class Team:
    players = []
    names = ["Galor", "Siboni", "Shachar", "Nodi", "Zehev", "Niv", "nivik", "Aviv", "Tom", "Nissan", "Shavit", "Sorek", "Messi" , "Ronaldo", "Maradona", "Zlatan"]

    def __init__(self, name):
        self.name = name
        self.shoting_player = Player()

    def getLineUp(self):
        str = self.getTeamName()+": \n"
        for player in self.players:
            str += player.getName() + " " + player.getPos() + "\n"
        print(str)

    def getTeamName(self):
        return self.name

    def setTeam(self):
        self.players = []
        self.players.append(GoalKeeper(self.names[random.randint(0, len(self.names) - 1 - len(self.players))], random.randint(18, 36), random.randint(0, 10), random.randint(57, 90)))
        self.names.remove(self.players[0].getName())
        self.players.append(Player(self.names[random.randint(0, len(self.names) - 1 - len(self.players))], random.randint(18, 36), "CB", random.randint(10, 40)))
        self.names.remove(self.players[1].getName())

        if len(self.players) > 2:
            self.players.append(Player(self.names[random.randint(0, len(self.names) - 1 - len(self.players))], random.randint(18, 36), "CM", random.randint(40, 80)))
            self.names.remove(self.players[2].getName())
            self.players.append(Player(self.names[random.randint(0, len(self.names) - 1 - len(self.players))], random.randint(18, 36), "ST", random.randint(60, 95)))
        else:
            self.players.append(Player(self.names[0], random.randint(18, 36), "CM", random.randint(40, 80)))
            self.names.remove(self.players[2].getName())
            self.players.append(Player(self.names[0], random.randint(18, 36), "ST", random.randint(60, 95)))
        self.names.remove(self.players[3].getName())
        self.getLineUp()

    def defendeBall(self):
        return self.players[0].defendeBall()

    def kickBall(self):
        self.shoting_player = self.players[random.randint(0, 3)]
        return self.shoting_player.kickBall()


class Game:
    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        self.scoreA = 0
        self.scoreB = 0

    def play(self):
        scoreBoard = ""

        while self.scoreA < 5 and self.scoreB < 5:
            if self.teamA.kickBall() > self.teamB.defendeBall():
                self.scoreA += 1
                scoreBoard += self.teamA.shoting_player.getPos()+ " " + self.teamA.shoting_player.getName() + " " + str(self.scoreA) + ":" + str(self.scoreB) + "\n"
                self.teamA.shoting_player.goalScored += 1
                if self.scoreA == 5:
                    break
            if self.teamB.kickBall() > self.teamA.defendeBall():
                self.scoreB += 1
                scoreBoard += "\t\t " + str(self.scoreA) + ":" + str(self.scoreB) + " " + self.teamB.shoting_player.getPos() + " " + self.teamB.shoting_player.getName() + "\n"
                self.teamB.shoting_player.goalScored += 1

        final_scoreBoard = self.teamA.getTeamName() + " " + str(self.scoreA) + " : " + str(self.scoreB) + " " + self.teamB.getTeamName() + "\n" + scoreBoard
        print(final_scoreBoard)
    def getVictorious(self):
        if self.scoreA > self.scoreB:
            return self.teamA
        return self.teamB

class Tournament:
    def __init__(self,teams):
        self.teams = teams
    def letTheGamesBegin(self):
        team1 = self.teams[random.randint(0, 3)]
        teams.remove(team1)
        team2 = self.teams[random.randint(0, 2)]
        teams.remove(team2)
        team3 = self.teams[random.randint(0, 1)]
        teams.remove(team3)
        team4 = self.teams[0]
        teams.append(team1)
        teams.append(team2)
        teams.append(team3)
        Game1 = Game(team1 , team2)
        print("*****************First Semi Final Game*****************\n")
        Game1.play()
        Game2 = Game(team3 , team4)
        print("*****************Second Semi Final Game****************\n")
        Game2.play()
        FinalGame = Game(Game1.getVictorious(), Game2.getVictorious())
        print("***********************Final Game***********************\n")
        FinalGame.play()
    def getTopScorer(self):
        topScorer = 0
        tempPlayer = Player()
        for team in teams:
            for player in team.players:
                if player.goalScored > topScorer:
                    tempPlayer = player
                    topScorer = player.goalScored
        print("***********The Top Scorer Of The Tournament***********\n")
        print("       ",tempPlayer.getName(),"Has Scored",tempPlayer.goalScored,"Goals")



teamA = Team("Galor Siboni")
teamB = Team("Shachar Nissan")
teamC = Team("Zeav Shavit")
teamD = Team("Nadav Halevy")
teams = [teamA, teamB, teamC, teamD]
for i in teams:
    i.setTeam()
tourni = Tournament(teams)
tourni.letTheGamesBegin()
tourni.getTopScorer()
