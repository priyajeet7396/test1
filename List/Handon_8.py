a=[1,2,3,4,5,6,6,5,4,3,2,1]


b=int(input("Enter the number of which 1 occurance to remove"))
c=0
for i in a:
  if i==b:
     break
  c=c+1 


del a[c]

for j in a:
  print(j)