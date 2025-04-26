#Tehtävä 2.2 

string = input("Anna syöte ")

count = 0
list = []
for i in string:
    if(i not in list):
        count += 1
        list.append(i)
print("Syötteessäsi on " + str(count) + " erilaista merkkiä")