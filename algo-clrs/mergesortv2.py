def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        print " {0} ..... {1}".format(lefthalf,righthalf)
        # Sort both halfs separately
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0 # Add in increasing from beginning alist (in subtasks it will be lefthalf and righthalf)
        # Add smallest of both Until one of the list is empty
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        # Add the remaining left if righthalf is finished
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        # Add the remaining righthalf if lefthalf is finished
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

#alist = [54,26,93,17,77,31,44,55,20]
alist = [31, 41, 59, 26, 41, 58]

mergeSort(alist)
print(alist)
