class Lake:
      def __init__(self,name,location,depth,width,size,ltype):
            self.name = name
            self.location = location
            self.depth = depth
            self.width = width
            self.size = size
            self.ltype = ltype

#Any method of a class should have a aparameter "self" and we use it to identify the properties of a class.
#All objcets belog to a class
#shish method(__init__) is a special method used to identify properties of a class.
#the first parameter in the shish parenthesis(self) refers to an individual class and not an attribute.
#creating objects of a classlake
            
lake1 = Lake("victoria", "Uganda,""1200ft","4000m","500km","salty")
           
class River:
      def __init__(ozzy,name,location,length):
            ozzy.name = name
            ozzy.location = location
            ozzy.length = length

class Waterfall:
     def __init__(self,a,b,c):
      self.name = a
      self.location = b
      self.length = c
Waterfall1 = Waterfall("karuma","northern","600km")


                  