import tkinter as tk
from tkinter import messagebox
import random

# --- ⚙️ CONFIG: Difficulty Settings ---
DIFFICULTY_SETTINGS = {
    "Easy": {
        "name": "Easy Mode (Kindergarten)",
        "prog_min": 15, "prog_max": 30,  # งานเดินไว
        "heal_min": 15, "heal_max": 30,  # ฮีลแรง
        "ai_chance": 0.3,                # AI มาน้อย (30%)
        "dmg_mult": 0.5                  # โดนดาเมจเบาลงครึ่งนึง
    },
    "Normal": {
        "name": "Normal Mode (Human)",
        "prog_min": 10, "prog_max": 20,
        "heal_min": 10, "heal_max": 25,
        "ai_chance": 0.5,                # AI มาครึ่งๆ (50%)
        "dmg_mult": 0.8                  # โดนดาเมจเบาลงนิดนึง
    },
    "Hard": {
        "name": "Hard Mode (Real Life)",
        "prog_min": 8, "prog_max": 18,
        "heal_min": 5, "heal_max": 15,
        "ai_chance": 0.7,                # AI มาบ่อย (70%)
        "dmg_mult": 1.0                  # ดาเมจปกติ (แรง)
    },
    "God": {
        "name": "God Mode (Are you kidding?)",
        "prog_min": 1, "prog_max": 5,    # งานแทบไม่เดิน
        "heal_min": 1, "heal_max": 5,    # ฮีลแทบไม่ขึ้น
        "ai_chance": 0.95,               # AI มาแทบทุกตา (95%)
        "dmg_mult": 2.0                  # ดาเมจคูณ 2 (ทีเดียวเกือบตาย)
    }
}

