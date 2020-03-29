chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
import os
password = str(input("Input password: "))
disp = input("Do you ywant to see each guess and attempt #? It will slow down the program. (y/n)")
if not disp == 'y' or not disp == "Y":
  print('This may take a while...')
guess = []
base61 = []
attempts = 0
hmm = 0
for char in password:
  base61.append(0)
  guess.append('_')
guesss = ''
while guesss != password:
  guesss = ''

  thing = 0

  for char in password:
    guess[len(password)-(len(password)-thing)] = chars[base61[thing]]
    thing +=1


  attempts +=1
  base61[0] += 1

  for item in base61:
    if item > 61:
      base61[base61.index(item) + 1] = base61[base61.index(item) + 1] + 1
      base61[base61.index(item)] = 0

  for char in guess:
    guesss += char

  if disp == 'y' or disp == "Y":
    print (guesss)
    print (attempts)
    os.system('clear')
os.system('clear')
print('the password is: ' + guesss)
print('It took: ' + str(attempts) +' attempts to crack.')
rating = ''
if attempts >10000000000:
  rating = "Amazing"
elif attempts > 1000000000:
  rating = 'Alright'
elif attempts > 100000000:
  rating = 'ok'
elif attempts > 10000000:
  rating = 'eh'
elif attempts > 1000000:
  rating = 'bad'
elif attempts > 100000:
  rating = 'terrible'
elif attempts > 37830:
  rating = 'utter garbage'
elif attempts > 620:
  rating = 'one of the worst passwords ever created'
elif attempts <= 620:
  rating = "The worst password in existence. You wasted everyone's time with this. Why would you create this stinking, rotting pile of garbage and use it as a password. You are a dissapointment to everyone around you."
print('rating: ' + rating)
