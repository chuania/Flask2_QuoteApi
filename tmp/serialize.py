from author import Author
from schema import AuthorSchema

author = Author(1, "Alex", "alex5@mail.ru")
author_schema = AuthorSchema()
result = author_schema.dump(author)
print(result)

authors = [Author("1", "Alex"), Author("1", "Ivan"), Author("1", "Tom")]
authors_schema = AuthorSchema(many=True)
res = authors_schema.dump(authors)
print(res)
