import threading
import time

class Schedule():
    def __init__(self,matchDB):
        self.matches=matchDB
    
    def delete(self):
        print("Enter the Match ID which you want to delete:")
        match_id=int(input("Enter matchid:"))
        index=0
        for li in self.matches:
            if li["MatchId"]==match_id:
                del self.matches[index]
                print("Deleted match details")
                break
            index+=1
                
    def add(self):
        print("Adding new match details please answer following:")
        match_id=int(input("Enter matchid:"))
        for key in self.matches:
            if key["MatchId"]==match_id:
                print("Match id Already exists")
                return
        teams=input("Enter Teams:")
        venue=input("Enter Venue:")
        date=input("Enter Date:")
        
        matchdetails={"Teams":teams,"Venue":venue,"Date":date}
        newmatch={"MatchId":match_id,"Match Details":matchdetails}
        self.matches.append(newmatch)
        
    def retrive(self):
        print("*" * 40)
        if len(self.matches)==0:
            print("No matches Scheduled yet")
            return
        for match_list in self.matches:
            for key, value in match_list.items():
                if type(value) == dict: #check if the value is a dictionary
                    print(f"  {key}:")
                    for sub_key, sub_value in value.items():
                        print(f"    {sub_key}: {sub_value}")
                else:
                    print(f"  {key}: {value}")
            print("*" * 40)
            
    def start(self):
        while True:
            print("*"*40)
            print("Please select Below options:")
            print("1.Retrive")
            print("2.Add")
            print("3.Delete")
            print("Press any other key to exit")
            print("*"*40)
            user_input=input("Enter your choice")
            if user_input=="1":
                time.sleep(5)
                self.retrive()
                time.sleep(5)
            elif user_input=="2":
                time.sleep(5)
                self.add()
                time.sleep(5)
            elif user_input=="3":
                time.sleep(5)
                self.delete()
                time.sleep(5)
            else:
                break