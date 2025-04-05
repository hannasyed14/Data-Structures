'''
    Hanna Syed
    Project 1
    command.py
'''

from myclasses import *
from TreeIndex import *


def showteams(league, teamid):
    team = league.findTeam(teamid)
    if team != None:
        print(f"Team ID: {team.id}")
        print(f"City: {team.city}")
        print(f"Name: {team.name}")
        print(f"Owner: {team.ownername}")
        print(f"Coach: {team.coachname}")
        
    else:
        print("Team not found.")
        
def showplayers(league, playerid):
    for team in league.teams:
        player = team.findPlayer(playerid)
        if player is not None: 
            break
    
    if player != None:
        print(f"Player ID: {player.id}")
        print(f"Name: {player.name}")
        print(f"Position: {player.position}")
        print(f"Number: {player.number}")
        print(f"Salary: {player.salary}")
        
    else:
        print("Player not found.")

def showgames(league, gameid):
    game = league.findGame(gameid)
    if game != None:
        print(f"Game ID: {game.id}")
        print(f"Teams: {game.team1.name} vs {game.team2.name}")
        print(f"Where Played: {game.wherePlayed}")
        print(f"When Played: {game.whenPlayed}")
        
    else:
        print("Game not found")

def help():
    print("quit")
    print("add new team")
    print("add new player")
    print("add new games")
    print("play N -- where N is the id number of the game wanted to be played")
    print("show teams")
    print("show players")
    print("show games")
    print("samples -- make sample objects and puts them into the league")
    print("help")

def samples(league):
    team1 = Team(id=1, city="Buffalo", name="Bills", ownername="Rob", coachname="Bob")
    team2 = Team(id=2, city="Chicago", name="Cats", ownername="Tim", coachname="Tom")
    
    league.addTeam(team1)
    league.addTeam(team2)
    
    player1 = Player(id=1, name="John", position="Quarterback", number=10, salary=500000)
    player2 = Player(id=2, name="Jim", position="Linebacker", number=23, salary=600000)
  
    team1.addNewPlayer(player1)
    team2.addNewPlayer(player2)

    sample_game = Game(id=100, team1=team1, team2=team2, wherePlayed="Las Vegas", whenPlayed="03-08-2024",played = True)
    
    league.addGame(sample_game)
    print("Sample teams, players, and game added to the league.")

#Project Two

def make_index(league):
    league.setTeamPointers()
    print("BST index has been built.")

def show_all_players(league):
    full_info = input("Do you want to see full player info? (yes/no): ")
    if full_info.lower() == "yes":
        league.showAllPlayers(full=True)
    else:
        league.showAllPlayers()

def find_player(league):
    partial_name = input("Enter part of the player's name (use '*' as wildcard): ")
    found_players = league.findPlayer(partial_name)
    if found_players:
        print("Found players:")
        for player in found_players:
            print(f"Player ID: {player.id}, Name: {player.name}")
    else:
        print("No players found.")

    

def main():
    league = League()

    while True:
        response = input("Enter a command: ")
        
        if response == "quit":
            break
        
        elif response.startswith("add new "):
            response = response[7:].strip()
            
            if response == "team":
                team = league.makeTeam()
                league.teams.append(team)
                print("Team added to league")
                
            elif response == "player":
                player = league.makePlayer()
                teamid = int(input("The id number of the team to put the player in?"))
                team = league.findTeam(teamid)
                if team is not None:
                    team.addPlayer(player)
                    print("Player has been added")
                else:
                    print("Team id not found")
                
            elif response == "games":
                game = league.makeGame()
                if game is not None:
                    league.addGame(game)
                    print("Game added to league")
                else:
                    print("Team 1 or Team 2 ID not found")


        elif response.startswith("play "):
            game_id = int(response[5:].strip())
            game = league.findGame(game_id)
            if game is not None:
                game.playGame(game_id)
            else:
                print("Game not found.")

        elif response.startswith("show "):
            response = response[5:].strip()
            
            if response == "teams":
                teamid = int(input("Enter the team's id: "))
                showteams(league, teamid)
                    
            if response == "players":
                playerid = int(input("Enter the player's id: "))
                showplayers(league, playerid)
                    
            if response == "games":
                gameid = int(input("Enter the game's id: "))
                showgames(league, gameid)

        elif response == "help":
            help()

        elif response == "samples":
            samples(league)

        #Project two   

        elif response == "make index":
            make_index(league)

        elif response == "show all players":
            show_all_players(league)

        elif response == "find player":
            find_player(league)


        else:
            print("Unknown Command")
            
main()
            
