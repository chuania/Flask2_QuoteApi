from learner import Learner
from schema import LearnerSchema
from pprint import pprint

json_data = """
[
   {
       "id": 1,
       "name": "Alex",
       "final_test": false
   },
   {
       "id": 2,
       "name": "Ivan",
       "final_test": true
    },
   {
       "id": 4,
       "name": "Tom",
       "final_test": true
   }
]
"""


schema = LearnerSchema(many=True)
result = schema.loads(json_data)
pprint(result)