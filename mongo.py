from pymongo import MongoClient
import json
conn = MongoClient("mongodb://localhost:27017/")
print("connected successfully")

db=conn["college"]
col=db["studlist"]

print("Database and collection created")

with open("test.json") as file:
    data=json.load(file)
#col.insert_many(data)
print("data inserted")

#for doc in col.find({"gender":"female","course":"MCA"},{"name":1,"mark":1,"_id":1}):
#   print("Name ",doc["name"]["fname"],doc["name"]["lname"],"| Mark",doc["mark"])

# for doc in col.find({"course": "Mechanical"}).sort("mark", -1).limit(3):
#     print(doc["name"]["fname"],doc["name"]["lname"])

# for i in col.find({"gender":"male","grade":"A+"},{"name":1,"grade":1}):
#     print(i["name"]["fname"],i["name"]["lname"],"-",i["grade"])

for i in col.find({"mark":{"$gt":90}},{"name":1,"_id":0,"grade":1}):
    print(i["name"]["fname"],i["name"]["lname"],"- grade",i["grade"])
    