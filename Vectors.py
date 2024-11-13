class Vector2:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.components = [x, y]

        self.module = (x**2+y**2)**(1/2)


    def __getitem__(self, index):

        return(self.components[index])


    def __eq__(self, other):
        
        if self.components == other.components:
            return(True)

        else:
            return(False)

    
    def __add__(self, other):
        
        result = Vector2(self.x+other.x, self.y+other.y)
        return(result)


    def __sub__(self, other):

        result = Vector2(self.x-other.x, self.y-other.y)
        return(result)

    
    def __mul__(self, other):

        if type(other) == Vector2:
            result = self.x*other.x + self.y*other.y
            return(result)

        else:
            result = Vector2(self.x*other.x, self.y*other.y)
            return(result)


    def __truediv__(self, other):

        result = Vector2(self.x/other, self.y/other)
        return(result)

    
    def unit(self):

        result = self / self.module
        return(result)



class Vector3:

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

        self.components = [x, y, z]

        self.module = (x**2+y**2+z**2)**(1/2)


    def __getitem__(self, index):

        return(self.components[index])
    

    def __eq__(self, other):

        if self.components == other.components:
            return(True)

        else:
            return(False)

    
    def __add__(self, other):
        
        result = Vector3(self.x+other.x, self.y+other.y, self.z+other.z)
        return(result)


    def __sub__(self, other):

        result = Vector3(self.x-other.x, self.y-other.y, self.z-other.z)
        return(result)

    
    def __mul__(self, other):

        if type(other) == Vector2:
            result = self.x*other.x + self.y*other.y + self.z*other.z
            return(result)

        else:
            result = Vector2(self.x*other, self.y*other, self.z*other)
            return(result)


    def __truediv__(self, other):

        result = Vector2(self.x/other, self.y/other, self.z/other)
        return(result)

    
    def unit(self):

        result = self / self.module
        return(result)



class VectorN:

    def __init__(self, *components):

        self.components = components[0]

        self.module = 0
        for component in self.components:
            self.module = self.module + component**2
        self.module = self.module**(1/2)

        self.size = len(self.components)

    def __getitem__(self, index):

        return(self.components[index])
    

    def __eq__(self, other):

        if self.components == other.components:
            return(True)

        else:
            return(False)

    
    def __add__(self, other):
        
        result = []
        for i in range(self.size):
            result.append(self[i] + other[i])
        return(VectorN(result))


    def __sub__(self, other):

        result = []
        for i in range(self.size):
            result.append(self[i] - other[i])
        return(VectorN(result))

    
    def __mul__(self, other):

        if type(other) == VectorN:
            result = 0
            for i in range(self.size):
                result = result + self[i] * other[i]
            return(result)

        else:
            result = []
            for i in range(self.size):
                result.append(self[i] * other)
            return(VectorN(result))


    def __truediv__(self, other):

        result = []
        for i in range(self.size):
            result.append(self[i] / other)
        return(VectorN(result))

    
    def unit(self):

        result = self / self.module
        return(result)



class Matrix:

    def __init__(self, matrix):

        self.matrix = matrix
        self.size = Vector2(len(self.matrix), len(self.matrix[0]))


    def __getitem__(self, index):

        if index[0] == -1:
            item = []
            for y in range(self.size[0]):
                item.append(self.matrix[y][index[1]])
            item = VectorN(item)

        elif index[1] == -1:
            item = self.matrix[index[0]]
            item = VectorN(item)

        else:
            item = self.matrix[index[0]][index[1]]
            
        return(item)
    

    def __str__(self):

        string = ""
        for y in range(self.size[0]):

            new_line = "("

            for x in range(self.size[1]-1):
                new_line = new_line + str(self[y, x]) + " "
            new_line = new_line + str(self[y, self.size[1]-1]) + ")\n"

            string = string + new_line

        return(string)


    def __add__(self, other):

        result = []

        for y in range(self.size[0]):
            result.append([])
            for x in range(self.size[1]):
                result[y].append(self[y, x] + other[y, x])

        return(Matrix(result))
    

    def __sub__(self, other):

        result = []

        for y in range(self.size[0]):
            result.append([])
            for x in range(self.size[1]):
                result[y].append(self[y, x] - other[y, x])

        return(Matrix(result))


    def __mul__(self, other):
        
        result = []

        for y in range(self.size[0]):
            result.append([])
            for x in range(other.size[1]):
                result[y].append(self[y, -1] * other[-1, x])

        return(Matrix(result))


a=Matrix([[1,2,3,4],
          [5,6,7,8],
          [9,0,1,2]])

b=Matrix([[0,9,8],
          [6,5,4],
          [2,1,0],
          [1,2,3]])


print(a)
print(b)

print(a*b)
