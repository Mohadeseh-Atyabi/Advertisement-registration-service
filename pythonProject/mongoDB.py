import pymongo
from pymongo.server_api import ServerApi
from pymongo import errors
import random


class MongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://mohadeseh:9726004@cluster0.ynzhpkm.mongodb.net/?retryWrites=true&w=majority",
            server_api=ServerApi('1'))
        self.db = self.client["HW1"]
        self.coll = self.db["hw1"]
        self._id = 0

    def insert(self, email, description):
        self._id = str(random.randint(0, 10000))
        while self.coll.count_documents({"_id": self._id}) > 0:
            # print(self._id)
            self._id = str(random.randint(0, 10000))

        try:
            self.coll.insert_one({
                "_id": self._id,
                "email": email,
                "description": description,
                "state": "Pending",
                "category": ""
            })
            return self._id
        except errors.DuplicateKeyError:
            self.insert(email, description)

    def update(self, id, state, category):
        self.coll.update_one({"_id": id}, {
            "$set": {"state": state, "category": category}
        })

    def show(self, id):
        return self.coll.find_one({"_id": id})
