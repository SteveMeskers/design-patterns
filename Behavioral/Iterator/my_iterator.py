class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if left:
      self.left.parent = self
    if right:
      self.right.parent = self

  def traverse_preorder(self):
    yield self.value

    if self.left is not None:
        yield from self.left.traverse_preorder()

    if self.right is not None:
        yield from self.right.traverse_preorder()
