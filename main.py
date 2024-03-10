nric = input('Enter an NRIC number: ')
nric = nric.strip().upper()
check = True
ST = 'JZIHGFEDCBA'
FG = 'XWUTRQPNMLK'

if nric[0] != 'S' and nric[0] != 'T' and nric[0] != 'F' and nric[0] != 'G':
  check = False
elif len(nric) != 9:
  check = False
elif nric[1:8].isdigit() != True or nric[-1].isalpha() != True:
  check = False

if check == True:
  weight = int(nric[1])*2 + int(nric[2])*7 + int(nric[3])*6 + int(nric[4])*5 + int(nric[5])*4 + int(nric[6])*3 + int(nric[7])*2
  if nric[0] == 'T' or nric[0] == 'G':
    weight += 4
  remainder = weight % 11
  if nric[0] == 'S' or nric[0] == 'T':
    if nric[-1] != ST[remainder]:
      check = False
  else:
    if nric[-1] != FG[remainder]:
      check = False

if check == True:
  print('NRIC is valid.')
else:
  print('NRIC is invalid.')