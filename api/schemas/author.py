from api import ma
from api.models.author import AuthorModel
from api.models.quote import QuoteModel


# схема создается автоматически на основе моделии автора,
# такая схема не всегда подходит
class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuthorModel


# для единичного экземпляра
author_schema = AuthorSchema()
# для списка экземпляров
authors_schema = AuthorSchema(many=True)