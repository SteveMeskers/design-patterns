class CodeBuilder:
    def __init__(self, root_name):
        self.class_name = root_name
        self.members = []

    def add_field(self, type, name):
        self.members.append((type, name))
        return self

    def __str__(self):
        lines = []
        lines.append('class {}:'.format(self.class_name))
        if len(self.members) == 0:
            lines.append('  pass')
            return '\n'.join(lines)
            
        lines.append('  def __init__(self):')
        for m in self.members:
            lines.append('    self.{} = {}'.format(m[0], m[1]))
            
        return '\n'.join(lines)
