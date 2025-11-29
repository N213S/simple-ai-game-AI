import tkinter as tk
from tkinter import messagebox
import random

# --- DevWarrior Class (ใช้โค้ด V7 เดิม ไม่ต้องเปลี่ยน) ---
class DevWarrior:
    def __init__(self):
        self.name = "ไอ้หนุ่มซินตึ๊ง"
        self.sanity = 100
        self.progress = 0
        self.coffee = 3 
        self.water_count = 0 

    def code(self):
        gain = random.randint(8, 20) 
        self.progress += gain
        if self.progress > 100: self.progress = 100
        return f"⌨️  มึงพิมพ์โค้ดรัวๆ... งานเดินไป {gain}% !!"

    def google_stack(self):
        heal = random.randint(10, 25) 
        self.sanity += heal
        if self.sanity > 100: self.sanity = 100
        return f"🔍 มึงไปก๊อปโค้ดชาวอินเดียใน StackOverflow... สติกลับมา {heal} หน่วย"

    def drink_coffee(self):
        if self.coffee > 0:
            self.coffee -= 1
            self.sanity += 40
            if self.sanity > 100: self.sanity = 100
            return f"☕ ซดกาแฟเซเว่น... ดีดจัด!! สติเพิ่ม 40 หน่วย! (เหลือ {self.coffee} แก้ว)"
        else:
            self.water_count += 1
            heal = random.randint(3, 10) 
            self.sanity += heal
            if self.sanity > 100: self.sanity = 100
            return f"💧 กาแฟหมด! มึงแดกน้ำเปล่าแทน... ฟื้นฟูสติ {heal} หน่วย (ต้องสู้ด้วยใจแล้ว!)"

    def ai_attack(self):
        ai_list = ["Claude ขี้ขอโทษ", "Gemini โควต้าหมด", "GPT เอ๋อแดก"]
        boss = random.choice(ai_list)
        
        log_msg = f"⚠️  {boss} โผล่มาขัดจังหวะมึง!!"

        if boss == "Claude ขี้ขอโทษ":
            damage = random.randint(10, 20) 
            self.progress -= damage
            if self.progress < 0: self.progress = 0
            log_msg += f"\n🤖 Claude: 'ขอโทษครับ โค้ดพังหมดแล้ว เดี๋ยวผมสร้างใหม่ด้วย **Rust** นะ!'\n💥 งานมึงหายไป {damage}% !!"
            self.sanity -= 5
            
        elif boss == "Gemini โควต้าหมด":
            damage = random.randint(15, 25) 
            self.sanity -= damage
            log_msg += f"\n🤖 Gemini: 'Limit Reached! สมัคร Premium สิสัส!'\n💰 มี Billing Pop-up เด้งมา! สติมึงหาย {damage} หน่วย!!"
            
        elif boss == "GPT เอ๋อแดก":
            damage = random.randint(10, 25) 
            self.sanity -= damage
            log_msg += f"\n🤖 GPT: 'โค้ดที่ให้ไปเข้าสู่ **Infinite Recursion** แล้ว!'\n💥 มึงเสียสติในการ Debug ไป {damage} หน่วย!!"
            
        return log_msg

