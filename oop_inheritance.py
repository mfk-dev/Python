print("---" * 10)

# Base Class
class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def code(self):
        print(f"{self.name}, is coding in {self.language} language.")

# Child Class inheriting from Developer ( Base Class )
class NASADeveloper(Developer):
    def __init__(self, name, language, project):
        super().__init__(name, language)
        self.project = project

    def launch_rocket(self):
            print(f"{self.name}, is launching the rocket for the project {self.project}!")

nasa_dev = NASADeveloper("MFK", "Python", "Artemis")
nasa_dev.code()
nasa_dev.launch_rocket()
