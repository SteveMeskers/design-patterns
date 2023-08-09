# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too
from abc import ABC
class Renderer(ABC):
    @property
    def what_to_render_as(self, name):
        return None
        
# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
class Shape:
    def __init__(self, name, renderer):
        self.name = name
        self.renderer = renderer
        
class Square(Shape):
    def __init__(self, renderer):
        super().__init__('Square', renderer)
        
    def __str__(self):
        return "Drawing {} as {}".format(self.name, self.renderer.what_to_render_as)
        
class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__('Triangle', renderer)
        
    def __str__(self):
        return "Drawing {} as {}".format(self.name, self.renderer.what_to_render_as)
        
class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "lines"
        
class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "pixels"
    