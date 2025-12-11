class Book:
    # წიგნის ობიექტი
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class BookManager:
    # წიგნების მენეჯერი
    def __init__(self):
        self.books = []   # ინახავს ყველა წიგნს მეხსიერებაში

    def add_book(self, title, author, year):
        # ამატებს ახალ წიგნს
        self.books.append(Book(title, author, year))
        print("წიგნი წარმატებით დაემატა!")

    def show_all(self):
        # ყველა წიგნის ჩვენება
        if not self.books:
            print("სია ცარიელია.")
            return
        for b in self.books:
            print(f"{b.title} | {b.author} | {b.year}")

    def search_by_title(self, title):
        # ძებნა სათაურით
        for b in self.books:
            if b.title.lower() == title.lower():
                print(f"ნაპოვნია: {b.title} - {b.author} ({b.year})")
                return
        print("ასეთი წიგნი ვერ მოიძებნა.")


def main():
    manager = BookManager()

    while True:
        print("\n BOOK MANAGER")
        print("1. წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. ძებნა სათაურით")
        print("4. გასვლა")

        choice = input("აირჩიეთ ოპერაცია: ")

        if choice == "1":
            title = input("სათაური: ")
            author = input("ავტორი: ")
            year = input("წელი: ")

            if not year.isdigit():
                print("გთხოვთ შეიყვანოთ რიცხვი.")
                continue

            manager.add_book(title, author, int(year))

        elif choice == "2":
            manager.show_all()

        elif choice == "3":
            t = input("ძიების სათაური: ")
            manager.search_by_title(t)

        elif choice == "4":
            print("გამოსვლა…")
            break

        else:
            print("არასწორი არჩევანი!")
main()