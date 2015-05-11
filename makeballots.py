from random import *
from math import *
from copy import *

f=open("myrandom", 'a')
f.write(str(getstate()))
f.close()


totalballots=2000 	# total ballots cast

nomineenum=60          # total nominees considered
#nomineenum=450          # total nominees considered
nomineenum1=nomineenum+1

stan=range(0, 5)

# How many votes on a ballot? 
# For novels 2009-2013, usually the top 16 got around 1.35 votes among them.
# ballots averaged around 3.5 votes in 2013.
# probabilities for rare nominees are too high, so that with more than 60 we approach an average of
# 5 votes/ballot. This does not matter for voting systems where rare nominees are quickly eliminated.

pdf=[0]
for x in range(0,nomineenum):
	pdf.append(.10*exp(-.26*(x-1))+.045) # constant should probably be another power series?
	
scratch=1.35/sum(pdf[1:17])

p=[0]	
for i in range(1, nomineenum1):
	p.append(pdf[i]*scratch)

#print(p)

ballots=[]
def setupballots():
	global ballots
	ballots=[]
	for i in range(0, totalballots):
		ballots.append(set())
setupballots()

def fillout():
	global ballots
	setupballots()
	for ballot in ballots:
		while len(ballot)==0:
			for j in range(1, nomineenum1):
				if len(ballot)==5: break
				if random()<p[j]:
					ballot.add(j)
				
# imperfect, completely filled ballots will result in not enough rare votes.
# fix by randomizing nominee order. Expect it's a small effect since filled ballots are rare

fillout()

ballots1=copy(ballots)
names = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"

for i  in range(0, len(ballots)):
	scratch=""
	for vote in ballots[i]:
		scratch  += names[vote] 
	ballots1[i]=scratch + ", "

f=open("ballots", 'w')
for ballot in ballots1:
	f.write(ballot)
f.close()
