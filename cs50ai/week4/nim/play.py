from nim import train, play

ai = train(10000)
#play(ai) 0 human players first 1 goes second, goes second always win
play(ai, 1)
