# stop = "car stopped"
# start = " Car Started...Ready To GO!"

# while 1:
#      car_game = input(" >").lower()
#      if car_game == "start" :
#           print (start)
#      elif car_game == "help":
#           print(" start - To start the car \n stop - to stop the car \n quit - to exit \n")
#      elif car_game in {"stop", "quit"} :
#          if car_game == "stop": print(stop)
#          break
#      else:
#           print ("I don't understand that...🤷‍♂️")

start = "car is started"
stop = "car is stopped"
is_car_started = False
is_car_stopped = False
while True:
        game = input("> ").lower()
        # breakpoint()
        if game == "start":
                if not is_car_started:
                    print(start)
                    is_car_started = True
                else:
                    print("Car Already running.....")
        elif game =="start" :
                print("Car is already started")
        elif game == "stop":
                if not is_car_stopped :
                 print(stop)
                 is_car_stopped = True
                else :
                       print("car is already stopped !!!!")

        elif game == "help":
                print("start - to start a car\n stop - to stop the car\n quit - to quit")
        elif game == "quit":
                print("Game is over")
                break
        else:
                print("I don't understand 🤷‍♂️")