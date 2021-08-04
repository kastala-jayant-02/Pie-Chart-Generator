import matplotlib.pyplot as p
List_length=int(input("Enter Length of a list:"))
lis=[]
lis2=[]
for i in range(List_length):
    ask_user=int(input("Enter Y axis data:"))
    lis.append(ask_user)
for l in range(List_length):
    ask_user2=int(input("Enter X axis data:"))
    lis2.append(ask_user2)
lab_input=input("Enter label of the line graph:")
YAxis_input=input("Enter Y axis name:")
XAxis_input=input("Enter X axis name:")
Title_input=input("Enter Graph title:")
print('''Line Color:
      1.Blue
      2.Green
      3.Cyan
      4.Magenta
      5.Black
      6.White
      7.Yellow
      8.Red''')
ask_user3=input("Enter color you want for the line from above options:")
if ask_user3 =="Blue" or "blue":
      p.plot(lis2,lis,'b',label=l)
elif ask_user3=="Green" or 'green':
      p.plot(lis2,lis,'g',label=l)
elif ask_user3 == 'Cyan' or 'cyan':
      p.plot(lis2,lis,'c',label=l)
elif ask_user3 =='Magenta' or 'magenta':
      p.plot(lis2,lis,'m',label=l)
elif ask_user3=="Black" or 'black':
      p.plot(lis2,lis,'k',label=l)
elif ask_user3=="White" or 'white':
      p.plot(lis2,lis,'w',label=l)
elif ask_user3=='Yellow' or "yellow":
      p.plot(lis2,lis,'y',label=l)
elif ask_user3=='Red' or "red":
      p.plot(lis2,lis,'r',label=l)
p.ylabel(YAxis_input)
p.xlabel(XAxis_input)
p.title(Title_input)
p.legend()
p.show()

