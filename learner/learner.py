class Learner:
    def __init__(self, id, name, final_test):
        self.id = id
        self.name = name
        self.final_test = final_test

    def __repr__(self):
       return f"Learner({self.id}): {self.name}|{self.final_test}"
