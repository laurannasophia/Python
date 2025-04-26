#Tehtävä 2.4
string = input("Syötä sana, niin tarkistetaan onko se palindromi ")
length = len(string)
first = 0
last = length - 1

while first < last:
    if string[first]!=string[last]:
        print("Sana ei ole palindromi")
        break
    else:
        print("Sana on palindromi")
        break