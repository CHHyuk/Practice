class person():
    def __init__(self,):
        self.folder = []

    def add_files(self,file):
        self.folder.append(file)

jin = person()
jin.add_files('txt')

paul = person()
paul.add_files('img')

print(jin.folder)
print(paul.folder)