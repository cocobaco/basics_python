#guessing game
# http://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

import random


def respond(ran,gues):
    if gues-ran > 10:
        print('way too high')
    elif ran-gues > 10:
        print('way too low')
    elif ran > gues:
        print("too low")
    elif ran < gues:
        print("too high")
    print('guess again')


def guess_loop():
    global ntries
    myrand = random.randint(1,100)
    #print('check: ', myrand)
    myguess = 0
    myguess = int(input('> '))
    while myguess != myrand:
        respond(myrand,myguess)
        myguess = int(input('> '))
        ntries += 1
    print('you got it after %d tries' % (ntries))


print('Hello. Guess a number (1-100):')

ntries = 1
guess_loop()

