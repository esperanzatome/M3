collection=[]
def Fizz_Buzz(stop):
  for num in range(1,stop):
    if num%15==0:
      collection.append('FizzBuzz')
    elif num%3==0:
      collection.append('Fizz')
    elif num%5==0:
      collection.append('Buzz')
    else:
      collection.append(num)
  return collection
print(Fizz_Buzz(101))  
  

  
   