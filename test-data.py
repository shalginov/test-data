import csv
import os.path
import json

PATH_DIR = os.path.dirname(__file__)

PATH_BOOK_CSV = os.path.join(PATH_DIR, "books.csv")
PATH_USER_JSON = os.path.join(PATH_DIR, "users.json")
PATH_RESULT_JSON = os.path.join(PATH_DIR, "result.json")

bc = open(PATH_BOOK_CSV, "r", newline="")
books_reader = csv.reader(bc)
header = next(books_reader)
header.remove("Publisher")

users = []
with open(PATH_USER_JSON, "r") as f:
    users_load = json.load(f)
    users = [ dict(
        name = u["name"],
        gender = u["gender"],
        address = u["address"],
        age = u["age"],
        books = []
    ) for u in users_load]

user_index = 0
for book in books_reader:
    users[user_index]["books"].append(dict(zip(header, book)))
    user_index += 1
    if user_index >= len(users):
        user_index = 0

bc.close()

with open(PATH_RESULT_JSON, "w") as f:
    json.dump(users, f, indent=4)
