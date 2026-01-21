import os, time

FILENAME = "tasks.txt"

print("\n📋 ----------- TO-DO LIST -----------")

# Load existing tasks
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file if line.strip()]
else:
    tasks = []

while True:
    print("\n🔹 MENU")
    print("A. View tasks")
    print("B. Add task")
    print("C. Remove task")
    print("D. Exit")

    choice = input("\n👉 Enter your choice (A-D): ").strip().upper()

    # VIEW TASKS
    if choice == "A":
        if not tasks:
            print("\n⚠️ No tasks available.")
        else:
            print("\n📝 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"   {i}. {task}")
        time.sleep(1)

    # ADD TASK
    elif choice == "B":
        task = input("\n➕ Enter your task: ").strip()
        if task:
            tasks.append(task)
            with open(FILENAME, "a") as file:
                file.write(task + "\n")
            print(f"✅ Task added: {task}")
        else:
            print("❌ Task cannot be empty.")
        time.sleep(1)

    # REMOVE TASK
    elif choice == "C":
        if not tasks:
            print("\n⚠️ No tasks to remove.")
        else:
            print("\n🗑️ Select task to remove:")
            for i, task in enumerate(tasks, start=1):
                print(f"   {i}. {task}")

            try:
                index = int(input("\n👉 Enter task number: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    with open(FILENAME, "w") as file:
                        for t in tasks:
                            file.write(t + "\n")
                    print(f"🗑️ Task removed: {removed}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
        time.sleep(1)

    # EXIT
    elif choice == "D":
        print("\n👋 Exiting To-Do List...")
        time.sleep(1)
        for ch in "\n\t✨ Thanks for using the app!\n\n":
            print(ch, end="", flush=True)
            time.sleep(0.05)
        break

    # INVALID INPUT
    else:
        print("❌ Invalid choice. Please select A, B, C, or D.")
