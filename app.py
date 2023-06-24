import constants


def main():
    # We Make 2 Variables and we Assign to them the Value of the constants data 
    PLAYERS = constants.PLAYERS
    TEAMS = constants.TEAMS
    print("\nBASKETBALL TEAM STATS TOOL\n\n")
    
    def start_menu():
        # we print the Menu to the User
        print("----MENU----\n\n")
        print("Here are your Choices:")
        print("\t1) Display Team Stats")
        print("\t2) Quit\n")
    
        flag = 0
        while (flag == 0):
            try:
                # Asking The User to Enter a number from The Menu
                choice = int(input("Enter an option > "))
                try:
                    if ( choice < 1 or choice > 2):
                        # rasing an Exception if The User Enter Invalid Number 
                        raise Exception("Enter A Valid Option ")
                except Exception as err:
                    print(err)
                else:
                    flag = 1
            # we add an exception if the Value of the Input number not a Integer and we let the user try again 
            except ValueError:
                print("Only Integer are allowed, try Again Please ")
        # Return The Value of the choice Variable 
        return choice


    def display_menu(number):
        # Display the Menu the User and Ask The user to Enter a Number 
        print("\t1) Panthers")
        print("\t2) Bandits")
        print("\t3) Warriors\n")
        flag = 0
        while (flag == 0):
            try:
                # Asking The User to Enter a number from The Menu
                menu_choice = int(input("Enter an option > "))
                try:
                    if ( menu_choice < 1 or menu_choice > 3):
                        # rasing an Exception if The User Enter Invalid Number 
                        raise Exception("Enter A Valid Option ")
                except Exception as err:
                    print(err)
                else:
                    flag = 1
            # we add an exception if the Value of the Input number not a Integer and we let the user try again 
            except ValueError:
                print("Only Integer are allowed, try Again Please ")
        # Return The Value The User choose  
        return menu_choice
            
    def team_stats(number_team):
        # declaring a empty lists called team and guardians to save all the member of the Team Player did choose as well as their guardians.
        team = []
        guardians = []
        # Team Stats Variables , Total Players , Average Height, experienced Player and unexperienced Players.
        total_players = 0
        avr_height = 0
        experienced = 0
        unexperienced = 0 
        index = 0
        # Looping through the balanced data ( Dictionary )  we got from balance_teams() Function.
        for key,value in balanced_teams.items():
            if key == TEAMS[number_team-1]:
                # Looping through the Values of The Team the user did choose.
                for i in value:
                    for x in range(0,len(value[index])):
                        # counting how many Player we are Adding to the team List
                        total_players += 1
                        # Append each Player to the team list
                        team.append(value[index][x])
                    index += 1

        # Calculating the Sum of the Hight of each Player we added to the Team List
        # new_players_data is the data we got from the clean_data() Function.
        for data in clean_collection:
            for player in team:
                if data['name'] == player:
                    avr_height += data['height']
                    # Adding each guardian of the Player to the List guardians
                    guardians.append(data['guardians'])
                # Counting How many Experienced Players and unexperienced Players we have in the Team
                if data['name'] == player:
                    if data['experience']:
                        experienced += 1
                    else:
                        unexperienced += 1
        # calculate the average height and round it to two decimal
        avr_height = round((avr_height / total_players),2)
        # returning the Values of the Lists and Variables we made as Tuple 
        return total_players, experienced, unexperienced, avr_height, team, guardians
    
    

    def clean_data(players):
        # Function which Accept one Argument
        # Empty List which will be used to save our Clean Data
        cleaned_collection = []
        # Looping through the players List.
        for data in players:
            # Empty Dictionary which will be Used to save the new clean Data
            players_new = {}
            for key,value in data.items():
                if key == 'name':
                    # Adding the name key and the value to new Dictionary  
                    players_new[key] = value
                if key == 'guardians':
                    # splitting up the guardian string into a List if there is "and", and saving in in the new Collection 
                    players_new[key] = value.rsplit("and")
                if key == 'experience':
                    if value == 'YES':
                        # if Value of the experience is Yes we convert it to Bool Value True and add it to the new Collection 
                        players_new[key] = True
                    else:
                        # else Value of the experience is No we convert it to Bool Value False and add it to the new Collection 
                        players_new[key] = False
                if key == 'height': 
                    # Convert the Value of height Key to a integer 
                    players_new[key] = int(value.split(" ")[0])
            # we Add the Cleaned Data to the NEW list 
            cleaned_collection.append(players_new)
            # Returning the cleaned Collection 
        return cleaned_collection


    def balance_teams(teams):
        # function to balance the players across the three teams: Panthers, Bandits, and Warriors.
        # Tow empty lists of experienced und unexperienced Players
        experienced_players = []
        unexperienced_players = []
        teams_player = {}
        players = []
        num_player_team = int(len(PLAYERS) / len(TEAMS))
        # we call the count_experienced() function and we dividing we the number of teams we have to balance the teams
        num_experienced_unexperienced = int(count_experienced(players=PLAYERS) / len(TEAMS))
        count = 0
        for player in clean_collection:
            # if player is experienced  we add him to our new List experienced_pLayers
            if player['experience']:
                experienced_players.append(player['name'])
                # check if we have enough experienced Players and we add them to Players List
                if len(experienced_players) == int( num_experienced_unexperienced / 2):
                    players.append(experienced_players)
                    experienced_players = []

            # if player is unexperienced  we add him to our new List unexperienced_pLayers
            if not player['experience']:
                unexperienced_players.append(player['name'])
                # check if we have enough experienced Players and we add them to Players List
                if len(unexperienced_players) == int(num_experienced_unexperienced / 2):
                    players.append(unexperienced_players)
                    unexperienced_players = []

            if len(players) == 2:
                teams_player.update({TEAMS[count]: players})
                players = []
                count = count + 1
        # we return the new made collection we the balanced Teams
        return teams_player


    def count_experienced(players):
        # Counting how many experiences Players and unexperienced Players we have on the Main Collection 
        experienced = 0
        unexperienced = 0
        total = 0
        for player in clean_collection:
            if player['experience']:
                experienced += 1
            else:
                unexperienced += 1                
        total = experienced  + unexperienced
        # returning the Total Number
        return total

    # assign the return Value of the clean_data()function to new Variable
    clean_collection  = clean_data(PLAYERS)
    # Here Start the running Program
    flag = 0
    # LOOP which will run till the User Enter 2 Which will Assign The Variable Flag the Value of 1 and we Quit
    while (flag == 0):
        # We Assign the return Value of the Start Menu Function to Number Variable
        number = start_menu()
        # if the Value of the Number is 2 We end the Loop 
        if number == 2:
            flag = 1
        else:
            # Assigning the return of the Function balance_team() to balanced_teams
            balanced_teams = balance_teams(TEAMS)
            # Assigning the return of the Function display_menu() to chosen_team
            chosen_team = display_menu(number)
            # Printing The Stats of the Team The User chose
            print(f"Team: {TEAMS[chosen_team-1]} Stats ")
            print("-----------------------------------")
            # Team stats Function Return A tuple with 5 index.
            # Index 0 is the Total Players.
            print(f"Total Players: {team_stats(chosen_team)[0]}")
            # Index 1 is the Total experienced PLayers.
            print(f"Total experienced: {team_stats(chosen_team)[1]}")
            # Index 2 is the Total unexperienced Players.
            print(f"Total Unexperienced: {team_stats(chosen_team)[2]}")
            # Index 3 is the Average Height in the Team.
            print(f"Average height: {team_stats(chosen_team)[3]}\n")
            print("Players on Team: \n")
            # Index 4 is List of PLayers on the Team.
            for player in team_stats(chosen_team)[4]:
                print(player, end=", ")
            print("\n")
            print(f"Guardians: ")
            # Index 4 is List of Guardians.
            for guardian in team_stats(chosen_team)[5]:
                for i in guardian:
                    print(i, end=", ")
            print("\n")
        
    
    

if "__main__" == __name__:
    main()