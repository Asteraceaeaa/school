def zz(n):  
    a='0000' + bin(n)[2:]
    na = ''
    for i in a:
        if int(i)==0:
         na+='1'
        else:
            na+='0'
    number=int(na,2)
    raznost=number-n
    return  raznost

for d in range(256):
   result=zz(d)
   if result==111:
      print(result)

        
