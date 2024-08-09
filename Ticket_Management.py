import threading
import time

class Ticket():
    def __init__(self,matchDB,ticketDB):
        self.match=matchDB
        self.ticket=ticketDB
        self.last_ticket_number = None
        if len(self.ticket)!=0:
            self.last_ticket_number=max(ticket["TicketNumber"] for ticket in ticketDB) 
        else:
            self.last_ticket_number=0
        
    def bookticket(self):
        print("Welcome to Ticket Booking,enter below details:")
        print("See list of ongoing matches:")
        print("*"*40)
        for listkey in self.match:
            for key,value in listkey.items():
                print(f"{key}:{value}")
        print("*"*40)
        matchid=int(input("Enter the match ID form above matches:"))
        present=False
        for listitems in self.match:
            if listitems.get("MatchId")==matchid:
                present=True
                break
                
        if present:
            name=input("Enter Your Name:")
            address=input("Enter Your Address:")
        else:
            print("Invalid Match ID, pls try again")
            return
        
        newticket={"TicketNumber":self.last_ticket_number+1,"MatchID":matchid,"Name":name,"Address":address}
        self.ticket.append(newticket)
        print("Ticket Booked")
        
    def cancelticket(self):
        ticketnumber=int(input("Enter Ticket Number to cancelticket:"))
        valid=False
        index=0
        for listitems in self.ticket:
            if listitems.get("TicketNumber")==ticketnumber:
                del self.ticket[index]
                valid=True
                print("Ticket Deleted")
                break
            index+=1
            
        if valid==False:
            print("Invalid ticket number,pls try again")
    
    def retriveticket(self):
        ticketnumber=int(input("Enter Ticket Number:"))
        valid=False
        index=0
        for listitems in self.ticket:
            if listitems.get("TicketNumber")==ticketnumber:
                print(self.ticket[index])
                valid=True
                break
            index+=1
            
        if valid==False:
            print("Invalid ticket number,pls try again")

    def options(self):
        while True:
            print("*"*40)
            print("Please select Below options:")
            print("1.Retrive")
            print("2.Book")
            print("3.Cancel")
            print("Press any other key to exit")
            print("*"*40)
            user_input=input("Enter your choice")
            if user_input=="1":
                time.sleep(5)
                self.retriveticket()
                time.sleep(5)
            elif user_input=="2":
                time.sleep(5)
                self.bookticket()
                time.sleep(5)
            elif user_input=="3":
                time.sleep(5)
                self.cancelticket()
                time.sleep(5)
            else:
                break