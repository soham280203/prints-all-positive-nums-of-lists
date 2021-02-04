'''------------This code takes numbers as input in lists and prints only positive numbers among inputted numbers------------'''
list1=[]
list2=[]
n=int(input("Enter number of elements in list1 : ")) #input as [12, -7, 5, 64, -14]
m=int(input("Enter number of elements in list2 : ")) #input as  [12, 14, -95, 3]
print("Enter numbers in list1:")
for i in range(0, n):
    num=int(input())
    list1.append(num)
print("Enter numbers in list2:")
for i in range(0, m):
    num1=int(input())
    list2.append(num1)
print("list1 is %d list2 is %d ",list1,list2 )
print("Output for list1 after sorting")#Output: 12, 5, 64
i=0
while (i<n):
    if (list1[i]>=0):
        print(list1[i])
        i=i+1
    elif (list1[i]<=0):
        i=i+1
print("Output for list2 after sorting")#Output: [12, 14, 3]
i = 0
while i < len(list2):
  if list2[i] < 0:
    list2.remove(list2[i])
    continue
  i=1+i
print(list2)
