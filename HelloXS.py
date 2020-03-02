# My First Python App

# Author = Mike Wojke
# Maintainer = 'Mike Wojke'
# Version = '0.2.0'

from termcolor import cprint
import time

y = 1
while True:
    cprint ('Iteration #'+str(y),'white', 'on_yellow')
    cprint ('Hello Expert Services!' , 'red')
    cprint ('DevOps or Bust!!', 'green')
#    cprint ('Testing Ghetto CI/CD')
    time.sleep (5)
    y += 1
x += x
