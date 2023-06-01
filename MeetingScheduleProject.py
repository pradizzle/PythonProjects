meetings = {}

def schedule_meeting():
    print("Schedule a Meeting\n")
    print("Choose a day (enter 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday):")
    day = int(input())
    while day not in range(1, 5):
        print("Invalid day. Please enter a valid day (1-4):")
        day = int(input())
    print("Available times for selected day:")
    for hour in range(1, 4):
        for minute in ["00", "30"]:
            time = f"{hour}:{minute}"
            if time not in meetings.get(day, []):
                print(time)
    print("Choose a time:")
    time = input()
    while time not in meetings.get(day, []) and time not in [f"{hour}:{minute}" for hour in range(1, 4) for minute in ["00", "30"]]:
        print("Invalid time. Please choose an available time:")
        time = input()
    name = input("Enter your name:")
    email = input("Enter your email address:")
    topic = input("Enter discussion topic:")
    if topic == "":
        topic = "office hours"
    if day not in meetings:
        meetings[day] = {}
    meetings[day][time] = {"name": name, "email": email, "topic": topic}
    print("Meeting scheduled successfully!\n")

def view_all_meetings():
    print("All Scheduled Meetings\n")
    if not meetings:
        print("No meetings scheduled.\n")
        return
    for day in range(1, 5):
        print(f"Day {day}:")
        if day not in meetings:
            print()
            continue
        for time in sorted(meetings[day]):
            meeting = meetings[day][time]
            print(f"{time}: {meeting['name']} ({meeting['email']}) - {meeting['topic']}")
        print()
    input("Press enter to continue to the main menu.")

while True:
    print("Main Menu\n")
    print("1. Schedule a Meeting")
    print("2. View All Scheduled Meetings")
    print("3. Quit")
    choice = input("Enter your choice (1-3):")
    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter a valid choice (1-3):")
        choice = input()
    if choice == "1":
        schedule_meeting()
    elif choice == "2":
        view_all_meetings()
    else:
        print("Goodbye!")
        break

