#def moj_rang(start,stop):
   # value = start
    #while value <= stop:
     #   yield value
      #  value += 1

#a = moj_rang(1,100)
#for i in a:
 #   print(i)

def moj_rang(start,step):
    value = start
    while True:
        yield value
        value+= step

step = int(input("Vnesi step: "))
a = moj_rang(1,step)
for i in a:
    print(i)