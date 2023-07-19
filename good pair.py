def G_pair(array,pair):
    n=len(array)
    count=0
    for i in range(n):
        for j in range(1,n):
            if i!=j:
                if array[i]+array[j]==pair:
                    count+=1
    if count>=1:
        return 1
    else:
        return 0
array= list(map(int,input("Enter the array:").split()))
pair = int(input("Enter the value:"))
print(G_pair(array,pair))
