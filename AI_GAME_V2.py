import random
import time
import sys
import os

# --- ⚙️ CONFIG: Difficulty Settings (Same as V9.1 GUI) ---
DIFFICULTY_SETTINGS = {
    "Easy": {
        "name": "Easy Mode (Kindergarten)",
        "prog_min": 15, "prog_max": 30,  
        "heal_min": 15, "heal_max": 30,  
        "ai_chance": 0.3,                
        "dmg_mult": 0.5                  
    },
    "Normal": {
        "name": "Normal Mode (Human)",
        "prog_min": 10, "prog_max": 20,
        "heal_min": 10, "heal_max": 25,
        "ai_chance": 0.5,                
        "dmg_mult": 0.8                  
    },
    "Hard": {
        "name": "Hard Mode (Real Life)",
        "prog_min": 8, "prog_max": 18,
        "heal_min": 5, "heal_max": 15,
        "ai_chance": 0.7,                
        "dmg_mult": 1.0                  
    },
    "God": {
        "name": "God Mode (Are you kidding?)",
        "prog_min": 1, "prog_max": 5,    
        "heal_min": 1, "heal_max": 5,    
        "ai_chance": 0.95,               
        "dmg_mult": 2.0                  
    }
}

# Function to print coolly (slowly for suspense)
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    # Use 'cls' for Windows and 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

