#------factor of n numbers------------
# keep entering the integer number for which you need to calculate least common factor 
# it will create a dictionary at the end for each input value.
# for eg : you have entered 5 10 15
#result : {5:[1,5]} {10:1,5,10} {15:1,3,5,15}

def get_input(*args):
   try:
      my_list = []
      while True:
         my_list.append(int(input("Please enter your list of number ")))
   except:
      return (my_list)

n = get_input('args')
print()
print("Your list ",n)
dict_lcm ={}
result=[]
i=1
for x in range(len(n)):
   for i in range(1,n[x]+1):
      if n[x] % i == 0:
         a=n[x]
         result.append(i)
         dict_lcm[a] = result
   print(dict_lcm)
   result.clear()
   dict_lcm.clear()
