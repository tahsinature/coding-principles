# Good example following LSP

class Rectangle:
  def __init__(self, width, height):
    self._width = width
    self._height = height

  def get_width(self):
    return self._width

  def get_height(self):
    return self._height

  def set_width(self, width):
    self._width = width

  def set_height(self, height):
    self._height = height

  def area(self):
    return self._width * self._height


class Square(Rectangle):
  def set_width(self, width):
    self._width = width
    self._height = width

  def set_height(self, height):
    self._height = height
    self._width = height

  # Additional methods specific to Square, but do not override behavior of Rectangle
  def set_side(self, side):
    self._width = side
    self._height = side

  def get_side(self):
    return self._width  # or self._height, as they are always the same
