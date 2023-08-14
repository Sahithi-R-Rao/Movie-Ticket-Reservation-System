from AVL import *
class MovieTheatre:
    def __init__(self):
        self.name=""
        self.phno=0
        self.seatno=0
        self.bookedseatstotal=[]
        self.seatlistcollection=[]
        
    def display(self):
        print("\n###########################################################################################")
        print("\nEvening Shows\n(06:30 PM - 9:00 PM IST):\n\n\t\t\t**NOW SHOWING**")
        print("\n1. RRR\n2. KGF 2")
        print("\n###########################################################################################\n")


    def new_booking(self, tree, root):
        global booking_id
        booking_id+=1
        global total_seats
        name=input("Enter your Name: ")
        phno=input("Enter your Phone Number: ")
        seatno=int(input("Enter No of Seats: "))
        if total_seats>=seatno:
            total_seats=total_seats-seatno
            seats=[]  #individual customer booked seat list
            for i in range(seatno):
                seat=int(input("Enter Seat No: ")) #individual seat no
                if seat in self.bookedseatstotal:
                    seat=int(input("Seat taken, enter a new seat no:"))
                seats.append(seat)
                self.bookedseatstotal.append(seat)
            self.seatlistcollection.append(seats)
            print("-------------------------------------------------------------------------------------------")
            global info
            info=""
            info=info+name+"#"+phno+"#"+str(seatno)+"#"+str(seats)
            print("\n\t\t\t**Booking ID generated!**")
            print("\nYour Booking ID is: ", str(booking_id)+"#"+info, "\n")
            print("-------------------------------------------------------------------------------------------")
            root=tree.insert(root, booking_id, info, seats)
            
        else:
            print("-------------------------------------------------------------------------------------------")
            print("\nYou require ", seatno, "seats but only", total_seats, " are available. ")
            print("\nBooking cannot complete.\n")
            print("-------------------------------------------------------------------------------------------")
        return root
            
    def seatavailability(self, bookedseatstotal):
        print("Seats available:")
        print("\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
        print("\n\n|*________________________________________*|\n\n")
        print("\n             SCREEN THIS WAY!\n\n")
        cnt = 0
        for i in range(1, 101):
            if i in self.bookedseatstotal:
                cnt = cnt + 1
                if cnt<10:
                    print('{:>4}'.format("**"), end="")
                else:
                    print('{:>4}'.format("**"), end="")
                    print("\n")
                    cnt = 0
            else:    
                cnt = cnt + 1
                if cnt<10:
                    print('{:>4}'.format(i), end="")
                else:
                    print('{:>4}'.format(i), end="")
                    print("\n")
                    cnt = 0
                        
                if i == 50:
                    print("\n\n")
        print("\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
    def cancel(self, bookedseatstotal, tree, root):
        bookid=int(input("\nPlease enter your Booking ID. Your Booking ID consists of all the \nnumbers that appear before the first # symbol:"))
        result= tree.searchNode(root, bookid )
        cancelList=[]
        if result== False:
            print("\nInvalid Booking ID, try again.")
            self.cancel(self, bookedseatstotal, tree, root)
        else:
            print("\nBooking ID validated. You can proceed. The seats you have booked: ")
            tree.viewSeats(root, bookid)
            c1=int(input("\nDo you want to:\n1. Cancel the whole booking\n2. Cancel a part of the booking. "))
            if c1==2:
                     noOfSeats=int(input("\nEnter the number of seats you want to cancel:" ))
                     for i in range(0, noOfSeats):
                              s=int(input("\nEnter the Seat Number you want to cancel booking for: "))
                              if s in self.bookedseatstotal:
                                  cancelList.append(s)
                                  tree.updateTicket(root, bookid, cancelList)
                                  self.bookedseatstotal.remove(s)
                                  print("\nSeat booking for Seat", s, " has been cancelled!")
                                  print(self.bookedseatstotal)
                              self.seatavailability(self.bookedseatstotal)
                              for i in range(0, len(self.seatlistcollection)):
                                  if s in self.seatlistcollection[i]:
                                           self.seatlistcollection[i].remove(s)
                              print(self.seatlistcollection)
            else:
                     #print("Root.seats", root.seats)
                     res=tree.returnList(root, bookid, [])
                     t=tree.delete(root, bookid, [])
                     print(res)
                     #t=res[0]
                     #temp=res[1]
                     #print(temp)
                     print("Total booked seats before for: ", self.bookedseatstotal)
                     for i in res:
                              self.bookedseatstotal.remove(i)
                     #print(t)
                     print("Seat Booking for Booking ID: ", bookid, " has been cancelled. ")
                     print("Root.seats", root.seats)
                     print("Total booked seats", self.bookedseatstotal)
                     
                     


   

                
            

        
global root
bookedseatstotal=[] #total booked seats
print("===========================================================================================")
print("\t\t\tWelcome to ADS Cinemas!")
print("===========================================================================================")
tree=AVL_Tree()
AVLroot=None
RRRtree=AVL_Tree()
RRRroot=None
KGFtree=AVL_Tree()
KGFroot=None
MT=MovieTheatre()
RRRMT=MovieTheatre()
KGFMT=MovieTheatre()
dummyflag=0
totaldummylist=[]
for i in range(1, 101):
    totaldummylist.append(i) 
while dummyflag==0:
    print("-------------------------------------------------------------------------------------------")
    print("\nMenu:")
    print("\n1. Now showing\n2. Book tickets for shows\n3. View Seat availability\n4. Cancel tickets\n5. Exit\n")
    print("-------------------------------------------------------------------------------------------")
    c=int(input("Enter your choice: "))
    print("-------------------------------------------------------------------------------------------")
    if c==1:
        MT.display()
        continue
    elif c==2:
        print("\n\t\t\t**FILMS SCREENING**")
        print("Enter your choice.\n1. RRR\n2. KGF 2")
        print("-------------------------------------------------------------------------------------------")
        choice=int(input())
        print("-------------------------------------------------------------------------------------------")
        if choice==1:
            total_seats=100
            booking_id=1000
            RRRMT.seatavailability(RRRMT.bookedseatstotal)
        elif choice==2:
            total_seats=100
            booking_id=2000
            KGFMT.seatavailability(KGFMT.bookedseatstotal)
        while choice==1 or choice==2:
            if choice==1:
                letsbook=input("Proceed to Book(Y/N): ")
                letsbook = letsbook.upper()
                clarify = ""
                while letsbook=='Y':
                    RRRroot=RRRMT.new_booking(RRRtree, RRRroot)
                    letsbook='N'
                    clarify=input("Book another customer(Y/N): ")
                    clarify = clarify.upper()
                    while clarify=='Y':
                        RRRroot=RRRMT.new_booking(RRRtree, RRRroot)
                        clarify=input("Continue booking for this show(Y/N): ")
                        clarify = clarify.upper()
                print("\nBooking Information of Customers: ")
                RRRtree.preOrder(RRRroot)
                RRRMT.seatavailability(RRRMT.bookedseatstotal)
                letsbook='N'
                choice=0
                
            elif choice==2:
                letsbook=input("Proceed to Book(Y/N): ")
                letsbook = letsbook.upper()
                while letsbook=='Y':
                    KGFroot=KGFMT.new_booking(KGFtree, KGFroot)
                    letsbook='N'
                    clarify=input("Book another customer(Y/N): ")
                    clarify = clarify.upper()
                    while clarify=='Y':
                        KGFroot=KGFMT.new_booking(KGFtree, KGFroot)
                        clarify=input("Continue booking for this show(Y/N): ")
                        clarify.upper()
                print("\nBooking Information of Customers: ")
                KGFtree.preOrder(KGFroot)
                KGFMT.seatavailability(KGFMT.bookedseatstotal)
                choice=0
    elif c==3:
        print("\nWhich film do you want to check seat availability for:\n ")        
        c1=int(input("Enter your choice.\n1. RRR\n2. KGF 2\n"))
        if c1==1:
            RRRMT.seatavailability(bookedseatstotal)
        if c1==2:
            KGFMT.seatavailability(bookedseatstotal)
    elif c==4:
        print("\nWhich show do you want to cancel your booking for?:")
        show=int(input("Enter your choice.\n1. RRR\n2. KGF 2\n"))
        if show==1:
            RRRMT.cancel(bookedseatstotal, RRRtree, RRRroot)
        elif show==2:
            KGFMT.cancel(bookedseatstotal, KGFtree, KGFroot)        
    else:
        break



                

