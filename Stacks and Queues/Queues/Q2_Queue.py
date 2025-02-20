class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []


    def enqueue(self,animal,type):
        if type == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats):
            cat = self.cats.pop(0)
        else:
            return None
        return cat

    def dequeueDog(self):
        if len(self.dogs):
            dog = self.dogs.pop(0)
        else:
            return None
        return dog
    
    def dequeueAny(self):
        if len(self.cats):
            pass
