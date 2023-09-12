from employee import Employee

class Developer(Employee) :

    def __init__(self, firstname, lastname, age, job = "Developer", salary = 15000):
        super().__init__(firstname, lastname, age, job, salary)
        self.coding_skills = []

    def add_skills(self, *skills) :
        self.coding_skills.extend(skills)
    
    def coding(self) :
        print(f"{super().get_fullname()} coding skills are {','.join(self.coding_skills)}")

    def coding_with_partner(self, other_developer) :
        print("Developers are working together")
        self.coding() #like doing first_dev.coding()
        other_developer.coding() #like doing second_dev.coding()

    def get_promotion(self, new_promotion) :
        self.salary *= new_promotion

first_dev = Developer("Tom", "Cruize", 30)
first_dev.add_skills("Javascript", "Python", "React")
# first_dev.coding()

second_dev = Developer("Angelina", "Jolie", 20)
second_dev.add_skills("Javascript", "Python", "React")

first_dev.coding_with_partner(second_dev)

first_dev.get_promotion(1.2)
first_dev.show_info()