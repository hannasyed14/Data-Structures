'''
    Hanna Syed
    Project 1
    myclasses.py
'''


def trueID(n):
    if n == id(None):
        return 0
    else:
        return n

class League:
    def __init__(self, city="DefaultCity", name="DefaultName", director="DefaultDirector"):
        self.city = city
        self.name = name
        self.director = director
        self.teams = []
        self.games = []

    def size(self):
        'Returns the number of teams in league'
        return len(self.teams)

    def addTeam(self, aTeam):
        'Adds new team to list'
        assert type(aTeam) is Team,"1st param must be Team object"
        self.teams.append(aTeam)

    def addGame(self, game):
        'Adds a new game to the list of games'
        assert type(game) is Game, "Parameter must be a Game object"
        self.games.append(game)

    def findTeam(self, teamid):
        'Find team in league using ID'
        assert type(teamid) is int,"team id must be an integer"
        for team in self.teams:
            if teamid == team.id:
                return team
        return None
            
    def findGame(self, gameid):
        'Find game in league using ID'
        assert type(gameid) is int,"game id must be an integer"
        for game in self.games:
            if gameid == game.id:
                return game
        return None

    def makeGame(self):
        'Make a new game with two teams in the league'
        id = int(input("Enter the game id number: "))
        team1_id = int(input("Enter the id of Team 1: "))
        team2_id = int(input("Enter the id of Team 2: "))
        
        team1 = self.findTeam(team1_id)
        team2 = self.findTeam(team2_id)
        
        if team1 is not None and team2 is not None:
            wherePlayed = input("Enter where the game will be played: ")
            whenPlayed = input("Enter when the game will be played (format: MM-DD-YYYY): ")
            new_game = Game(id=id, team1=team1, team2=team2, wherePlayed=wherePlayed, whenPlayed=whenPlayed)
            return new_game
        else:
            return None
        
    def makePlayer(self):
        'Make a new player in a team'
        id = int(input("Enter the player id number: "))
        name = input("What is their name?")
        position = input("What role or position do they play? (e.g. quarterback)")
        number = int(input("What is their team number?"))
        salary = float(input("How many dollars is their salary?"))
        return Player(id=id, name=name, position=position, number=number, salary=salary)

    def makeTeam(self):
        'Make a new team in the league'
        id = int(input("Enter the team id number: "))
        city = input("Enter the city for the new team: ")
        name = input("Enter the name for the new team: ")
        ownername = input("Enter the owner's name for the new team: ")
        coachname = input("Enter the coach's name for the new team: ")
        newteam = Team(id=id, city=city, name=name, ownername=ownername, coachname=coachname)
        return newteam

#Project Two
    def setTeamPointers(self):
        for team in self.teams:
            for player in Team.players:
                player.myteam = team

    
    def showAllPlayers(self,full=False):
        'Goes through each Team and inside each Team it goes through the Players and lists and prints out player info'
        for team in self.teams:
            for player in Team.players:
                if full is True:
                    print(f"Team: {team.name}")
                    print(f"Player ID: {trueID(id(player))}")
                    print(f"Name: {player.name}")
                    print(f"Position: {player.position}")
                    print(f"Number: {player.number}")
                    print(f"Salary: {player.salary}")
                    print(f"Team ID: {trueID(id(player.myteam))}")
                else:
                    print(f"Player ID: {trueID(id(player))}, Name: {player.name}, Team ID: {trueID(id(player.myteam))}")
                    

league = League()

class Team:
    def __init__(self, id, city, name, ownername, coachname):
        self.id = id
        self.city = city
        self.name = name
        self.ownername = ownername
        self.coachname = coachname
        self.players = []

    def addNewPlayer(self, player):
        'Add a new player to a team'
        assert type(player) is Player,"1st parameter must be a Player object"
        self.players.append(player)
        
    def move(self, newcity):
        'Change the team city'
        self.city = newcity

    def addPlayer(self, player):
        'Add existing player to a team'
        assert type(player) is Player,"1st parameter must be a Player object"
        self.players.append(player)
        
    def firePlayer(self, playerid):
        'Remove player from a team'
        assert type(playerid) is int,"Player id must be an integer"
        player = self.findPlayer(playerid)
        if player != None:
            self.players.remove(player)
        else:
            print("Player not found in the team")

    def findPlayer(self, playerid):
        'Find player by id'
        assert type(playerid) is int,"Player id must be an integer"
        for player in self.players:
            if playerid == player.id:
                return player
        return None
    
    
  
        
class Player:
    def __init__(self, id, name, position, number, salary):
        self.id = id
        self.name = name
        self.position = position
        self.number = number
        self.salary = salary

    def changePosition(self, newposition):
        'Change players position'
        self.position = new_position

    def changeSalary(self, newsalary):
        'Change players salary'
        assert type(newsalary) is int,"New salary must be an integer"
        assert newsalary > 0, "Salary must be greater than 0"
        self.salary = newsalary

    def payRaise(self, amount):
        'Raise salary of player'
        assert type(amount) is int,"Salary raise amount must be an integer"
        assert amount > 0, "Salary raise amount must be greater than 0"
        self.salary += amount

    


class Game:
    def __init__(self, id, team1, team2, wherePlayed, whenPlayed, played = False):
        self.id = id
        self.team1 = team1
        self.team2 = team2
        self.wherePlayed = wherePlayed
        self.whenPlayed = whenPlayed
        self.played = played
        self.score = [0,0]

    def changeStatus(self):
        'Change status of game (played/not played)'
        return self.played


    def playGame(self, game_id):
        if self.id == game_id:
            if self.played == False:
                team1score = int(input("Enter score for team 1: "))
                team2score = int(input("Enter score for team 2: "))
                self.score = [team1score, team2score]
                self.played = True
                print(self.score)
                
            else:
                print("This game has already been played.")
        else:
            print("Game not found.")






        
                    
        

    
            

                             
        







    

    
