import random
import time
import sys
import os

# Function to print coolly (slowly for suspense)
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class DevWarrior:
    def __init__(self):
        self.name = "The Desperate Dev"
        self.sanity = 100  # Sanity
        self.progress = 0  # Work Done
        self.coffee = 3    # Healing Item

    def status(self):
        print(f"\n========================================")
        print(f"👤 Player: {self.name}")
        print(f"🧠 Sanity: {self.sanity}/100")
        print(f"💻 Progress: {self.progress}% Done")
        print(f"☕ Coffee Left: {self.coffee} แก้ว")
        print(f"========================================\n")

    def code(self):
        gain = random.randint(10, 25)
        self.progress += gain
        slow_print(f"⌨️  You type furiously... Progress +{gain}% !!")
        if self.progress > 100: self.progress = 100

    def google_stack(self):
        heal = random.randint(10, 20)
        self.sanity += heal
        slow_print(f"🔍 You copy code from StackOverflow... Sanity restored by {heal} points")
        if self.sanity > 100: self.sanity = 100

    def drink_coffee(self):
        if self.coffee > 0:
            self.coffee -= 1
            self.sanity += 40
            slow_print(f"☕ Sipping 7-11 coffee... Hyped!! Sanity +40!")
            if self.sanity > 100: self.sanity = 100
        else:
            slow_print(f"❌ Coffee ran out! You have to fight with water!")

def ai_attack(player):
    ai_list = ["Apologetic Claude", "Quota-Exceeded Gemini", "Glitchy GPT"]
    boss = random.choice(ai_list)
    
    print(f"\n⚠️  {boss} appears to interrupt you!!")
    time.sleep(1)

    if boss == "Apologetic Claude":
        damage = random.randint(10, 20)
        player.progress -= damage
        if player.progress < 0: player.progress = 0
        slow_print(f"🤖 Claude: 'Sorry, the previous code was broken. I'll rewrite it.' (Deletes your code)")
        slow_print(f"💥 Progress lost by {damage}% !!")

    elif boss == "Quota-Exceeded Gemini":
        damage = random.randint(15, 25)
        player.sanity -= damage
        slow_print(f"🤖 Gemini: 'Limit Reached! Subscribe to Premium!'")
        slow_print(f"💥 You rage and lose {damage} Sanity!!")

    elif boss == "Glitchy GPT":
        slow_print(f"🤖 GPT: 'asdf jkl; error 404 logic not found...'")
        slow_print(f"💫 You are confused by its answer. Wasted 1 turn.")
        # No damage but wasted turn

# --- GAME START ---
clear_screen()
slow_print("🔥 Welcome to 'The Desperate Dev' 🔥")
slow_print("Mission: Finish code before AI drives you crazy...")
time.sleep(1)

player = DevWarrior()

while player.progress < 100 and player.sanity > 0:
    player.status()
    print("Choose action:")
    print("1. ⌨️  Code (Progress, risk of AI)")
    print("2. 🔍 Research (Sanity)")
    print("3. ☕ Drink Coffee (Restore Sanity, Limited)")
    
    choice = input("\nSelect (1-3): ")

    if choice == '1':
        player.code()
    elif choice == '2':
        player.google_stack()
    elif choice == '3':
        player.drink_coffee()
    else:
        slow_print(f"❌ What did you press? Wasted turn!")
    
    time.sleep(1)
    
    # AI attacks if work not done
    if player.progress < 100:
        if random.random() < 0.7: # 70% chance of AI attack
            ai_attack(player)
        else:
            slow_print("\n✨ Lucky! AI didn't annoy you this round.")
    
    input("\n[Press Enter to continue...]")
    clear_screen()

# --- GAME OVER / WIN ---
if player.progress >= 100:
    slow_print("\n🎉🎉 YEAH! You finished the code! 🎉🎉")
    slow_print("You defeated the stupid AIs! Go to sleep now!")
else:
    slow_print("\n💀💀 GAME OVER 💀💀")
    slow_print("You went insane at your computer... AI takes over the world.")
    slow_print("RIP.")