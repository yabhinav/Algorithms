
# There is a general rule for moving a tower of size n (n > 1) from the peg S
# to the peg T:
# move a tower of n - 1 discs Dn-1 ... D1 from S to A. Disk Dn is left alone
# on peg S Move disk Dn to T move the tower of n - 1 discs Dn-1 ... D1 on A to
# T, i.e. this tower will be put on top of Disk Dn

def moveTower(height, fromPole, toPole, withPole):
	if height >=1:
		moveTower(height-1, fromPole, withPole, toPole)
		moveDisk(fromPole,toPole)
		moveTower(height-1, withPole,toPole,fromPole)

def moveDisk(fp,tp):
	print("Moving Disk from",fp,"to",tp)



moveTower(3,"A","B","C")

count=0
### Other Implementation  ###
def hanoi(n, source, helper, target):
    #print "hanoi( ", n, source, helper, target, " called"
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            global count
            count = count+1
            #print "moving " + str(disk) + " from " + source[1] + " to " + target[1]
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        
source = ([4,3,2,1], "source")
target = ([], "target")
helper = ([], "helper")

print source, helper, target
hanoi(len(source[0]),source,helper,target)

print "TotalMoves 2pow({0})-1 : {1}".format(len(target[0]),count)
print source, helper, target

