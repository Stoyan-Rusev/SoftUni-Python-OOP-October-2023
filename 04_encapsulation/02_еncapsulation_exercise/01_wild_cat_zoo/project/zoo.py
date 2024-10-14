from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for current_worker in self.workers:
            if current_worker.name == worker_name:
                self.workers.remove(current_worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animal_cost = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_animal_cost:
            self.__budget -= total_animal_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]

        lions = [animal for animal in self.animals if animal.__class__.__name__ == 'Lion']
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah']

        result.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            result.append(lion.__repr__())

        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(tiger.__repr__())

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            result.append(cheetah.__repr__())

        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        vets = [worker for worker in self.workers if worker.__class__.__name__ == 'Vet']

        result.append(f"----- {len(keepers)} Keepers:")
        for keeper in keepers:
            result.append(keeper.__repr__())

        result.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            result.append(caretaker.__repr__())

        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(vet.__repr__())

        return "\n".join(result)
