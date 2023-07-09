class Rectangle:
  def __init__(self, w, h):
    self.w = w
    self.h = h

  def set_width(self, w):
    self.w = w

  def set_height(self, h):
    self.h = h
  
  def get_area(self):
    return self.w * self.h
 
  def get_perimeter(self):
    return 2 * (self.w + self.h)

  def get_diagonal(self):
    return (self.w ** 2 + self.h ** 2) ** .5

  def get_picture(self):
    pic = ''
    if self.h > 50 or self.w > 50:
      return "Too big for picture."
    for i in range(self.h):
      for j in range(self.w):
        pic += "*"
      pic += "\n"
    return pic

  def __str__(self):
    return f"Rectangle(width={self.w}, height={self.h})"

  def get_amount_inside(self, other):
    return (self.h // other.h) * (self.w // other.w)

class Square(Rectangle):
  def __init__(self, s):
    self.h = s
    self.w = s

  def set_side(self, s):
    self.h = s
    self.w = s

  def __str__(self):
    return f"Square(side={self.h})"

  def set_width(self, s):
    self.h = s
    self.w = s

  def set_height(self, s):
    self.h = s
    self.w = s
