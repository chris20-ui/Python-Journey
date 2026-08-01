Pass = 0
Fail = 0

for i in range(5):
      
   Grade= int (input("Enter Grade: "))

   if Grade >60:
        Pass += 1
   
  
   else:
        Fail += 1

print(f"Passed: {Pass}")

print(f"Failed: {Fail: }")

