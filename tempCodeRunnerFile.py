number = 9
staring_number = 0
ending_number = 3
while staring_number < ending_number :
     game = int(input("Guess :"))
     staring_number += 1
     if game == number:
          print ("You win")
          break
else:
     print ("Sorry you lost")
wining_number = 9 
staring_number = 0
ending_number = 4