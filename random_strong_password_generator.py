import random

spl = "! @ # $ % ^ & * ( ) _ - [ ] { } \ | : ; > < + = ? /  ~ ".split()

spl.append("'")
spl.append('"')

upper = list(map(chr,range(65,91)))         # map A to Z to a list using ascii chr(ascii_Value)

lower = list(map(chr,range(97,123)))        #map a to z to a list using ascii chr(ascii_value)

num = list(map(str,range(0,9)))           #map 0 to 9 as string 

while (True):

  n = input("Enter the length of the password: ")

  if (n == "0"):
    print("Thank you ... We are leaving :(\n")
    break

  try:
    n = int(n)
  except:
    print("Enter valid length !!\n")
    continue

  if (n>18 or n<6):
    print("Length should be in between 6 and 18 !!\n")
    continue

  s1 = ""
  s1+=random.choice(upper)
  s1+=random.choice(lower)
  s1+=random.choice(num)
  s1+=random.choice(spl)

  pwd = upper+lower+num+spl

  for i in range(n-4):

    s1+=random.choice(pwd)
  print("\n\nWe have successfully Generated your password :) ")
  print("Your Password: ",s1,"\n")
