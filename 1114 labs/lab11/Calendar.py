class Calendar:
    def __init__(self,month = 1,day =1 ,year =1 ,dayOfWeek =1):
        date = input("Please enter today's date in mm/dd/yy format: ")
        self.dayOfWeek = input("Please enter the day of the week today (1 for Monday and 7 for Sunday): ")
        self.month = date[:2]
        self.day = date[3:5]
        self.year = date[6:]

    def __repr__(self):
        print("Today's date is: ", self.dayOfWeek, " ", self.month, "/", self.day,"/",self.year,sep = '')
        print("Today's Accomplishment")
        print("==========================")
        for j in range(len(ToDoList.taskDone)):
            if(ToDoList.get_task_done(j) == True):
                print(ToDoList.get_toDo(j))
        print("Things left to Do")
        print("==========================")
        for i in range (len(ToDoList.toDo)):
            if(ToDoList.get_task_done(i) == False):
                print(ToDoList.get_toDo(i))

    def start_new_day(self):
        if(day <= 30):
            day += 1
        else:
            day = 1
            if (month == 12):
                month = 1
                year += 1
            else:
                month += 1
        if(dayOfWeek < 7):
            dayOfWeek += 1
        else: dayOfWeek = 1
    def to_do_list(self):
        listObject = ToDoList()

    class ToDoList:
        def get_toDo(self,j):
            return self.toDo[j]
        def get_task_done(self, j):
            return self.taskDone[j]
        def __init__(self, toDo = [], taskDone = []):
            self.toDo = toDo
            self.taskDone = taskDone
        def create_to_do_list_item(self):
            self.toDo.append(self.task)
            self.taskDone.append(False)
        def check_to_do_list(self):

            valid = False
            for i in range(len(self.toDo)):
                response = input("did you do", toDo[i], " (y/n)")
                while(valid == False):
                    if (response == 'y'):
                        self.taskDone[i] = True
                        valid = True
                    elif (response == 'n'):
                        self.taskDone[i] = False
                        valid = True
                    else:
                        print("Invalid response")
                        valid = False
        def __repr__(self):
            self.task = input("Enter the task: ")


def main():
    calendar = Calendar()
    while True:
        print("\nMain Menu:")
        print("1. Create New Calendar")
        print("2. Add To-Do List Item")
        print("3. check Off To-Do List")
        print("4. Show Today's Calendar")
        print("5. Start The Next Day\n")

        answer = input("What would you like to do? ")
        if answer == '1':
            calendar = Calendar()
        elif answer == '2':
            calendar.to_do_list.create_to_do_list_item()
        elif answer == '3':
            calendar.to_do_list.check_to_do_list()
        elif answer == '4':
            print(repr(calendar))
        elif answer == '5':
            calendar.start_new_day()

main()