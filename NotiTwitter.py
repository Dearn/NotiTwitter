#!/usr/bin/python2.7
import os
import tweepy
import pynotify
import gtk
from multiprocessing import Process


testValue = 1

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        a = pynotify.Notification(tweet.user.screen_name, tweet.text, '/usr/share/pixmaps/notitwitter.png')
        a.set_timeout(10000)
        a.show()
        print 'test'
                
    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False
    
class NotiTwitter(tweepy.StreamListener):
    def zamknijsie(self, event, data=None):
        os.system("killall -9 NotiTwitter.py")

        
    def delete_event(self, widget, event, data=None):
        print "delete event occured"
        # return False
        self.hide_on_delete()
    
    def right_click_event(self, icon, button, time):
        menu = gtk.Menu()
        quit = gtk.MenuItem("Quit")
        quit.connect("activate", self.zamknijsie)
        menu.append(quit)
        menu.show_all()
        menu.popup(None, None, gtk.status_icon_position_menu, button, time, self.statusicon)

    def destroy(self, widget, data=None):
        print "destroy signal occured"
        self.hide_on_delete()
        gtk.main_quit()

    def __init__(self):
        self.statusicon = gtk.StatusIcon()
        self.statusicon.set_from_file("/usr/share/pixmaps/notitwitter.png")
        self.statusicon.connect("popup-menu", self.right_click_event)



    def main(self):
        gtk.main()
   

if __name__ == "__main__":

    pynotify.init('NotiTwitter')
    consumer_key='P5LVRKzOVgW6JgDuEi4IxQ'
    consumer_secret=''
    access_token='351423916-u75BbwS6f6P3SBiGCEjoXC7AauZ3H0Fmk8aTSRRI'
    access_token_secret=''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    gtkgui = NotiTwitter()
    api = tweepy.API(auth)
    l = StreamListener()
    streamer = tweepy.Stream(auth=auth, listener=l)

    
    Process(target=gtkgui.main).start()
    Process(target=streamer.userstream).start()

   
    # first.setDaemon(True)
    # first.start()
    # second.start()

