def pow_no(base, ex):
  result=1
  for i in range(ex):
    result=result*base
    i+=1
  return result

b=int(input("Enter base : "))
p=int(input("Enter exponent : "))
a=pow_no(b,p)
print("The answer is : ",a)