# --- DevWarrior Class (Using Settings) ---
class DevWarrior:
    def __init__(self, difficulty="Normal"):
        self.difficulty = difficulty
        self.settings = DIFFICULTY_SETTINGS[difficulty]
        self.name = "The Desperate Dev"
        self.sanity = 100 
        self.progress = 0 
        self.coffee = 3 
        self.water_count = 0 

    def status(self):
        print(f"\n========================================")
        print(f"👤 Player: {self.name} (Difficulty: {self.settings['name']})")
        print(f"🧠 Sanity: {self.sanity}/100")
        print(f"💻 Progress: {self.progress}% Done")
        
        coffee_display = f"☕ Coffee: {self.coffee} cups"
        if self.coffee == 0:
             coffee_display = f"💧 Water: {self.water_count} times"
             
        print(f"📦 Items: {coffee_display}")
        print(f"========================================\n")

    def code(self):
        s = self.settings
        gain = random.randint(s["prog_min"], s["prog_max"]) 
        self.progress += gain
        slow_print(f"⌨️  You code... Progress +{gain}% !!")
        if self.progress > 100: self.progress = 100
        return "code" 

    def google_stack(self):
        s = self.settings
        heal = random.randint(s["heal_min"], s["heal_max"]) 
        self.sanity += heal
        slow_print(f"🔍 You research... Sanity restored by {heal} points")
        if self.sanity > 100: self.sanity = 100
        return "google"

    def drink_coffee(self):
        if self.coffee > 0:
            self.coffee -= 1
            self.sanity += 40
            slow_print(f"☕ Sipping 7-11 coffee... Hyped!! Sanity +40! ({self.coffee} cups left)")
            if self.sanity > 100: self.sanity = 100
            return True 
        else:
            self.water_count += 1
            s = self.settings
            heal = random.randint(s["heal_min"] // 2, s["heal_max"] // 2)
            if heal < 1: heal = 1
            self.sanity += heal
            if self.sanity > 100: self.sanity = 100
            slow_print(f"💧 Coffee ran out! Drinking water... Sanity +{heal} points")
            return False 

def ai_attack(player):
    s = player.settings
    ai_list = ["Apologetic Claude", "Quota-Exceeded Gemini", "Glitchy GPT"]
    boss = random.choice(ai_list)
    
    print(f"\n⚠️  {boss} appears to interrupt you!!")
    time.sleep(1)

    base_dmg = random.randint(15, 25)
    final_dmg = int(base_dmg * s["dmg_mult"])

    if boss == "Apologetic Claude":
        player.progress -= final_dmg
        if player.progress < 0: player.progress = 0
        slow_print(f"🤖 Claude: 'Sorry, the previous code was broken...' (Deletes your code)")
        slow_print(f"💥 Progress lost by {final_dmg}% !!")
        player.sanity -= 5 
        

    elif boss == "Quota-Exceeded Gemini":
        player.sanity -= final_dmg
        slow_print(f"🤖 Gemini: 'Limit Reached! Subscribe to Premium!'")
        slow_print(f"💥 You rage and lose {final_dmg} Sanity!!")

    elif boss == "Glitchy GPT":
        damage = int(final_dmg * 0.7) 
        player.sanity -= damage
        slow_print(f"🤖 GPT: 'asdf jkl; error 404 logic not found...'")
        slow_print(f"💫 You are confused by its answer. Sanity lost by {damage} points!!")
        
    time.sleep(1)


def difficulty_selection():
    clear_screen()
    slow_print("--- Choose Your Difficulty ---", delay=0.01)
    
    modes_list = list(DIFFICULTY_SETTINGS.keys())
    
    for i, mode_key in enumerate(modes_list):
        settings = DIFFICULTY_SETTINGS[mode_key]
        print(f"{i+1}. {settings['name']} (AI Chance: {int(settings['ai_chance']*100)}%)")

    while True:
        try:
            choice = input("\nSelect (1-4): ")
            index = int(choice) - 1
            
            if 0 <= index < len(modes_list):
                return modes_list[index]
            else:
                slow_print(f"💢 **What the hell did you choose?** {choice} is not an option! Try again!")
                time.sleep(1)

        except ValueError:
            slow_print("💢 **What the hell did you choose?** Numbers only! Try again!")
            time.sleep(1)

# --- GAME LOOP ---
def game_loop():
    chosen_difficulty = difficulty_selection()
    
    clear_screen()
    slow_print(f"🔥 Start Game Mode: {DIFFICULTY_SETTINGS[chosen_difficulty]['name']} 🔥")
    slow_print("Mission: Finish code before AI drives you crazy...")
    time.sleep(1)

    player = DevWarrior(chosen_difficulty)

    while player.progress < 100 and player.sanity > 0:
        player.status()
        
        is_safe_turn = False
        
        print("Choose Action:")
        print("1. ⌨️  Code (Progress)")
        print("2. 🔍 Research (Sanity)")
        print("3. ☕ Drink Coffee (Restore Sanity/Water)")
        print("0. 🛑 Quit Game (Why? Don't quit. Why quit? Why quit? Why quit?)")
        
        choice = input("\nSelect (0-3): ")

        if choice == '1':
            player.code()
        elif choice == '2':
            player.google_stack()
        elif choice == '3':
            is_safe_turn = player.drink_coffee() 
        elif choice == '0':
            slow_print("\nGive up? Seriously? It's an easy game! 🤣")
            break
        else:
            slow_print("❌ What did you press? Wasted turn!")
        
        time.sleep(1)
        
        # 4. AI Counter Attack
        if player.progress < 100 and player.sanity > 0:
            
            if is_safe_turn:
                slow_print("\n🧘 Safe Zone! Coffee saves lives!")
                
            else:
                chance = player.settings['ai_chance']
                if random.random() < chance:
                    ai_attack(player)
                else:
                    slow_print("\n✨ Lucky! AI didn't annoy you this round.")
        
        if player.sanity <= 0: break
        
        input("\n[Press Enter to continue...]")
        clear_screen()

    # --- GAME OVER / WIN ---
    player.status()
    if player.progress >= 100:
        if player.difficulty == "God":
            slow_print("\n🏆🏆 You are a GOD! How did you win this hell mode! 🏆🏆")
            slow_print("Take the trophy!")
        else:
            slow_print("\n🎉🎉 YEAH! You finished the code! 🎉🎉")
            slow_print("You defeated the stupid AIs! Go to sleep now!")
    elif player.sanity <= 0:
        slow_print("\n💀💀 GAME OVER 💀💀")
        slow_print("You went insane at your computer... AI takes over the world.")
        slow_print("RIP.")

    time.sleep(3)
    
    # --- Fix: Loop until y/n is pressed ---
    while True:
        try_again = input("\nPlay again? (y/n): ").lower()
        if try_again == 'y':
            game_loop()
            break # Exit loop
        elif try_again == 'n':
            clear_screen()
            slow_print("Go rest! See you later!")
            break # Exit loop
        else:
            slow_print("💢 **I asked for y or n!** Play (y) or Quit (n)!? Try again!")
            time.sleep(1)
            
if __name__ == "__main__":
    game_loop()