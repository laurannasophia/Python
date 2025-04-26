# Tehtävä 2.1
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]

letter = input("Syötä kirjain ")
if letter in alphabet:                                                                                 # Tarkastaa löytyykö syötetty kirjain aakkosista
    print("Syöttämäsi kirjaimen sijainti aakkosissa on " + str(alphabet.index(letter) + 1) + ". sija") # Etsii syötetyn kirjaimen sijainnin listasta ja lisää siihen yhden sijan
else:
    print("Et syöttänyt kirjainta")