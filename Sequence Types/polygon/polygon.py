import math

class Polygon: 
    def __init__(self, edges, circumradius): 
         self._edges = edges
         self._circumradius = circumradius
      
    # edges/vertices
    @property
    def edges(self): 
        return self._edges 
      
    # a setter function 
    @edges.setter 
    def edges(self, vertices): 
        if(vertices < 3): 
           raise ValueError("Value Error: Vertices of a Polygon") 
        self._edges = vertices 

    # circumradius
    @property
    def circumradius(self): 
        return self._circumradius 
       
    # a setter function 
    @circumradius.setter 
    def circumradius(self, radius): 
        if(radius < 0): 
           raise ValueError("Value Error: Circum radius value should be positive") 
        self._circumradius = radius
         
    # Interior Angle
    @property
    def interiorAngle(self): 
        return (self.edges - 2)*(180/self.edges)

    # Edge Length
    @property
    def edgeLength(self): 
        return math.floor((2 * self.interiorAngle)*(math.sin(3.14/self.edges)))


    @property
    def apothem(self): 
        return (self.interiorAngle)*(math.cos(3.14/self.edges))

    @property
    def area(self): 
        return (1/2 * self.edges * self.edgeLength * self.apothem)

    @property
    def perimeter(self): 
        return (self.edges * self.edgeLength)

    #Object's information 
    def __repr__(self): 
       return f'Polygon with sides(%s) having circumradius (%s)' % (self.edges, self.circumradius)   

    #Equality check
    def __eq__(self, other):
        if(isinstance(other, Polygon)):
            return ((self.edges == other.edges) and (self.circumradius == other.circumradius))

    #Comparison
    def __gt__(self, other):
        if(isinstance(other, Polygon)):
            return (self.edges > other.edges)
        else:
            raise ValueError("Value Error: Instance is not a valid Polygon to compare") 
       


if __name__ == "__main__":
    p = Polygon(3, 90)
    q = Polygon(3, 90)
    r = Polygon(4, 90)
    print(p.edges)
    print(p.circumradius)
    print(p.interiorAngle)
    print(p.edgeLength)
    print(p.apothem)
    print(p.area)
    print(p.perimeter)
    print(repr(p)) 
    print(p == q) 
    print(p == r) 
    print(r > p) 
    print(p > r)
    print(p < r)