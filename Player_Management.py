import threading
threadLock = threading.Lock()# to prevent race around condition

class Player(threading.Thread):
    def __init__(self,player_stats):
        threading.Thread.__init__(self)
        self.pstats=player_stats
        self.last_player_id = None
        if len(self.pstats)!=0:
            self.last_player_id=max(pstats["player_id"] for pstats in player_stats) 
        else:
            self.last_player_id=0
    
    def retrive_stats(self):
        print("Stats of all players are:")
        print("*"*40)
        for list_key in self.pstats:
            for key,value in list_key.items():
                with threadLock:
                    print(f"{key}:{value}")
            print("*"*40)
    
    def add(self):
        name=input("Enter Player Name:")
        avg=int(input("Enter new batting avg:"))
        country=input("Enter Country Name:")
        home_runs=int(input("Enter new home runs count:"))
        sout=int(input("Enter new strikeout count:"))
        pid=self.last_player_id+1
        new_player={"player_id":pid,"player_name":name,"team_name":country,"batting_avg":avg,"home_runs":home_runs,"strike_out":sout}
        self.pstats.append(new_player)
            
    def update_stats(self):
        while(True):
            player_id=int(input("Enter Player ID to update stats:"))
            present=False
            for list_key in self.pstats:
                if list_key.get("player_id") == player_id:
                    present= True
                    break
                    
            if present == True:
                print("Choose below options for updating stats")
                print("1.Batting avg,2.Home runs,3.Strike outs,press any other key to exit")
                for list_items in self.pstats:
                    user_input=input("Enter your choice:")
                    if user_input=="1":
                        avg=int(input("Enter new batting avg:"))
                        list_items["batting_avg"]=avg
                    elif user_input=="2":
                        home_runs=int(input("Enter new home runs count:"))
                        list_items["home_runs"]=home_runs
                    elif user_input=="3":
                        sout=int(input("Enter new strikeout count:"))
                        list_items["strike_out"]=sout
                    else:
                        print("Bye,Have a nice day")
                    print(f"Updated stats for Player: {player_id}")
                    break
            else:
                print("Player ID not present, Pls try again")
                break
            break    

    def run(self):
        while True:
            print("*"*40)
            print("Please select Below options:")
            print("1.Retrive")
            print("2.Add")
            print("3.Update")
            print("Press any other key to exit")
            print("*"*40)
            user_input=input("Enter your choice")
            if user_input=="1":
                time.sleep(5)
                self.retrive_stats()
                time.sleep(5)
            elif user_input=="2":
                time.sleep(5)
                self.add()
                time.sleep(5)
            elif user_input=="3":
                time.sleep(5)
                self.update_stats()
                time.sleep(5)
            else:
                time.sleep(5)
                break