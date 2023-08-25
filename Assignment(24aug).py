class FlightTable:
    def _init_(self, pid, process, start_time, priority):
        self.pid = pid
        self.process = process
        self.start_time = start_time
        self.priority = priority

def sort_key(item):
    return item.pid

def main():
    flight_data = [
        FlightTable("P1", "VSCode", 100, "MID"),
        FlightTable("P23", "Eclipse", 234, "MID"),
        FlightTable("P93", "Chrome", 189, "High"),
        FlightTable("P42", "JDK 9", 9, "High"),
        FlightTable("P9", "CMD", 7, "High"),
        FlightTable("P87", "NotePad", 23, "Low")
    ]

    print("Sorting options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sorted_data = sorted(flight_data, key=sort_key)
    elif choice == 2:
        sorted_data = sorted(flight_data, key=lambda item: item.start_time)
    elif choice == 3:
        sorted_data = sorted(flight_data, key=lambda item: item.priority)
    else:
        print("Invalid choice")
        return

    print("\nSorted Flight Table:")
    print("{:<5} {:<10} {:<15} {:<8}".format("P_ID", "Process", "Start Time", "Priority"))
    for item in sorted_data:
        print("{:<5} {:<10} {:<15} {:<8}".format(item.pid, item.process, item.start_time, item.priority))

if _name_ == "_main_":
    main()