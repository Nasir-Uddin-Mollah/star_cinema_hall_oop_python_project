class Star_Cinema:
    def __init__(self) -> None:
        self.__hall_list = {}

    def entry_hall(self, hall):
        self.__hall_list[hall.hall_no] = hall
    
    def get_hall_list(self):
        return self.__hall_list


class Hall:
    def __init__(self, row, col, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__row = row
        self.__col = col
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        info = (id,movie_name,time)
        self.__show_list.append(info)
        allocate = [[0 for i in range(self.__col)] for i in range(self.__row)]
        self.__seats[id] = allocate

    def book_seats(self, id, row, col):
        if id not in self.__seats: 
            print(f"Id {id} not found.")
            return False
         
        if 0 <= row < self.__row and 0 <= col < self.__col: 
            if self.__seats[id][row][col] == 0: 
                self.__seats[id][row][col] = 1 
                print(f"Seat ({row}, {col}) for id {id} is booked successfully.")
                return True
            else: 
                print(f"Seat ({row}, {col}) for id {id} is already booked.") 
                return False
        else:
            print(f"Invalid seat position.")
            return False

    def view_show_list(self):
        if len(self.__show_list) == 0:
            print(f"No shows running")
        else:
            print("Running shows are:")
            for id,movie_name,time in self.__show_list:
                print(f"id: {id}, movie_name: {movie_name}, time: {time}")

    def view_available_seats(self, id):
        if id in self.__seats: 
            print(f"Available seats in Holl No: {self.hall_no} for Id {id}: ")
            for seat in self.__seats[id]:
                print(seat) 
            return True
        else :
            return False


class Counter:
    def __init__(self):
        pass

    def option1(self, cinema):
        for key, val in cinema.get_hall_list().items():
            val.view_show_list()

    def option2(self, cinema, id):
        ok = False
        for key, val in cinema.get_hall_list().items():
            check = val.view_available_seats(id)
            if check:
                ok = True
        if not ok :
            print(f"id {id} is not available.")
        print()

    def option3(self, cinema, hall_id, row, col):
        hall_list = cinema.get_hall_list()
        if hall_id in hall_list:
            room = hall_list[hall_id]
            if len(room._Hall__show_list) == 0:
                print(f"No show in hall ({hall_id})")
                return
            id = room._Hall__show_list[0][0]
            room.book_seats(id, row, col)
        else:
            print(f"Hall {hall_id} does not exist.")
        # print()


cinema = Star_Cinema()

cinema.entry_hall(Hall(5,5,101))
cinema.entry_hall(Hall(5,5,102))
cinema.entry_hall(Hall(5,5,103))
cinema.entry_hall(Hall(5,5,104))

cinema.get_hall_list()[101].entry_show(1001, "A", "12:00 PM")
cinema.get_hall_list()[101].entry_show(1002, "B", "3:00 PM")
cinema.get_hall_list()[102].entry_show(1003, "C", "3:00 PM")
cinema.get_hall_list()[102].entry_show(1004, "D", "6:00 PM")
cinema.get_hall_list()[103].entry_show(1005, "E", "6:00 PM")
cinema.get_hall_list()[103].entry_show(1006, "F", "9:00 PM")
cinema.get_hall_list()[104].entry_show(1007, "G", "9:00 PM")
cinema.get_hall_list()[104].entry_show(1008, "H", "12:00 AM")


while True:
    print("1. View running shows")
    print("2. View available seats")
    print("3. Book ticket")
    print("4. Exit")

    n = int(input("Enter option: "))
    customer = Counter()

    if n == 1:
        customer.option1(cinema)
        print()
    if n == 2:
        id = int(input("Enter movie id: "))
        customer.option2(cinema,id)
    if n == 3:
        id = int(input("Enter hall id: "))
        row = int(input("Enter row: "))
        col = int(input("Enter Col: "))
        customer.option3(cinema,id,row,col)
        print()
    elif n == 4:
        break


