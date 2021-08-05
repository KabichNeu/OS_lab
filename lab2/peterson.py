import threading
import random
import time

class PetersonSolution():
    other = 1
    turn = 0
    
    interested = [False, False]
    def EntrySection(self,*args):
        PetersonSolution.other = 1 - args[0]
        PetersonSolution.interested[args[0]] = True
        PetersonSolution.turn = args[0]

        while PetersonSolution.interested[PetersonSolution.other] == True and PetersonSolution.turn == args[0]:
            print(f"Process {args[0]} is waiting")
        print(f"Process {args[0]} Entered Critical Section")
        
        self.ExitSection(args[0])
        time.sleep(3000)

    def ExitSection(self,process):
        PetersonSolution.interested[process] = False
    def main(self):
        while True:
            t1 = threading.Thread(target = self.EntrySection, args = (0,)) 
            t1.start()
            t2 = threading.Thread(target = self.EntrySection, args = (1,)) 
            t2.start()


if __name__ == "__main__":
    p = PetersonSolution()
    p.main()