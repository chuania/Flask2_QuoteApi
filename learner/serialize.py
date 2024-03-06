from learner import Learner
from schema import LearnerSchema
from random import choice
from pprint import pprint


learner = Learner(name='Vlad', id=10, final_test=True)
learner_schema = LearnerSchema()
result = learner_schema.dump(learner)
print(result)

learners = [
   Learner("1", "Alex", False),
   Learner("1", "Ivan", True),
   Learner("1", "Tom", True)
]
learners_schema = LearnerSchema(many=True)
res = learners_schema.dump(learners)
print(res)


# Реализация проверки типов через pattern matching
print('==== CHECK ONE ====')
data = choice([learners, learner])
match type(data):
    case s if s is Learner:
        learner_schema = LearnerSchema()
        result = learner_schema.dump(data)
        print(result)
    case s if s is list:
        schemas = LearnerSchema(many=True)
        res = schemas.dump(data)
        pprint(res)

print('==== CHECK TWO ====')
data = choice([learners, learner])
match data:
    case Learner():
        learner_schema = LearnerSchema()
        result = learner_schema.dump(data)
        print(result)
    case list():
        schemas = LearnerSchema(many=True)
        res = schemas.dump(data)
        pprint(res)