
# Recursive list sum
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
    	mid = len(numList)//2
        return listsum(numList[:mid])+listsum(numList[mid:])

def factorial(num) :
	if num > 1:
		return num*factorial(num-1)
	else:
		return 1 # Needed Exit Case otherwise NoneType is returned by Factorial(1)

if __name__ == "__main__":
	print(listsum([1,3,5,7,9]))
	print(factorial(4))
