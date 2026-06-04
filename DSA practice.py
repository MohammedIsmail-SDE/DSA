start = "car is started"
stop = "car is stopped"

while True:
    game = input(">").lower()
    if game == "start":
        print(start)
    elif game == "stop":
        print(stop)
    elif game == "help":
        print("start - to start a car\nstop - to stop the car\nquit - to quit")
    elif game == "quit":
        print("Game is over")
        break
else:
 print("I don't understand 🤷‍♂️")