from urllib.request import urlopen
from playsound import playsound
def connected():
   state=False
   while state!=True:
      try:
         response=urlopen("http://216.58.192.142",timeout=1)
         playsound('dialup.mp3')
         return True
         state=True
      except:
         return False
         state=False
connected()