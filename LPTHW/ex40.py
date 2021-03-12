class song(object):

    def __init__(self,lyrics):
     self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = song(["happyB'day to you",
"what the fuck is this",
"ok just stop"])
bulls_on_parade = song(["ohh la la",
"ye kya hua",
"ab me kya karu"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
