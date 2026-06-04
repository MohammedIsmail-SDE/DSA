start = " car is ready to go "
stop = "car is stopped"
game=input (">").lower

while game == "start":
    print(start)

if game == "stop":
     print(stop)

if game == "help ":
      print ("start - to start a car \n Stop - to stop the car \n quit  - to quit  ")

if game == "quit" :
    print ("Game is over")
    
else :
  print("i dont understand 🤷‍♂️")




        