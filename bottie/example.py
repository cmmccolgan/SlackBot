import time
from slackclient import SlackClient

#Starterbot:
token = "xoxb-48634413793-7u17sky3B5786T9ZPLsWuh50"

#Bottie:
#token = "xoxb-48228368374-bPTRoIBnREBAOV2drqNEkMaR"

sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
