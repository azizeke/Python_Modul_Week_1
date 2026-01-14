vraa1: liste = []

for i in range(3):
    movie = input(f"{i+1}. favori filmi girin: ")
    liste.append(movie)

print("Full liste:", liste)
print("İlk film:", liste[0])
print("Son film:", liste[-1])



# Vraag2: Age Check



jaar = int(input("Kunt u uw jaar invullen: "))

if jaar < 18:
    print("U bent geen volwassene.")
else:
    print("U bent een volwassene")

# Vraag naar je geboortejaar en bereken je leeftijd
geboorte_datum = int(input("Voer je geboortejaar in: "))
bereken_leeftijd = 2025 - geboorte_datum

print("U leeftijd in 2025 is:", bereken_leeftijd)



# Vraag3:Word Analysis Tool

zin= input("Voer alstublieft een zin in")

# Aantal tekens
aantal_tekens= len(zin.replace(" ", ""))

woorden= zin.split()
aantal_woorden= len(woorden)

# unieke woorden
unieke_woord= set(woorden)

# Laangste woord vinden
langste_woord= max(woorden, key=len)


print("Aantal tekens (zonder spaties):", aantal_tekens)
print("Aantal woorden:", aantal_woorden)
print("Unieke woorden:", unieke_woord)
print("Langste woord:", langste_woord)



# Vraag4: Mini Market Basket

products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}

basket = []
total_price = 0

for i in range(3):
    product = input(f"{i+1}. ürünü girin: ").lower()

    if product in products:
        basket.append(product)
        total_price += products[product]
    else:
        print(f"Uyarı: '{product}' ürünü mevcut değil!")

print("Your basket:", ", ".join(basket))
print("Total price:", total_price, "TL")



# Vraag5: Student Gradding System


students = {
    "Ali": [80, 90, 70],
    "Ayşe": [85, 75, 95],
    "Mehmet": [60, 70, 65]
}

en_yuksek_ort = 0
top_student = ""

for isim, notlar in students.items():
    ortalama = sum(notlar) / len(notlar)
    print(f"{isim} ortalama: {ortalama:.2f}")

    if ortalama > en_yuksek_ort:
        en_yuksek_ort = ortalama
        top_student = isim

print(f"\nEn yüksek ortalamaya sahip öğrenci: {top_student} ({en_yuksek_ort:.2f})")



# Vraag6: Mini Library Management System


library = {
    "python101": "Available",
    "datascience": "Available",
    "algorithms": "Available"
}

borrowed = set()

while True:
    print("\n1- Add Book")
    print("2- Borrow Book")
    print("3- Return Book")
    print("4- View All Books")
    print("5- Exit")

    choice = input("Choice: ")

    if choice == "1":
        book = input("Book name: ").lower()
        if book in library:
            print("Book already exists!")
        else:
            library[book] = "Available"

    elif choice == "2":
        book = input("Book name: ").lower()
        if book in library and library[book] == "Available":
            library[book] = "Borrowed"
            borrowed.add(book)
        else:
            print("Book not available!")

    elif choice == "3":
        book = input("Book name: ").lower()
        if book in borrowed:
            library[book] = "Available"
            borrowed.remove(book)
        else:
            print("This book was not borrowed!")

    elif choice == "4":
        for book, status in library.items():
            print(book, "-", status)
        print("Total books:", len(library))
        print("Borrowed books:", len(borrowed))

    elif choice == "5":
        break

    else:
        print("Invalid choice!")

