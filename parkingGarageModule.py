# John Burgess
class Parking_garage():
    tickets = []
    parking_spaces = []
    def __init__(self, capacity, available_tickets, current_ticket = {}, leaving = False):
        self.capacity = capacity
        self.available_tickets = available_tickets
        self.current_ticket = current_ticket
        self.leaving = leaving

    def driver(self): 
        while True:
            if not self.tickets:
                res = input("\n---Welcome to the garage!---\nWould you like to:\n\t[1] Take a ticket? Enter '1', or enter [Q] to quit.\n")
            else: 
                res = input("\n---Welcome to the garage!---\nWould you like to:\n\t[1] Take a ticket\n\t[2] Pay your ticket\n\t[3] Exit the garage\n\n(Enter 1, 2, or 3. To cancel, enter [Q])\n")
            
            if res.lower() == 'q':
                break

            elif res == '1':
                self.take_ticket()
            
            elif res == '2':
                self.pay_for_parking()
            
            elif res == '3':
                self.leave_garage()
            else:
                print('\nPlease enter a valid response!')
# Hamed Yurteri
    def take_ticket(self):
        if self.available_tickets > 0:
            print("Here is your ticket.")
            self.capacity -= 1
            self.available_tickets -= 1
            self.tickets.append('ticket')
            print(f"There are [{self.capacity}] parking spaces available.")
            print(f"There are [{self.available_tickets}] tickets remaining.")
            self.current_ticket['paid'] = False
        else:
            print("Garage Full")

    def pay_for_parking(self):
        
        payment = input("How much will you pay?\n")
        while int(payment) <= 0 :
           payment = input("You must make your payment before exiting the garage.\n")
    
        else:
            self.current_ticket['paid'] = True
            print(f"You paid ${payment},")

        if self.leaving:
            self.leave_garage()
        else:
            print("Thank you for your payment. Please exit the garage within 15 minutes.")

    def leave_garage(self):
        self.leaving = True
        while self.leaving:
            if self.current_ticket['paid']:
                print("\nThank You, \nHave a nice day!\n")
                self.tickets.pop()
                self.leaving = False
                self.capacity += 1
                self.available_tickets += 1
                print(f"There are [{self.capacity}] parking spaces available.")
                print(f"There are [{self.available_tickets}] tickets remaining.")
    
                
            else:
                print('\nPlease pay your ticket before departing.')
                self.pay_for_parking()
        
my_garage = Parking_garage(3, 3)

my_garage.driver()
