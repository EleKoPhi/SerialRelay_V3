class program:
    ID = None
    Name = None
    Type = None
    ProgramDefinition = None
    event = None

    def __init__(self, definition):
        self.ID = definition["ID"]
        self.Name = definition["name"]
        self.event = definition["event"]
        self.ProgramDefinition = definition["definition"]
