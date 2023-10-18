#get input from user
n1 = []
ele = int(input("Enter number of elements to be added in the list:"))

for i in range(0, ele):
    lst = int(input())
    n1.append(lst)
print("Original list is:",n1)

for i in range(0,len(n1)):
    for j in range(i+1,len(n1)):
        if n1[i] <= n1[j]:
            n1[i],n1[j] = n1[j],n1[i]

print("Sorted list is:",n1)

