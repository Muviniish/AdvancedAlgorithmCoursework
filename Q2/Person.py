class Person:
    def __init__(self, name, privacy, biography):
        self.name = name
        self.privacy = privacy
        self.biography = biography

    def __str__(self):
        return f"Person (Name: {self.name}, privacy: {self.privacy}, biography: {self.biography})"
    
    def getName(self):
        return self.name
    
    def getPrivacy(self):
        return self.privacy
    
    def getBiography(self):
        return self.biography