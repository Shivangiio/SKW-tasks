import datetime

class TaskScheduler:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, time):
        if time in self.tasks:
            self.tasks[time].append(task)
        else:
            self.tasks[time] = [task]

    def get_tasks(self, date):
        tasks_on_date = self.tasks.get(date, [])
        return tasks_on_date

def main():
    scheduler = TaskScheduler()
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. View tasks for a particular day")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            date_str = input("Enter date (YYYY-MM-DD): ")
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                scheduler.add_task(task, date)
                print("Task added successfully!")
            except ValueError:
                print("Invalid date format. Please enter date in YYYY-MM-DD format.")

        elif choice == '2':
            date_str = input("Enter date to view tasks (YYYY-MM-DD): ")
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                tasks = scheduler.get_tasks(date)
                if tasks:
                    print("Tasks for {}:".format(date))
                    for task in tasks:
                        print("- {}".format(task))
                else:
                    print("No tasks scheduled for", date)
            except ValueError:
                print("Invalid date format. Please enter date in YYYY-MM-DD format.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
