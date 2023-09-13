from beanie import Document


class Author(Document):
	name: str
	books: list[str] = []