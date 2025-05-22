def broji_samoglasnike(ime):
    samoglasnici = "aeiouAEIOU"
    broj_samoglasnika = 0
    for slovo in ime:
        if slovo in samoglasnici:
            broj_samoglasnika += 1
    return broj_samoglasnika

while True:
    ime = input("Unesite ime kupca (ili pritisnite Enter da zavrÅ¡ite): ")
    
    if ime == "":
        break
    
    broj_samoglasnika = broji_samoglasnike(ime)
    
    if broj_samoglasnika == 0:
        print("Ime nema samoglasnike, program se zavrsava.")
        break
    print(f"Ime {ime} sadrzi {broj_samoglasnika} samoglasnika!")
    