import tkinter as tk
from tkinter import messagebox
import random

# --- DevWarrior Class (Using V7 logic, no changes needed) ---
class DevWarrior:
    def __init__(self):
        self.name = "The Desperate Dev"
        self.sanity = 100
        self.progress = 0
        self.coffee = 3 
        self.water_count = 0 

    def code(self):
        gain = random.randint(8, 20) 
        self.progress += gain
        if self.progress > 100: self.progress = 100
        return f"⌨️  You type furiously... Progress +{gain}% !!"

    def google_stack(self):
        heal = random.randint(10, 25) 
        self.sanity += heal
        if self.sanity > 100: self.sanity = 100
        return f"🔍 You copy code from StackOverflow... Sanity restored by {heal} points"

    def drink_coffee(self):
        if self.coffee > 0:
            self.coffee -= 1
            self.sanity += 40
            if self.sanity > 100: self.sanity = 100
            return f"☕ Sipping 7-11 coffee... Hyped!! Sanity +40! ({self.coffee} cups left)"
        else:
            self.water_count += 1
            heal = random.randint(3, 10) 
            self.sanity += heal
            if self.sanity > 100: self.sanity = 100
            return f"💧 Coffee ran out! You drink water instead... Sanity +{heal} (Fight with your heart!)"

    def ai_attack(self):
        ai_list = ["Apologetic Claude", "Quota-Exceeded Gemini", "Glitchy GPT"]
        boss = random.choice(ai_list)
        
        log_msg = f"⚠️  {boss} appears to interrupt you!!"

        if boss == "Apologetic Claude":
            damage = random.randint(10, 20) 
            self.progress -= damage
            if self.progress < 0: self.progress = 0
            log_msg += f"\n🤖 Claude: 'Sorry, the code is broken. I'll rewrite it in **Rust**!'\n💥 Progress lost by {damage}% !!"
            self.sanity -= 5
            
        elif boss == "Quota-Exceeded Gemini":
            damage = random.randint(15, 25) 
            self.sanity -= damage
            log_msg += f"\n🤖 Gemini: 'Limit Reached! Subscribe to Premium!'\n💰 Billing Pop-up appears! You lose {damage} Sanity!!"
            
        elif boss == "Glitchy GPT":
            damage = random.randint(10, 25) 
            self.sanity -= damage
            log_msg += f"\n🤖 GPT: 'The code provided entered **Infinite Recursion**!'\n💥 You lose {damage} Sanity debugging it!!"
            
        return log_msg

