stop = "car stopped"
start = " Car Started...Ready To GO!"

while 1:
     car_game = input(" >").lower()
     if car_game == "start" :
          print (start)
     elif car_game == "help":
          print(" start - To start the car \n stop - to stop the car \n quit - to exit \n")
     elif car_game in {"stop", "quit"} :
         if car_game == "stop": print(stop)
         break
     else:
          print ("I don't understand that...🤷‍♂️")