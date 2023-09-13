import asyncio

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from author_model import Author


async def example():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.db_name, document_models=[Author])
    author = await Author(name="J. R. R. Tolkien", books=['book1', 'book2']).insert()
    print(author)
    updated = await author.update({"$set": {"books": ["book3", "book4"], "name": "J. R. R. Tolkien2"}})
    print(updated)


if __name__ == '__main__':
    asyncio.run(example())