# --- Game App (GUI with Animation and Bugfix V8) ---
class GameApp:
    def __init__(self, master):
        self.master = master
        master.title("🔥 The Rate Limit Runner V8 (BUGFIXED!) 🔥")
        master.geometry("600x500")
        master.resizable(False, False)
        
        self.player = DevWarrior()
        self.message_queue = []
        self.is_animating = False

        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        # Header
        tk.Label(self.master, text="The Desperate Dev: Vibe Coding Saga", 
                 font=("Kanit", 16, "bold"), fg="#FF4500").pack(pady=15)

        # Status Frame
        self.status_frame = tk.Frame(self.master, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        self.status_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.sanity_label = tk.Label(self.status_frame, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.sanity_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.progress_label = tk.Label(self.status_frame, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.progress_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.coffee_label = tk.Label(self.status_frame, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.coffee_label.pack(side=tk.LEFT, padx=20, pady=10)

        # Log Text Area
        tk.Label(self.master, text="--- Turn Log (Latest Events) ---", font=("Arial", 10)).pack(pady=(10,0))
        self.log_text = tk.Text(self.master, height=12, width=65, state=tk.DISABLED, wrap=tk.WORD, 
                                font=("Consolas", 11), bg="#1e1e1e", fg="#00FF00")
        self.log_text.pack(pady=5)

        # Button Frame
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=20)

        # ปุ่ม 1, 2, 3
        self.btn_code = tk.Button(self.button_frame, text="1. ⌨️ Code", command=lambda: self.start_turn("code"), 
                  width=15, height=2, bg="#D4F0CC", font=("Arial", 11, "bold"))
        self.btn_code.pack(side=tk.LEFT, padx=10)
        
        self.btn_google = tk.Button(self.button_frame, text="2. 🔍 Research", command=lambda: self.start_turn("google"), 
                  width=15, height=2, bg="#CCE4F0", font=("Arial", 11, "bold"))
        self.btn_google.pack(side=tk.LEFT, padx=10)
        
        self.btn_coffee = tk.Button(self.button_frame, text="3. ☕ Drink Coffee", command=lambda: self.start_turn("coffee"), 
                  width=15, height=2, bg="#F0CCCC", font=("Arial", 11, "bold"))
        self.btn_coffee.pack(side=tk.LEFT, padx=10)

        # **Invisible Button: For TROLLing!**
        self.btn_troll = tk.Button(self.button_frame, text="4. 🤫", command=lambda: self.start_turn("troll"),
                                   width=4, height=2, bg="#333333", fg="#333333", borderwidth=0, 
                                   activebackground="#333333", activeforeground="#333333")
        self.btn_troll.pack(side=tk.LEFT, padx=2) 


    def update_status(self):
        # Update colors based on status
        sanity_color = "red" if self.player.sanity < 30 else "black"
        self.sanity_label.config(text=f"🧠 Sanity: {self.player.sanity}/100", fg=sanity_color)
        self.progress_label.config(text=f"💻 Work: {self.player.progress}%")
        
        # Change Text on Coffee button if ran out
        if self.player.coffee == 0:
            self.btn_coffee.config(text="3. 💧 Drink Water", bg="#EEEEEE")
            self.coffee_label.config(text=f"💧 Water x{self.player.water_count}")
        else:
            self.btn_coffee.config(text="3. ☕ Drink Coffee", bg="#F0CCCC")
            self.coffee_label.config(text=f"☕ Coffee: {self.player.coffee} cups")

    def set_buttons_state(self, state):
        self.btn_code.config(state=state)
        self.btn_google.config(state=state)
        self.btn_coffee.config(state=state)
        self.btn_troll.config(state=state) 

    # --- Animation Logic (Same as before) ---
    def type_text(self, text, index=0):
        if index < len(text):
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, text[index])
            self.log_text.see(tk.END)
            self.log_text.config(state=tk.DISABLED)
            self.master.after(30, self.type_text, text, index + 1)
        else:
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, "\n")
            self.log_text.config(state=tk.DISABLED)
            self.master.after(500, self.process_message_queue)

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

    # --- Turn Execution (Fixed AI Logic) ---
    def start_turn(self, action):
        if self.is_animating: return
        
        self.is_animating = True
        self.set_buttons_state(tk.DISABLED)
        
        # 1. Clear old Log
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete('1.0', tk.END)
        self.log_text.config(state=tk.DISABLED)

        # 2. Calculate Player Result
        player_msg = ""
        is_safe_turn = False 

        if action == "code":
            player_msg = self.player.code()
        elif action == "google":
            player_msg = self.player.google_stack()
        elif action == "coffee":
            player_msg = self.player.drink_coffee()
            # is_safe_turn is True only if action is 'coffee' and coffee is available
            if "☕ Sipping 7-11 coffee" in player_msg: 
                is_safe_turn = True 
        elif action == "troll":
            player_msg = "❌ What did you press? Wasted turn! (Because you wanted to be scolded)"
            
        self.message_queue.append(player_msg)

        # 3. Calculate AI Result (FIXED LOGIC)
        if self.player.progress < 100 and self.player.sanity > 0 and not action == "troll":
             
             if is_safe_turn:
                # FIX: If Safe Zone (Real Coffee), Skip AI Check
                self.message_queue.append("🧘 Relax! Coffee puts you in Safe Zone! AI dares not disturb!")
                
             else:
                # Normal Risk (Code, Google, Water, หรือ No-Real-Coffee)
                # 🔴 Reduce AI attack chance to 60%
                if random.random() < 0.6:
                    ai_msg = self.player.ai_attack()
                    for line in ai_msg.split('\n'):
                        self.message_queue.append(line)
                else:
                    self.message_queue.append("✨ Lucky! AI didn't annoy you this round.")


        # 4. Start Animation Process
        self.process_message_queue()

    def check_game_end(self):
        if self.player.progress >= 100:
            messagebox.showinfo("YOU WIN!", "🎉🎉 YEAH! You finished the code! Vibe Coding Success!")
            self.master.quit()
        elif self.player.sanity <= 0:
            messagebox.showerror("GAME OVER!", "💀 You went insane at your computer... AI drove you crazy. RIP.")
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()