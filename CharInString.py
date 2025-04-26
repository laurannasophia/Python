#Tehtävä 2.3

string = input("Anna syöte ")

count = 0
list = []
for i in string:
    if(i not in list):
        count += 1
        list.append(i)
print("Syötteessäsi on " + str(count) + " erilaista merkkiä")

count = {}
for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for l, x in count.items():
    print("Kirjain " + str(l) + " esiintyy syötteessäsi " + str(x) + " kertaa.")