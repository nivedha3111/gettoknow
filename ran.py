from flask import *
import pymongo
from pymongo import MongoClient
import datetime
from datetime import date

import random

global today
today= ''

cluster = 'mongodb+srv://ajaykumaar:ajay@cluster0.07d2o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app=Flask(__name__)
client = pymongo.MongoClient(cluster) 

Database = client.get_database('tacti') 
table = Database.ran_list
#aList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
#sampled_list = random.sample(aList, 5)
def get_list():
    aList = ["ajay", "bharat", "cathy", "david", "elizabeth", "fabiana", "gayathri", "hari", "ishwarya", "janani", "kesavaraj", "lajay", "mithra", "nivi", "orange", "preethi", "queeny", "reshma", "sneha"]
    list1 = random.sample(aList, int(len(aList)/2))
    list2 = [i for i in aList if i not in list1]
    return list1, list2

def check(prev_list,list1,list2):
    old_list1, old_list2=[],[]
    for l in prev_list:
        old_list1.append(l['person1'])
        old_list2.append(l['person2'])

    for p1 in list1:
        new_id= list1.index(p1)
        if p1 in old_list1:
            old_id=old_list1.index(p1)
            old_p=old_list2[old_id]
            if old_p == list2[new_id]:
                return 1






@app.route('/')
def home():
    global today
    #today =''
    t=str(date.today())
    if t != today:
        today = t
        print(t)
        print(today)
        list1, list2= get_list()  
    else:
        prev_list = table.find()
        list1, list2=[],[]
        for l in prev_list:
            list1.append(l['person1'])
            list2.append(l['person2'])
    
    prev_list = table.find()
    table.remove( { } );
    repeat=check(prev_list,list1,list2)
    if repeat == 1 :
        list1,list2=get_list()
    #print(prev_list)
    #table.remove( { } );
    for i in range(len(list1)):
        table.insert_one({"person1":list1[i], "person2":list2[i] })
    meet_l = table.find()
    
    return render_template('home.html',meet_l=meet_l)
if __name__ == "__main__":
    app.run(debug=True)