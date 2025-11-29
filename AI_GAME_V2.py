import random
import time
import sys
import os

# --- ⚙️ CONFIG: ตั้งค่าความยากง่ายตรงนี้ (เหมือนกับ V9.1 GUI) ---
DIFFICULTY_SETTINGS = {
    "Easy": {
        "name": "โหมด Easy (อนุบาล)",
        "prog_min": 15, "prog_max": 30,  
        "heal_min": 15, "heal_max": 30,  
        "ai_chance": 0.3,                
        "dmg_mult": 0.5                  
    },
    "Normal": {
        "name": "โหมด Normal (คนปกติ)",
        "prog_min": 10, "prog_max": 20,
        "heal_min": 10, "heal_max": 25,
        "ai_chance": 0.5,                
        "dmg_mult": 0.8                  
    },
    "Hard": {
        "name": "โหมด Hard (ชีวิตจริง)",
        "prog_min": 8, "prog_max": 18,
        "heal_min": 5, "heal_max": 15,
        "ai_chance": 0.7,                
        "dmg_mult": 1.0                  
    },
    "God": {
        "name": "โหมด มึงตลกเหรอวะ (God Slayer)",
        "prog_min": 1, "prog_max": 5,    
        "heal_min": 1, "heal_max": 5,    
        "ai_chance": 0.95,               
        "dmg_mult": 2.0                  
    }
}

# ฟังก์ชันพิมพ์แบบเท่ๆ (ช้าๆ ให้ลุ้น)
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    # ใช้ 'cls' สำหรับ Windows และ 'clear' สำหรับ Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

