import pymongo

client_cloud = pymongo.MongoClient('mongodb+srv://mongopass:mongopass@mymongocluster0.50qf7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
client_db1 = client_cloud['mydb']


client_cloud.list_database_names()

# adding collection
collection = client_db1["company"]

record = {
    "companyName" :"ineuron",
    "product" :"visual detector",
    "courses_offered":['data science', 'statistics']
}
collection.insert_one(record)

record = {
    "companyName" :"tocco",
    "product" :"plotly",
    "courses_offered":['mathematics', 'artificial intelligence'],
    "rating": 5.3,
    "contact":{
            "email":'tocco@gmail.com',
            'phone no ': 242394283840242
            }
}
collection.insert_one(record)


st_collection.insert_one({
     "name" : "thomas",
     "major" : "Data science" ,
     "phone_number": 9562348638,
     "gpa" : 9.12
     })
st_collection.insert_one({
    "name":"CLaire",
    "major" : "Machine learning",
    "gpa" : 9.49
})

st_collection.insert_one({
    "name" : 'Maria',
    "gpa" : 8.43,
    "awards" : ["hackathone", "basel jhons", "summa cum laude"],
})
st_collection.insert_one({ "_id" : 4,
    "name" : 'martin',  "gpa" : 9.45,
    "email" : "marting23@gmail.com",
    "marks": [23,1,2,13,324,53]
})
st_collection.insert_one({
    "name":"Antony",
    "major" : "Analytics",
    "gpa" : 8.49,
    "awards" : ["hackathone","Summa cum laude"]
})
st_collection.insert_one({
    "name":"Kate",
    "major" : "Sociology",
    "gpa" : 8.49,
    "contact" :{"phone":"9562348628", "email":"kateste123@gmail.com"},

})
st_collection.insert_one({
    "name" : "phill",
    "age" :23,
    "gpa" : 8.53,
    "startdate" : "2021-08-12"
})
st_collection.insert_many([
    {"name":"able", "major": "mathematics", "gpa" : 4.5},
    {"name": "andrea", "major" : "Statistics", "gpa" : 8.9, "contact" : {"email": "andreath@gmail.com"}}
])

# quering
st_collection.find_one()

collection.find_one()

for i in collection.find():
    print(i )

for i in collection.find({"companyName":'ineuron'}):
    print(i)

list(collection.find({'companyName':'ineuron'}))

#finding students with gpa greater than gpa 9
list(st_collection.find({"gpa": {"$gt" :9 }},{"_id":0}))

delete_query = {'name':'CLaire'}
st_collection.delete_one(delete_query)

multi_deletes = {"gpa": {"$gt" :9 }}
st_collection.delete_many(multi_deletes)

# trying to get the students with gpa greater than gpa 9
# wont get any result
list(st_collection.find({"gpa": {"$gt" :9 }},{"_id":0}))

st_collection.find_one()

# enumerate all the documents in student collection
all_st_docs = st_collection.find()
for idx,document in enumerate(all_st_docs):
    print(f"{document}\n")

# here the collection name refers to the company collection
collection.drop()

# now we have only student collection in the mydb database

# verifying the collection
collection_name = 'student'
db_name = 'mydb'
client_db1.list_collection_names()



present_data = {'name':'able'}
new_data = {"$set":{'name':'Thomaskutty reji'}}
st_collection.update(present_data, new_data)

# enumerate all the documents again in student collection
# can see that the name "able" is changed to "Thomaskutty reji"
all_st_docs = st_collection.find()
for idx,document in enumerate(all_st_docs):
    print(f"{document}\n")





