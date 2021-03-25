from flask import *
import pymongo
from pymongo import MongoClient


import random

cluster = 'mongodb+srv://ajaykumaar:ajay@cluster0.07d2o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app=Flask(__name__)
client = pymongo.MongoClient(cluster) 

Database = client.get_database('tacti') 
table = Database.ran_list
#aList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
#sampled_list = random.sample(aList, 5)

@app.route('/')
def home():
    aList = ["ajay", "bharat", "cathy", "david", "elizabeth", "fabiana", "gayathri", "hari", "ishwarya", "janani", "kesavaraj", "lajay", "mithra", "nivi", "orange", "preethi", "queeny", "reshma", "sneha", "t"]
    list1 = random.sample(aList, int(len(aList)/2))
    list2 = [i for i in aList if i not in list1]
    table.remove( { } );
    for i in range(len(list1)):
        table.insert_one({"person1":list1[i], "person2":list2[i] })
    meet_l = table.find()
    
    return render_template('home.html',meet_l=meet_l)
if __name__ == "__main__":
    app.run(debug=True)