# --- DevWarrior Class (ปรับใช้ Settings) ---
class DevWarrior:
    def __init__(self, difficulty="Normal"):
        self.difficulty = difficulty
        self.settings = DIFFICULTY_SETTINGS[difficulty]
        self.name = "ไอ้หนุ่มซินตึ๊ง"
        self.sanity = 100 
        self.progress = 0 
        self.coffee = 3 
        self.water_count = 0 

    def status(self):
        print(f"\n========================================")
        print(f"👤 Player: {self.name} (Difficulty: {self.settings['name']})")
        print(f"🧠 Sanity (สติ): {self.sanity}/100")
        print(f"💻 Progress (งาน): {self.progress}% เสร็จ")
        
        coffee_display = f"☕ Coffee: {self.coffee} แก้ว"
        if self.coffee == 0:
             coffee_display = f"💧 Water: {self.water_count} ครั้ง"
             
        print(f"📦 Items: {coffee_display}")
        print(f"========================================\n")

    def code(self):
        s = self.settings
        gain = random.randint(s["prog_min"], s["prog_max"]) 
        self.progress += gain
        slow_print(f"⌨️  มึงปั่นโค้ด... งานเดินไป {gain}% !!")
        if self.progress > 100: self.progress = 100
        return "code" 

    def google_stack(self):
        s = self.settings
        heal = random.randint(s["heal_min"], s["heal_max"]) 
        self.sanity += heal
        slow_print(f"🔍 มึงไปหาข้อมูล... สติกลับมา {heal} หน่วย")
        if self.sanity > 100: self.sanity = 100
        return "google"

    def drink_coffee(self):
        if self.coffee > 0:
            self.coffee -= 1
            self.sanity += 40
            slow_print(f"☕ ซดกาแฟเซเว่น... ดีดจัด!! สติเพิ่ม 40 หน่วย! (เหลือ {self.coffee} แก้ว)")
            if self.sanity > 100: self.sanity = 100
            return True 
        else:
            self.water_count += 1
            s = self.settings
            heal = random.randint(s["heal_min"] // 2, s["heal_max"] // 2)
            if heal < 1: heal = 1
            self.sanity += heal
            if self.sanity > 100: self.sanity = 100
            slow_print(f"💧 กาแฟหมด! แดกน้ำเปล่าแทน... ฟื้นฟูสติ {heal} หน่วย")
            return False 

def ai_attack(player):
    s = player.settings
    ai_list = ["Claude ขี้ขอโทษ", "Gemini โควต้าหมด", "GPT เอ๋อแดก"]
    boss = random.choice(ai_list)
    
    print(f"\n⚠️  {boss} โผล่มาขัดจังหวะมึง!!")
    time.sleep(1)

    base_dmg = random.randint(15, 25)
    final_dmg = int(base_dmg * s["dmg_mult"])

    if boss == "Claude ขี้ขอโทษ":
        player.progress -= final_dmg
        if player.progress < 0: player.progress = 0
        slow_print(f"🤖 Claude: 'ขอโทษครับ โค้ดตะกี้พังหมดเลย...' (ลบโค้ดมึงทิ้ง)")
        slow_print(f"💥 งานมึงหายไป {final_dmg}% !!")
        player.sanity -= 5 
        

    elif boss == "Gemini โควต้าหมด":
        player.sanity -= final_dmg
        slow_print(f"🤖 Gemini: 'Limit Reached! สมัคร Premium สิสัส!'")
        slow_print(f"💥 มึงหัวร้อนจนเสียสติไป {final_dmg} หน่วย!!")

    elif boss == "GPT เอ๋อแดก":
        damage = int(final_dmg * 0.7) 
        player.sanity -= damage
        slow_print(f"🤖 GPT: 'asdf jkl; error 404 logic not found...'")
        slow_print(f"💫 มึงนั่งงงกับคำตอบมันจนเสียเวลา สติหาย {damage} หน่วย!!")
        
    time.sleep(1)


def difficulty_selection():
    clear_screen()
    slow_print("--- เลือกความยากของชีวิตมึง ---", delay=0.01)
    
    modes_list = list(DIFFICULTY_SETTINGS.keys())
    
    for i, mode_key in enumerate(modes_list):
        settings = DIFFICULTY_SETTINGS[mode_key]
        print(f"{i+1}. {settings['name']} (AI Chance: {int(settings['ai_chance']*100)}%)")

    while True:
        try:
            choice = input("\nเลือกตัวเลข (1-4): ")
            index = int(choice) - 1
            
            if 0 <= index < len(modes_list):
                return modes_list[index]
            else:
                slow_print(f"💢 **มึงเลือกเหี้ยอะไรเนี่ยยย!** {choice} ไม่มีในตัวเลือกโว้ยไอ้ควาย! ลองใหม่!")
                time.sleep(1)

        except ValueError:
            slow_print("💢 **มึงเลือกเหี้ยอะไรเนี่ยยย!** ใส่แต่ตัวเลขโว้ยไอ้สัส! ลองใหม่!")
            time.sleep(1)

# --- GAME LOOP ---
def game_loop():
    chosen_difficulty = difficulty_selection()
    
    clear_screen()
    slow_print(f"🔥 เริ่มเกมโหมด: {DIFFICULTY_SETTINGS[chosen_difficulty]['name']} 🔥")
    slow_print("ภารกิจ: เขียนโค้ดให้เสร็จก่อนที่ AI จะทำให้มึงเป็นบ้า...")
    time.sleep(1)

    player = DevWarrior(chosen_difficulty)

    while player.progress < 100 and player.sanity > 0:
        player.status()
        
        is_safe_turn = False
        
        print("เลือกการกระทำ:")
        print("1. ⌨️  ปั่นโค้ด (เพิ่ม Progress)")
        print("2. 🔍 หาข้อมูล (เพิ่ม Sanity)")
        print("3. ☕ แดกกาแฟ (เพิ่ม Sanity เยอะ/น้ำเปล่า)")
        print("0. 🛑 ออกจากเกม (จบละไอ้สัส ทำไมวะ อย่าออกเลย ทำไมต้องออก ทำไมต้องออก ทำไมต้องออก ทำไมต้องออก)")
        
        choice = input("\nเลือกมา (0-3): ")

        if choice == '1':
            player.code()
        elif choice == '2':
            player.google_stack()
        elif choice == '3':
            is_safe_turn = player.drink_coffee() 
        elif choice == '0':
            slow_print("\nยอมแพ้? โธ่เอ้ยย เกมง่ายๆ มึงก็ยอมแพ้ละ! 🤣")
            break
        else:
            slow_print("❌ มึงกดเหี้ยไรเนี่ย เสียเทิร์นฟรีๆ เลยไอ้ควาย!")
        
        time.sleep(1)
        
        # 4. AI สวนกลับ
        if player.progress < 100 and player.sanity > 0:
            
            if is_safe_turn:
                slow_print("\n🧘 Safe Zone! กาแฟช่วยชีวิต!")
                
            else:
                chance = player.settings['ai_chance']
                if random.random() < chance:
                    ai_attack(player)
                else:
                    slow_print("\n✨ โชคดี! รอบนี้ AI ไม่กวนตีนมึง")
        
        if player.sanity <= 0: break
        
        input("\n[กด Enter เพื่อไปต่อ...]")
        clear_screen()

    # --- GAME OVER / WIN ---
    player.status()
    if player.progress >= 100:
        if player.difficulty == "God":
            slow_print("\n🏆🏆 มึงมันเทพเจ้า! ชนะโหมดนรกแตกได้ไงวะ! 🏆🏆")
            slow_print("มึงเอาโล่ไปเลยไอ้สัส!")
        else:
            slow_print("\n🎉🎉 เชรดดดด! มึงเขียนโค้ดเสร็จแล้ว! 🎉🎉")
            slow_print("มึงเอาชนะเหล่า AI ปัญญาอ่อนพวกนี้ได้! ไปนอนได้แล้วเพื่อน!")
    elif player.sanity <= 0:
        slow_print("\n💀💀 GAME OVER 💀💀")
        slow_print("มึงสติแตกตายคาคอม... AI ครองโลกสำเร็จ")
        slow_print("RIP.")

    time.sleep(3)
    
    # --- แก้ไขตรงนี้: เพิ่มการวนลูปด่าจนกว่าจะกด y/n ---
    while True:
        try_again = input("\nอยากลองอีกรอบไหม? (y/n): ").lower()
        if try_again == 'y':
            game_loop()
            break # ออกจากลูปด่า
        elif try_again == 'n':
            clear_screen()
            slow_print("ไปพักผ่อนซะเพื่อน! ไว้มาสู้กันใหม่!")
            break # ออกจากลูปด่า
        else:
            slow_print("💢 **กูถามแค่ y หรือ n ไอ้สาสเอ้ยยยย!** มึงจะเล่นต่อ (y) หรือเลิก (n)!? ลองพิมพ์ใหม่ดีๆ!")
            time.sleep(1)
            
if __name__ == "__main__":
    game_loop()