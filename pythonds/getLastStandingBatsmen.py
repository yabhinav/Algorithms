# 
def  getLastBatsmen(striker, ball):
	if striker == 1:
		nonstriker = 2
	elif striker == 2:
		nonstriker = 1
	else :
		return "Not possible to take 10 wickets it striker is :"+str(striker)+"\n"

	a = 0 #No wickets yet
	while a < 10 : # Till 9 wickets have fallen
		#print striker, nonstriker
		if ball > 6:
			# Over finsihed switch strike
			striker,nonstriker = nonstriker, striker
			ball = 0
		ball =  ball+1 
		a=a+1# wicket has fallen
		striker = a+2 # Next batsmen comes to strike
	return nonstriker

print "When No:1 Batsmen is the first Strike :"
print getLastBatsmen(1,1), getLastBatsmen(1,2),getLastBatsmen(1,3),getLastBatsmen(1,4),getLastBatsmen(1,5),getLastBatsmen(1,6)

print "When No:2 Batsmen is the first Strike :"
print getLastBatsmen(2,1), getLastBatsmen(2,2),getLastBatsmen(2,3),getLastBatsmen(2,4),getLastBatsmen(2,5),getLastBatsmen(2,6)
