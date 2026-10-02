from math import sin, cos, pi



class Vector2:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.components = [x, y]

        self.module = (x**2+y**2)**(1/2)


    def __getitem__(self, index):

        return(self.components[index])


    def __str__(self):

        string = "(" + str(self.x) + " " +  str(self.y) + ")"

        return(string)


    def __eq__(self, other):
        
        if self.components == other.components:
            return(True)

        else:
            return(False)

    
    def __add__(self, other):
        
        result = Vector2(self[0]+other[0], self[1]+other[1])
        return(result)


    def __sub__(self, other):

        result = Vector2(self[0]-other[0], self[1]-other[1])
        return(result)

    
    def __mul__(self, other):

        if type(other) == Vector2:
            result = self[0]*other[0] + self[1]*other[1]
            return(result)

        elif type(other) == Matrix:
            result_x = self*other[-1, 0]
            result_y = self*other[-1, 1]
            result = Vector2(result_x, result_y)
            return(result)

        else:
            result = Vector2(self.x*other, self.y*other)
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


    def __str__(self):

        string = "(" + str(self.x) + " " +  str(self.y) + " " + str(self.z) + ")"

        return(string)
    

    def __eq__(self, other):

        if self.components == other.components:
            return(True)

        else:
            return(False)

    
    def __add__(self, other):
        
        result = Vector3(self[0]+other[0], self[1]+other[1], self[2]+other[2])
        return(result)


    def __sub__(self, other):

        result = Vector3(self[0]-other[0], self[1]-other[1], self[2]-other[2])
        return(result)

    
    def __mul__(self, other):

        if type(other) == Vector3 or type(other) == VectorN:
            result = self[0]*other[0] + self[1]*other[1] + self[2]*other[2]
            return(result)

        elif type(other) == Matrix:
            result_x = self*other[-1, 0]
            result_y = self*other[-1, 1]
            result_z = self*other[-1, 2]
            result = Vector3(result_x, result_y, result_z)
            return(result)

        else:
            result = Vector3(self.x*other, self.y*other, self.z*other)
            return(result)


    def __truediv__(self, other):

        result = Vector3(self.x/other, self.y/other, self.z/other)
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


    def __str__(self):

        string = "("
        for i in range(self.size-1):
            string = string + str(self.components[i]) + " "
        string = string + str(self.components(self.size-1)) + ")"

        return(string)

    

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

        elif type(other) == Matrix:
            result_components = []
            for i in range(self.size):
                result_components.append(self*Matrix[-1, i])
            result = VectorN(result_components)
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


    @staticmethod
    def rotation_3D(coordinate, angle):

        angle = (angle*2*pi)/360

        if coordinate == "x":
            result = Matrix([[1, 0         , 0          ],
                             [0, cos(angle), -sin(angle)],
                             [0, sin(angle), cos(angle) ]])

        elif coordinate == "y":
            result = Matrix([[cos(angle) , 0, sin(angle)],
                             [0          , 1, 0         ],
                             [-sin(angle), 0, cos(angle)]])

        else:
            result = Matrix([[cos(angle), -sin(angle), 0],
                             [sin(angle), cos(angle) , 0],
                             [0         , 0          , 1]])

        return(result)
    


x_unit_2D = Vector2(1, 0)
y_unit_2D = Vector2(0, 1)

x_unit_3D = Vector3(1, 0, 0)
y_unit_3D = Vector3(0, 1, 0)
z_unit_3D = Vector3(0, 0, 1)
