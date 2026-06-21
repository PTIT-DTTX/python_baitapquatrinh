from library import Library

lib = Library()

while True:
    print("\n========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Add Student")
    print("6. View Students")
    print("7. Search Student")
    print("8. Delete Student")
    print("9. Borrow Book")
    print("10. Return Book")
    print("0. Exit")

    choice = input("Chon chuc nang: ")

    if choice == "1":
        lib.add_book()
    elif choice == "2":
        lib.view_books()
    elif choice == "3":
        lib.search_book()
    elif choice == "4":
        lib.delete_book()
    elif choice == "5":
        lib.add_student()
    elif choice == "6":
        lib.view_students()
    elif choice == "7":
        lib.search_student()
    elif choice == "8":
        lib.delete_student()
    elif choice == "9":
        lib.borrow_book()
    elif choice == "10":
        lib.return_book()
    elif choice == "0":
        print("Tam biet!")
        break
    else:
        print("Lua chon khong hop le, vui long chon lai!")
