import copy
import constants
import sys

players = copy.deepcopy(constants.PLAYERS)
teams   = copy.deepcopy(constants.TEAMS)

Panthers  = []
Bandits   = []
Warriors  = []

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
        player['height'] = int(player['height'].split()[0])
        experience = player['experience'].split()
        if experience[0] == "YES":
            player['experience'] = True
            experince_player.append(player)
        else:
            player['experience'] = False
            unexperince_player.append(player)
        player["guardians"] = player["guardians"].split("and")    


def balance_teams():
    num_players_team   = int(len(players)/len(teams))
    num_explayers_team = int(len(experince_player)/len(teams))
    for player in players:
        if len(Panthers) < num_players_team :
            for ex_player in experince_player:
                if len(Panthers) < num_explayers_team :
                    Panthers.append(ex_player)
            if player["experience"] == False:
                Panthers.append(player)        
        elif len(Bandits) < num_players_team:
            for ex_player in experince_player:
                if len(Bandits) < num_explayers_team :
                    Bandits.append(ex_player)
            if player["experience"] == False:
                Bandits.append(player)
        else:
            Warriors.append(player) 


def stats(team,name_team):
    players_name = []
    guardians = []
    num_exp_players   = 0
    num_inexp_players = 0
    sum_height = 0
    for player in team:
        sum_height += player["height"]
        if player["experience"] == True:
            num_exp_players   += 1
        else:
            num_inexp_players += 1 
       
    print("\n")
    print("Team: {} stats".format(name_team))
    print("---------------------")
    print("Total players: {}\n".format(len(team)))
    print("Total experienced: {}\n".format(num_exp_players))
    print("Total inexperienced: {}\n".format(num_inexp_players))
    print("Average height: {}\n".format(sum_height/len(team)))
    for name in team:
        players_name.append(name['name'])
    print("Players on Team:")
    print(', '.join(players_name))
    print("\n")
    for guar in team:
        guardians.append(guar['guardians'])
    print("Guardians:")
    print(', '.join('{}'.format(k) for k in guardians))
    print("\n")
    input("Press Enter to continue...")
    main_app()

clean_data()
balance_teams()
main_app()



'''print("Panthers Team\n")
for p in Panthers:
    print(p)
print("\n")
print("Warriors Team\n")
for p in Warriors:
    print(p)
print("\n")
print("Bandits Team\n")
for p in Bandits:
    print(p)'''