# --- Game App (GUI พร้อม Animation และ Bugfix V8) ---
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
        tk.Label(self.master, text="--- Turn Log (เหตุการณ์ล่าสุด) ---", font=("Arial", 10)).pack(pady=(10,0))
        self.log_text = tk.Text(self.master, height=12, width=65, state=tk.DISABLED, wrap=tk.WORD, 
                                font=("Consolas", 11), bg="#1e1e1e", fg="#00FF00")
        self.log_text.pack(pady=5)

        # Button Frame
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=20)

        # ปุ่ม 1, 2, 3
        self.btn_code = tk.Button(self.button_frame, text="1. ⌨️ ปั่นโค้ด", command=lambda: self.start_turn("code"), 
                  width=15, height=2, bg="#D4F0CC", font=("Arial", 11, "bold"))
        self.btn_code.pack(side=tk.LEFT, padx=10)
        
        self.btn_google = tk.Button(self.button_frame, text="2. 🔍 หาข้อมูล", command=lambda: self.start_turn("google"), 
                  width=15, height=2, bg="#CCE4F0", font=("Arial", 11, "bold"))
        self.btn_google.pack(side=tk.LEFT, padx=10)
        
        self.btn_coffee = tk.Button(self.button_frame, text="3. ☕ แดกกาแฟ", command=lambda: self.start_turn("coffee"), 
                  width=15, height=2, bg="#F0CCCC", font=("Arial", 11, "bold"))
        self.btn_coffee.pack(side=tk.LEFT, padx=10)

        # **ปุ่มล่องหน: สำหรับ TROLL โดยเฉพาะ!**
        self.btn_troll = tk.Button(self.button_frame, text="4. 🤫", command=lambda: self.start_turn("troll"),
                                   width=4, height=2, bg="#333333", fg="#333333", borderwidth=0, 
                                   activebackground="#333333", activeforeground="#333333")
        self.btn_troll.pack(side=tk.LEFT, padx=2) 


    def update_status(self):
        # อัปเดตสีตามค่าสถานะ
        sanity_color = "red" if self.player.sanity < 30 else "black"
        self.sanity_label.config(text=f"🧠 สติ: {self.player.sanity}/100", fg=sanity_color)
        self.progress_label.config(text=f"💻 งาน: {self.player.progress}%")
        
        # เปลี่ยน Text บนปุ่มกาแฟถ้ากาแฟหมด
        if self.player.coffee == 0:
            self.btn_coffee.config(text="3. 💧 แดกน้ำเปล่า", bg="#EEEEEE")
            self.coffee_label.config(text=f"💧 น้ำเปล่า x{self.player.water_count}")
        else:
            self.btn_coffee.config(text="3. ☕ แดกกาแฟ", bg="#F0CCCC")
            self.coffee_label.config(text=f"☕ กาแฟ: {self.player.coffee} แก้ว")

    def set_buttons_state(self, state):
        self.btn_code.config(state=state)
        self.btn_google.config(state=state)
        self.btn_coffee.config(state=state)
        self.btn_troll.config(state=state) 

    # --- Animation Logic (เหมือนเดิม) ---
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

    # --- Turn Execution (แก้ไข Logic AI) ---
    def start_turn(self, action):
        if self.is_animating: return
        
        self.is_animating = True
        self.set_buttons_state(tk.DISABLED)
        
        # 1. Clear Log เก่าทิ้ง
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete('1.0', tk.END)
        self.log_text.config(state=tk.DISABLED)

        # 2. คำนวณผลลัพธ์ของ Player
        player_msg = ""
        is_safe_turn = False 

        if action == "code":
            player_msg = self.player.code()
        elif action == "google":
            player_msg = self.player.google_stack()
        elif action == "coffee":
            player_msg = self.player.drink_coffee()
            # is_safe_turn จะเป็น True ก็ต่อเมื่อ action คือ 'coffee' และยังเหลือกาแฟจริงๆ
            if "☕ ซดกาแฟเซเว่น" in player_msg: 
                is_safe_turn = True 
        elif action == "troll":
            player_msg = "❌ มึงกดเหี้ยไรเนี่ย เสียเทิร์นฟรีๆ เลยไอ้ควาย! (เพราะมึงอยากโดนด่า)"
            
        self.message_queue.append(player_msg)

        # 3. คำนวณผลลัพธ์ AI (FIXED LOGIC)
        if self.player.progress < 100 and self.player.sanity > 0 and not action == "troll":
             
             if is_safe_turn:
                # FIX: ถ้าเป็น Safe Zone (ดื่มกาแฟจริง) ให้ข้าม AI Check ไปเลย
                self.message_queue.append("🧘 สบายใจ! การดื่มกาแฟทำให้มึงอยู่ใน Safe Zone! AI ไม่กล้ากวน!")
                
             else:
                # Normal Risk (Code, Google, Water, หรือ No-Real-Coffee)
                # 🔴 ปรับลดโอกาส AI โจมตีเป็น 60%
                if random.random() < 0.6:
                    ai_msg = self.player.ai_attack()
                    for line in ai_msg.split('\n'):
                        self.message_queue.append(line)
                else:
                    self.message_queue.append("✨ โชคดี! รอบนี้ AI ไม่กวนตีนมึง")


        # 4. เริ่มกระบวนการ Animate
        self.process_message_queue()

    def check_game_end(self):
        if self.player.progress >= 100:
            messagebox.showinfo("YOU WIN!", "🎉🎉 เชรดดดด! มึงเขียนโค้ดเสร็จแล้ว! Vibe Coding สำเร็จ!")
            self.master.quit()
        elif self.player.sanity <= 0:
            messagebox.showerror("GAME OVER!", "💀 มึงสติแตกตายคาคอม... โดน AI ป่วนจนเป็นบ้า RIP.")
            self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()