from book import Book
from student import Student


class Library:
    def __init__(self):
        self.books = []
        self.students = []

    # ===== QUAN LY SACH =====
    def add_book(self):
        id = input("Nhap ma sach: ")
        title = input("Nhap ten sach: ")
        author = input("Nhap tac gia: ")
        try:
            quantity = int(input("Nhap so luong: "))
            if quantity < 0:
                print("So luong khong duoc am!")
                return
        except ValueError:
            print("Loi: ban phai nhap so luong la so nguyen!")
            return

        new_book = Book(id, title, author, quantity)
        self.books.append(new_book)
        print("Them sach thanh cong!")

    def view_books(self):
        if len(self.books) == 0:
            print("Danh sach sach dang trong!")
            return
        for book in self.books:
            book.show_info()

    def find_book(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None

    def search_book(self):
        id = input("Nhap ma sach can tim: ")
        book = self.find_book(id)
        if book is None:
            print("Khong tim thay sach!")
        else:
            print("Da tim thay sach:")
            book.show_info()

    def delete_book(self):
        id = input("Nhap ma sach can xoa: ")
        book = self.find_book(id)
        if book is None:
            print("Khong tim thay sach!")
        else:
            self.books.remove(book)
            print("Xoa sach thanh cong!")

    # ===== QUAN LY SINH VIEN =====
    def add_student(self):
        id = input("Nhap ma sinh vien: ")
        name = input("Nhap ho ten: ")
        class_name = input("Nhap lop: ")

        new_student = Student(id, name, class_name)
        self.students.append(new_student)
        print("Them sinh vien thanh cong!")

    def view_students(self):
        if len(self.students) == 0:
            print("Danh sach sinh vien dang trong!")
            return
        for student in self.students:
            student.show_info()

    def find_student(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def search_student(self):
        id = input("Nhap ma sinh vien can tim: ")
        student = self.find_student(id)
        if student is None:
            print("Khong tim thay sinh vien!")
        else:
            print("Da tim thay sinh vien:")
            student.show_info()

    def delete_student(self):
        id = input("Nhap ma sinh vien can xoa: ")
        student = self.find_student(id)
        if student is None:
            print("Khong tim thay sinh vien!")
        else:
            self.students.remove(student)
            print("Xoa sinh vien thanh cong!")

    # ===== MUON / TRA SACH =====
    def borrow_book(self):
        student_id = input("Nhap ma sinh vien: ")
        student = self.find_student(student_id)
        if student is None:
            print("Khong tim thay sinh vien!")
            return

        book_id = input("Nhap ma sach can muon: ")
        book = self.find_book(book_id)
        if book is None:
            print("Book not found")
            return

        if book.decrease_quantity():
            print(f"{student.name} da muon sach {book.title} thanh cong!")
        else:
            print("Sach da het, khong the muon!")

    def return_book(self):
        book_id = input("Nhap ma sach can tra: ")
        book = self.find_book(book_id)
        if book is None:
            print("Book not found")
            return

        book.increase_quantity()
        print("Tra sach thanh cong!")