# --- DevWarrior Class (Logic) ---
class DevWarrior:
    def __init__(self, difficulty="Normal"):
        self.difficulty = difficulty
        self.settings = DIFFICULTY_SETTINGS[difficulty] 
        self.name = "The Desperate Dev"
        self.sanity = 100
        self.progress = 0
        self.coffee = 3 
        self.water_count = 0 

    def code(self):
        s = self.settings
        gain = random.randint(s["prog_min"], s["prog_max"]) 
        self.progress += gain
        if self.progress > 100: self.progress = 100
        return f"⌨️  You code ({self.difficulty})... Progress +{gain}% !!"

    def google_stack(self):
        s = self.settings
        heal = random.randint(s["heal_min"], s["heal_max"]) 
        self.sanity += heal
        if self.sanity > 100: self.sanity = 100
        return f"🔍 You research... Sanity restored by {heal} points"

    def drink_coffee(self):
        if self.coffee > 0:
            self.coffee -= 1
            self.sanity += 40 
            if self.sanity > 100: self.sanity = 100
            return f"☕ Sipping 7-11 coffee... Hyped!! Sanity +40! ({self.coffee} cups left)"
        else:
            self.water_count += 1
            heal = random.randint(self.settings["heal_min"] // 2, self.settings["heal_max"] // 2)
            if heal < 1: heal = 1
            self.sanity += heal
            if self.sanity > 100: self.sanity = 100
            return f"💧 Coffee ran out! Drinking water... Sanity +{heal} points"

    def ai_attack(self):
        s = self.settings
        ai_list = ["Apologetic Claude", "Quota-Exceeded Gemini", "Glitchy GPT"]
        boss = random.choice(ai_list)
        
        log_msg = f"⚠️  {boss} appears!!"

        base_dmg = random.randint(15, 25)
        final_dmg = int(base_dmg * s["dmg_mult"])

        if boss == "Apologetic Claude":
            self.progress -= final_dmg
            if self.progress < 0: self.progress = 0
            log_msg += f"\n🤖 Claude: 'Deleting code!'\n💥 Progress lost by {final_dmg}% !!"
            self.sanity -= 5
            
        elif boss == "Quota-Exceeded Gemini":
            self.sanity -= final_dmg
            log_msg += f"\n🤖 Gemini: 'Pay me!'\n💰 Sanity lost by {final_dmg} points!!"
            
        elif boss == "Glitchy GPT":
            self.sanity -= final_dmg
            log_msg += f"\n🤖 GPT: 'Error 404 Brain Not Found'\n💥 Sanity lost by {final_dmg} points!!"
            
        return log_msg

# --- Game App (GUI) ---
class GameApp:
    def __init__(self, master):
        self.master = master
        master.title("🔥 The Rate Limit Runner V9.1 (Long Text Fix) 🔥")
        master.geometry("600x550")
        master.resizable(False, False)
        
        self.message_queue = []
        self.is_animating = False
        
        self.show_difficulty_selection()

    def show_difficulty_selection(self):
        # Clear old screen
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Choose Your Difficulty", font=("Kanit", 20, "bold")).pack(pady=30)

        # Mode Selection Buttons
        modes = [
            ("Easy (Kindergarten)", "Easy", "#90EE90"),
            ("Normal (Human)", "Normal", "#ADD8E6"),
            ("Hard (Real Life)", "Hard", "#F08080"),
            # **แก้ไขข้อความตามที่มึงขอ และให้ปุ่มมันยาวตามข้อความ**
            ("God (Are you kidding? If you win, you are a god. Take the trophy)", "God", "#8B0000") 
        ]

        for text, mode, color in modes:
            fg_color = "white" if mode == "God" else "black"
            tk.Button(self.master, text=text, command=lambda m=mode: self.start_game(m),
                      # **ลบ 'width=25' ออกเพื่อให้ปุ่มมันขยายอัตโนมัติ**
                      height=2, bg=color, fg=fg_color, font=("Arial", 12, "bold"),
                      # **เพิ่ม wraplength ให้ข้อความยาวๆ ขึ้นบรรทัดใหม่สวยๆ**
                      wraplength=450).pack(pady=10, padx=50, fill=tk.X) # ใช้ fill=tk.X ให้มันยาวเท่ากันหมด
            
    def start_game(self, difficulty):
        self.player = DevWarrior(difficulty) 
        
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.create_game_widgets()
        self.update_status()
        
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, f"> Start: {self.player.settings['name']}\n> Good luck...")
        self.log_text.config(state=tk.DISABLED)

    def create_game_widgets(self):
        # Header
        mode_name = self.player.settings['name']
        header_color = "red" if self.player.difficulty == "God" else "#FF4500"
        tk.Label(self.master, text=f"The Desperate Dev: {mode_name}", 
                 font=("Kanit", 14, "bold"), fg=header_color).pack(pady=15)

        # Status Frame
        self.status_frame = tk.Frame(self.master, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        self.status_frame.pack(pady=5, padx=20, fill=tk.X)
        
        self.sanity_label = tk.Label(self.status_frame, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.sanity_label.pack(side=tk.LEFT, padx=15, pady=10)
        
        self.progress_label = tk.Label(self.status_frame, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.progress_label.pack(side=tk.LEFT, padx=15, pady=10)
        
        self.coffee_label = tk.Label(self.status_frame, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.coffee_label.pack(side=tk.LEFT, padx=15, pady=10)

        # Log Area
        self.log_text = tk.Text(self.master, height=12, width=65, state=tk.DISABLED, wrap=tk.WORD, 
                                font=("Consolas", 11), bg="#1e1e1e", fg="#00FF00")
        self.log_text.pack(pady=5)

        # Button Frame
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=15)

        self.btn_code = tk.Button(self.button_frame, text="1. ⌨️ Code", command=lambda: self.start_turn("code"), 
                  width=15, height=2, bg="#D4F0CC", font=("Arial", 11, "bold"))
        self.btn_code.pack(side=tk.LEFT, padx=5)
        
        self.btn_google = tk.Button(self.button_frame, text="2. 🔍 Research", command=lambda: self.start_turn("google"), 
                  width=15, height=2, bg="#CCE4F0", font=("Arial", 11, "bold"))
        self.btn_google.pack(side=tk.LEFT, padx=5)
        
        self.btn_coffee = tk.Button(self.button_frame, text="3. ☕ Drink Coffee", command=lambda: self.start_turn("coffee"), 
                  width=15, height=2, bg="#F0CCCC", font=("Arial", 11, "bold"))
        self.btn_coffee.pack(side=tk.LEFT, padx=5)

        # Troll Button
        self.btn_troll = tk.Button(self.button_frame, text="4. 🤫", command=lambda: self.start_turn("troll"),
                                   width=4, height=2, bg="#333333", fg="#333333", borderwidth=0, 
                                   activebackground="#333333", activeforeground="#333333")
        self.btn_troll.pack(side=tk.LEFT, padx=2)
        
        # Reset Button
        tk.Button(self.master, text="🔄 Restart", command=self.show_difficulty_selection, 
                  bg="white", fg="red").place(x=10, y=10)

    def update_status(self):
        sanity_color = "red" if self.player.sanity < 30 else "black"
        self.sanity_label.config(text=f"🧠 Sanity: {self.player.sanity}/100", fg=sanity_color)
        self.progress_label.config(text=f"💻 Work: {self.player.progress}%")
        
        if self.player.coffee == 0:
            self.btn_coffee.config(text="3. 💧 Drink Water", bg="#EEEEEE")
            self.coffee_label.config(text=f"💧 Water: {self.player.water_count}")
        else:
            self.btn_coffee.config(text="3. ☕ Drink Coffee", bg="#F0CCCC")
            self.coffee_label.config(text=f"☕ Coffee: {self.player.coffee}")

    def set_buttons_state(self, state):
        self.btn_code.config(state=state)
        self.btn_google.config(state=state)
        self.btn_coffee.config(state=state)
        self.btn_troll.config(state=state)

    def type_text(self, text, index=0):
        if index < len(text):
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, text[index])
            self.log_text.see(tk.END)
            self.log_text.config(state=tk.DISABLED)
            self.master.after(20, self.type_text, text, index + 1) 
        else:
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, "\n")
            self.log_text.config(state=tk.DISABLED)
            self.master.after(300, self.process_message_queue)

    def process_message_queue(self):
        if self.message_queue:
            next_msg = self.message_queue.pop(0)
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, "> ")
            self.log_text.config(state=tk.DISABLED)
            self.type_text(next_msg)
        else:
            self.is_animating = False
            self.set_buttons_state(tk.NORMAL)
            self.update_status()
            self.check_game_end()

    def start_turn(self, action):
        if self.is_animating: return
        self.is_animating = True
        self.set_buttons_state(tk.DISABLED)
        
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete('1.0', tk.END)
        self.log_text.config(state=tk.DISABLED)

        player_msg = ""
        is_safe_turn = False 

        if action == "code":
            player_msg = self.player.code()
        elif action == "google":
            player_msg = self.player.google_stack()
        elif action == "coffee":
            player_msg = self.player.drink_coffee()
            if "☕ Sipping 7-11 coffee" in player_msg: is_safe_turn = True 
        elif action == "troll":
            player_msg = "❌ What did you press? Wasted turn!"
            
        self.message_queue.append(player_msg)

        if self.player.progress < 100 and self.player.sanity > 0 and action != "troll":
             
             if is_safe_turn:
                self.message_queue.append("🧘 Safe Zone! Coffee saves lives!")
             else:
                chance = self.player.settings['ai_chance']
                if random.random() < chance:
                    ai_msg = self.player.ai_attack()
                    for line in ai_msg.split('\n'):
                        self.message_queue.append(line)
                else:
                    self.message_queue.append("✨ Safe! AI didn't attack.")

        self.process_message_queue()

    def check_game_end(self):
        if self.player.progress >= 100:
            if self.player.difficulty == "God":
                msg = "🏆🏆 You are a GOD! How did you win this hell mode! 🏆🏆\nTake the trophy!"
            else:
                msg = "🎉🎉 Vibe Coding Success! Go to sleep!"
            messagebox.showinfo("YOU WIN!", msg)
            self.show_difficulty_selection() 
        elif self.player.sanity <= 0:
            messagebox.showerror("GAME OVER!", "💀 Insanity... RIP.")
            self.show_difficulty_selection() 

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()