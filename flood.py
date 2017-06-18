_verify = True   #if the network filters https traffic
                 #set to false to turn off verification

from main import kahoot
import threading
import sys
import time

# Editor: Ellie 
# Author: msemple1111

names = ["Potato", "Sandwich", "Kahoot Admin", "Smelly", "Pop", "Lop", "xcdee",
         "ayylmao", "putu", "ikea", "sweden", "meatballs", "tasty", "lollypops",
         "famalam", "fammsquad", "squadfam", "bad bing", "google.arabia",
         "Hakiu", "literally poop", "bitsize", "key in the door", "100",
         "32", "pokemen", "help", "moist", "history", "hotdog", "polse",
         "leprecorn", "united kingdom", "Tonald Dump", "bb obama", "fishfinger",
         "thresa moo", "dritt", "coading", "flash", "scratch sucks", "notepad++",
         "art", "skateboard", "cow", "moooo", "Rhio", "pee game", "ethics",
         "naked cowboy", "cabbage", "vegans", "focus angus", "drugs", "weed",
         "drugs4pugs", "jesus", "gandelf", "xd", "hah", "<3", "lol", "english bean",
         "tombo", "daluk", "poppadoms", "oh noo", "abc123", "pollak", "chicken"]
		 
def kahoot_run(pin, name, verify):
  send = kahoot(pin, name)
  send.verify = verify
  send.connect()

def test_connection(pin):
  send = kahoot(pin, "Test Name")
  return send.testSession()

def find_two_factor_code(pin):
  send = kahoot(pin, "Test Name")
  send.reserve_session()
  while self.twoFactorCount < 24:
    time.sleep(0.05)
  if self.twoFactorSolved:
    print('true')
    print(self.twoFactor)
  else:
    print('false')

def start_kahoot_run():
  t = threading.Thread(target=kahoot_run, args=(pin,name,verify ))
  print("Establishing:",name)
  t.daemon = True
  t.start()
  esc()

def get_input():
  try:
    pin = sys.argv[1]
    exc = sys.argv[2]
    if (len(sys.argv) > 4):
      if (sys.argv[3].lower() =='false'):
        verify = False
    else:
      verify = True
  except:
    pin = input("Enter a Kahoot pin: ")
    exc = input("Enter how many names to add (you can add your own in file, ask bb): ")
    verify = _verify
  try:
    if (exc == None) or (pin == None):
      print("Please input properly")
      return get_input()
    else:
      return int(pin), int(exc), bool(verify)
  except:
    print("\nPlease provide valid input:")
    return get_input()

def esc():
  while True:
    esc = input("> ")
    if esc.lower() == 'e':
      break
    else:
      print("> invalid input")
      
if __name__ == '__main__':
    print("""\n-------------------------------------------------
      \tWelcome to the Kahoot Flood v2.3 \n
      \t\tby Ellie <3
      \n-------------------------------------------------\n
      I am not responsible for any badness caused by this program, it's 'educational'""");
    pin, exc, verify = get_input()
    if test_connection(pin):
      print("Connecting...")
      i = 0;
      for a in names:
        if i > exc:
          break
        name = a;
        time.sleep(0.1)
        start_kahoot_run()
        i = i+1
      print("\nFinished\nLeave running to keep accounts connected\nPress E to Exit\nBtw you can't disconnect the bot without restarting ;) <3")
      esc()
    else:
      print("A game was not found with that pin :(.")



