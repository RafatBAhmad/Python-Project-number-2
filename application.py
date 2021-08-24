import copy
import constants
import sys

players = copy.deepcopy(constants.PLAYERS)
teams   = copy.deepcopy(constants.TEAMS)

Panthers = []
Bandits  = []
Warriors = []
experince_player   = []
unexperince_player = []

def main_app():
    print("--------------------------")
    print("BASKETBALL TEAM STATS TOOL ")
    print("--------------------------\n")
    print("---- MENU----\n")
    print("Here are your choices:\n")
    print("A) Display Team Stats")
    print("B) Quit\n")
    while True:
        option = input("Enter an option[A\B]: ")
        if option.lower() == "b":
            sys.exit("see you later dude (= ") #TODO: add exit text
        elif option.lower() == "a":
            print("\nA) Panthers")
            print("B) Bandits")
            print("C) Warriors\n")
            while True:
                option2 = input("Enter an option[A\B\C] ")
                if option2.lower() == "a":
                    stats(Panthers,"Panthers")
                    break
                elif option2.lower() == "b":
                    stats(Bandits,"Bandits") 
                    break
                elif option2.lower() == "c":
                    stats(Warriors,"Warriors") 
                    break
                else:
                    print("Please enter valid choice!\n")           
            
        else:
            print("Please enter valid choice!\n") 


def clean_data():
    for player in players:
        #height = player['height'].split()
        #height = int(height[0])
        player['height'] = int(player['height'].split()[0])
        experience = player['experience'].split()
        if experience[0] == "YES":
            player['experience'] = True
            experince_player.append(player)
        else:
            player['experience'] = False
            unexperince_player.append(player)
        #guardians = player["guardians"].split("and")
        player["guardians"] = player["guardians"].split("and")    


def balance_teams():
    num_players_team = int(len(players)/len(teams))
    for player in players:
        if len(Panthers) < num_players_team :
            Panthers.append(player)
        elif len(Bandits) < num_players_team:
            Bandits.append(player)
        else:
            Warriors.append(player) 

def stats(team,name_team):
    print("\n")
    print("Team: {} stats".format(name_team))
    print("---------------------")
    print("Total players: {}\n".format(len(team)))
    print("Players on Team:")
    players_name = []
    for name in team:
        players_name.append(name['name'])
    print(', '.join(players_name))
    print("\n")
    input("Press Enter to continue...")
    main_app()

clean_data()
balance_teams()
print(experince_player)
print(len(experince_player))
print("\n")
print(unexperince_player)
print(len(unexperince_player))
main_app()
