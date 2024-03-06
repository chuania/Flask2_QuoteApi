from marshmallow import Schema, fields, validate

class LearnerSchema(Schema):
   id = fields.Integer(primary_key=True)
   name = fields.Str(
      required=True,
      error_messages={
         'required': {
               'message': 'name is required', 
               'code': 400
         }
      },
      validate=[validate.Length(max=50)]
      )
   final_test = fields.Boolean()
   