#class MojRang:
 #   def __init__(self,start,stop):
  #      self.value=start
   #     self.stop = stop
   # def __iter__(self):
    #    return self

# def __next__(self):
    #    if self.value >= self.stop:
           # raise StopIteration
       # else:
        #    current_value= self.value
         #   self.value = self.value + 1
          #  return current_value

#a = MojRang(1,100)
#for i in a:
 #   print(i)

class MojRang:
    def __init__(self, start, stop, step ):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.value >= self.stop) or (self.step < 0 and self.value <= self.stop):
            raise StopIteration
        current_value = self.value
        self.value += self.step
        return current_value

for i in MojRang(0,100,1):
    print(i)


