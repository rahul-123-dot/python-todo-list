import random, time

WHITE = "\033[97m"
GREEN = "\033[92m"
BLUE = "\033[34m"
RED = "\033[31m"
DARK_RED = "\033[91m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
CYAN = "\033[36m"
RESET = "\033[0m"

def check(comp, user):
    """This function is main part of this project because it handles all logics of snake water gun game"""

    if comp == user:
        return 0
    elif (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1
    else:
        return 1

user_score = 0
comp_score = 0
highest_user_score = 0
highest_comp_score = 0
history = []
    
print(f"\n\t{WHITE}🎮 Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!{RESET}")
print("-" * 100)
time.sleep(2)

while True:
    try:
        user = int(input("\nEnter number 0 for 'Snake 🐍', 1 for 'Water 💧', 2 for 'Gun 🔫': ").strip())
        if user not in [0, 1, 2]:
            time.sleep(1)
            print(f"{RED}Invalid Choice! Enter 0, 1, or 2 only.{RESET}")
            continue
    except ValueError:
        time.sleep(1)
        print(f"{RED}Please enter valid number (0, 1, 2).{RESET}")
        continue

    print(f"{RED}🤖 Computer is thinking", end=" ", flush=True)
    for sec in range(3, 0, -1):
        print(f"{sec}...", end=" ", flush=True)
        time.sleep(1)
    print(f"GO!{RESET}")
    time.sleep(1)
    comp = random.randint(0, 2)

    names = ["Snake 🐍", "Water 💧", "Gun 🔫"]    
    print(f"\n👤 You: {names[user]}")
    print(f"🤖 Computer: {names[comp]}")

    result = check(comp, user)

    match result:
        case 0:
            print(f"⚖️ {YELLOW} It's Draw!{RESET}")
            round_result = "Draw"
        case -1:        
            print(f"{RED}💻 Computer Win!{RESET}")
            comp_score += 1
            round_result = "Computer Win"
        case 1:
            print(f"{GREEN}🎉 You Win.{RESET}")
            user_score += 1
            round_result = "You Win"

    if user_score > highest_user_score:
        highest_user_score = user_score
    if comp_score > highest_comp_score:
        highest_comp_score = comp_score

     
    history.append({"You": names[user], "Computer": names[comp], "Result": round_result})

    print(f"\n{CYAN}Scoreboard ->{RESET}  You: {user_score}  |  Computer: {comp_score}")
    time.sleep(1)

    again = input("\nPlay again (yes/no): ").strip().lower()
    if again != "yes":
        time.sleep(2)
        print(f"\n{CYAN}----🏁 Final Score ----{RESET}")
        print(f"👤 You: {user_score}")
        print(f"🤖 Computer: {comp_score}")

        if user_score > comp_score:
            print(f"{GREEN}🏆 You Overall winner.{RESET}")
        elif user_score < comp_score:
            print(f"{RED}💻 Computer Overall winner.{RESET}")
        else:
            print(f"{YELLOW}⚖️  It's Tie Overall.{RESET}")
        time.sleep(1)

        print(f"\n{CYAN}----🏆 Leaderboard ----{RESET}")
        print(f"Highest User Score: {highest_user_score}")
        print(f"Highest Computer Score: {highest_comp_score}")
        print(f"Total Rounds Played: {len(history)}") 
        time.sleep(1)

        print(f"\n{CYAN}---- 📜 Game History ----{RESET}")
        for i, record in enumerate(history, 1):
            if "You Win" in record['Result']:
                color = GREEN
            elif "Computer Win" in record['Result']:
                color = RED
            else:
                color = YELLOW
            print(f"Round {i}: You -> {record['You']}  |  Computer -> {record['Computer']}  |  Result -> {color}{record['Result']}{RESET}")       
        time.sleep(2)

        for ch in f"\n\t✨ {BLUE}Thanks for Playing Snake-Water-Gun Game!{RESET} ✨\n\n":
            print(ch, end="", flush=True)
            time.sleep(0.05)
        break

