mylist = ["Funie", "Tapiwa", "Denis"]
print(mylist[1])
print(len(mylist))

mylist = ["Funie", "Tapiwa", "Denis"]
mylist[1] = ("Simba")
print(mylist)

mylist = ["Funie", "Tapiwa", "Denis"]
print(mylist[1:]) 

thislist = (mylist[1:]) 
print(thislist)

thislist = (mylist[1:]) 
thislist.append("Kanye")
thislist.append("Tawonga")
print(thislist)

thislist = (mylist[1:])
thislist.insert(0, "Tatenda")
print(thislist)

mylist = ["Funie", "Tapiwa", "Denis"]
thislist =["Tapiwa", "Denis", "Kanye", "Tawonga"]
mylist.extend(thislist)
print(mylist)