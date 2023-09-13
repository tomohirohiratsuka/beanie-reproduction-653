# Step to reproduce
1. Install the dependencies
    ```bash
    poetry install
    ```
2. Start mongodb server
    ```bash
    docker-compose up
    ```
3. Go to shell
    ```bash
    poetry shell
    ```
4. Run the script
    ```bash
    (poetry) python main.py
    ```
   
# Sample Log
If you don't change any script in main.py you can see the following log which show list is not merged.
```
id=ObjectId('650186046286ed1ead775446') revision_id=None name='J. R. R. Tolkien' books=['book1', 'book2']
id=ObjectId('650186046286ed1ead775446') revision_id=None name='J. R. R. Tolkien2' books=['book1', 'book2']
```