# Base Class
class Rover:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def status_report(self):
        print(f"{self.name} has {self.energy} energy remaining.")

# Child Class
class MarsRover(Rover):
    def __init__(self, name, energy, mission, camera_number, time_of_photo):
        super().__init__(name, energy)
        self.__mission = mission 
        self.camera_number = camera_number
        self.time_of_photo = time_of_photo

    def take_photo(self):
        if self.energy >= 10:
            with open("photo_log.txt", "a") as log_file:
                log_file.write(f"{self.name} takes a photo with camera {self.camera_number} at time {self.time_of_photo}.\n")
                self.energy -= 10
        else: 
            print(f"{self.name} has 0 energy remained, mission failed.")

mars_rover = MarsRover("Curiosity", 100, "Confidential", 1, "2024-06-01 12:00:00")
mars_rover.status_report()
mars_rover.take_photo()
mars_rover.status_report()
