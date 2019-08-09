m=list(map(int,input().split(' ')))
m.remove(m[0])
def mergeSort(m):
    if len(m)>1:
        mid = len(m)//2
        lefthalf = m[:mid]
        righthalf = m[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                m[k]=lefthalf[i]
                i=i+1
            else:
                m[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            m[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            m[k]=righthalf[j]
            j=j+1
            k=k+1

mergeSort(m)
for i in m: print(i,end=' ')
