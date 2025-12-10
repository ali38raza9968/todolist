dictionary [ key : value]
dict = {
    "name" : "md ali",
    "age" : 24,
    "marks" : 23.2,
    "grade" : ("a","b","c"),
    "subject" : ["sci","math","sst"]
}
print(dict)
dict["age"] = 32 isse age ka value change hojayega
print(dict["name"])
print(dict["subject"])
dict["surname"] = "shaikh" - isse naya key value add hojayegs
print(dict)
dict = {}
dict["name"] = "md ali"
print(dict)
NESTED DICTIONARY
student = {
    "name" : "ali",
    "marks" : {
        "math" : 34,
        "sci" : 25,
        "eng" : 98
    }
}
print(student["marks"])
print(student["marks"]["math"])
print(student)

DICTIONARY METHOD
student = {
    "name" : " samiullah",
    "subject" : {
        "phy" : 97,
        "sci" : 48,
        "math" : 43 
    }
}
print(list(student.keys())) # 1 isse key print hojayega
print(len(student))
print(list(student.values())) #2 pura value print hojayega
print(student.items()) # 3 isse key or value dono print hoga
pairs = list(student.items())
print(pairs[0])
print(student.get("subject"))#4 retur the key according to value/
new_dict = {"city": "delhi"}
student.update(new_dict)
student["city"] = "shaikh"
print(student)

set
collection = {1,2,3,"hello","world"}
print(collection)
null_set = set() # empty set
METHOD OF set
collection = set()
collection.add(1) #1
collection.add(2)
collection.add(3)
collection.add("world")
collection.add(2)
collection.remove("world") #2
collection.clear()#3
collection.pop() #4
print(len(collection))
set union.
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1.union(set2)
print(set3)
set intersection
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1.intersection(set2)
print(set3)
PRACTICE QUESTION
 Q1
dict = {}
dict["table"] = "a peace of furniture","list of facts and figures"
dict["cat"] = "a small animal"
print(dict)
Q2
subject = {
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print("total number of classes needed for study is :",len(subject))
q3
dict = {}
subject1 = input("enter 1st subject")
dict.update({subject1 : 20})
subject2 = input("enter your second subject")
dict.update({subject2 : 28})
subject3 = input("enter 3rd subject")
dict.update({subject3 : 40})
print(dict)
Q4
set = {
    ("float", 9.0),
    ("int",9)
}
print(set)


