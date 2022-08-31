class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self,width):
        self.width = width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        return (self.height * self.width)
    def get_perimeter(self):
        return (2*self.width + 2*self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height**2)**0.5)
    def get_picture(self):
        line = ""
        if self.width < 50 and self.height < 50:
            for i in range(self.height):
                for j in range(self.width):
                    line += "*"
                line += "\n"
            return line
        else:
            return "Too big for picture."
    def get_amount_inside(self,shape):
        horizontally = self.width//shape.width
        vertically = self.height//shape.height
        answer = horizontally * vertically
        return answer
class Square(Rectangle):
    def __init__(self,length):
        self.width = length
        self.height = length
    def __repr__(self):
        return f"Square(side={self.width})"
    def set_side(self,length):
        self.width = length
        self.height = length
rect = Rectangle(10,5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
rect.set_height(8)
rect.set_height(16)
print(rect.get_amount_inside(sq))