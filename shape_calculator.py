class Rectangle:

    def __init__(self,width,height): self.width,self.height = width,height
    def set_width(self,new_width): self.width = new_width
    def set_height(self,new_height): self.height = new_height
    def get_area(self): return self.width * self.height
    def get_perimeter(self): return 2 * (self.width + self.height)
    def get_diagonal(self): return (self.width**2 + self.height**2)**.5
    def __str__(self): return f"Rectangle(width={self.width}, height={self.height})"
    def get_amount_inside(self,shape): return self.get_area() // shape.get_area()
    def get_picture(self): return ("Too big for picture." if self.width > 50 or 
                  self.height > 50 else ("*" * self.width + "\n") * self.height)

class Square(Rectangle):

    def __init__(self,side): super().__init__(side,side)
    def set_side(self,sq_side): self.width = self.height = sq_side
    def __str__(self): return f"Square(side={self.width})"
