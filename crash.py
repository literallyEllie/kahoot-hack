_verify = True   #if the network filters https traffic
                 #set to false to turn off verification

import sys
from main import kahoot, error
import time

# Author: Ellie

def get_input():
  try:
    name = sys.argv[1]
    pin = sys.argv[2]
    if (len(sys.argv) > 3):
      if (sys.argv[3].lower() =='false'):
        verify = False
    else:
        verify = True
  except:
    pin = input("Kahoot Pin: ")
    name = input("Culprit name: ")
    verify = _verify
  try:
    return int(pin), str(name), bool(verify)
  except:
    print("Please input properly")
    error(0,"not proper input", True)

def esc():
  while send.end == False:
    if send.end == True:
      print("Done")
    else:
      time.sleep(0.1)


if __name__ == '__main__':
    print("""\n-------------------------------------------------
      \tWelcome to the Kahoot Crashed [UNTESTED] v2.1 \n
      \t\tby Ellie <3
      \n-------------------------------------------------\n
      I am not responsible for any badness caused by this program, it's 'educational'""");
    pin, name, verify = get_input()
    print ("Connecting...")
    send = kahoot(pin, name)
    send.verify = verify
    send.connect()
    send.run_game(True)
    esc()



