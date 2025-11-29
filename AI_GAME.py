import random
import time
import sys
import os

# ฟังก์ชันพิมพ์แบบเท่ๆ (ช้าๆ ให้ลุ้น)
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
        self.name = "ไอ้หนุ่มซินตึ๊ง"
        self.sanity = 100  # ค่าสติ
        self.progress = 0  # งานที่เสร็จ
        self.coffee = 3    # ไอเทมเพิ่มเลือด

    def status(self):
        print(f"\n========================================")
        print(f"👤 Player: {self.name}")
        print(f"🧠 Sanity (สติ): {self.sanity}/100")
        print(f"💻 Progress (งาน): {self.progress}% เสร็จ")
        print(f"☕ Coffee Left: {self.coffee} แก้ว")
        print(f"========================================\n")

    def code(self):
        gain = random.randint(10, 25)
        self.progress += gain
        slow_print(f"⌨️  มึงพิมพ์โค้ดรัวๆ... งานเดินไป {gain}% !!")
        if self.progress > 100: self.progress = 100

    def google_stack(self):
        heal = random.randint(10, 20)
        self.sanity += heal
        slow_print(f"🔍 มึงไปก๊อปโค้ดชาวอินเดียใน StackOverflow... สติกลับมา {heal} หน่วย")
        if self.sanity > 100: self.sanity = 100

    def drink_coffee(self):
        if self.coffee > 0:
            self.coffee -= 1
            self.sanity += 40
            slow_print(f"☕ ซดกาแฟเซเว่น... ดีดจัด!! สติเพิ่ม 40 หน่วย!")
            if self.sanity > 100: self.sanity = 100
        else:
            slow_print(f"❌ กาแฟหมดแล้วไอ้เวร! มึงต้องสู้ด้วยน้ำเปล่า!")

def ai_attack(player):
    ai_list = ["Claude ขี้ขอโทษ", "Gemini โควต้าหมด", "GPT เอ๋อแดก"]
    boss = random.choice(ai_list)
    
    print(f"\n⚠️  {boss} โผล่มาขัดจังหวะมึง!!")
    time.sleep(1)

    if boss == "Claude ขี้ขอโทษ":
        damage = random.randint(10, 20)
        player.progress -= damage
        if player.progress < 0: player.progress = 0
        slow_print(f"🤖 Claude: 'ขอโทษครับ โค้ดตะกี้พังหมดเลย เดี๋ยวผมเขียนใหม่นะ' (ลบโค้ดมึงทิ้ง)")
        slow_print(f"💥 งานมึงหายไป {damage}% !!")

    elif boss == "Gemini โควต้าหมด":
        damage = random.randint(15, 25)
        player.sanity -= damage
        slow_print(f"🤖 Gemini: 'Limit Reached! สมัคร Premium สิสัส!'")
        slow_print(f"💥 มึงหัวร้อนจนเสียสติไป {damage} หน่วย!!")

    elif boss == "GPT เอ๋อแดก":
        slow_print(f"🤖 GPT: 'asdf jkl; error 404 logic not found...'")
        slow_print(f"💫 มึงนั่งงงกับคำตอบมัน เสียเวลาไปฟรีๆ 1 เทิร์น")
        # ไม่ลดเลือดแต่เสียเทิร์นฟรี

# --- GAME START ---
clear_screen()
slow_print("🔥 ยินดีต้อนรับสู่ 'The Desperate Dev' 🔥")
slow_print("ภารกิจ: เขียนโค้ดให้เสร็จก่อนที่ AI จะทำให้มึงเป็นบ้า...")
time.sleep(1)

player = DevWarrior()

while player.progress < 100 and player.sanity > 0:
    player.status()
    print("เลือกการกระทำ:")
    print("1. ⌨️  ปั่นโค้ด (เพิ่ม Progress, เสี่ยงโดนด่า)")
    print("2. 🔍 หาข้อมูล (เพิ่ม Sanity)")
    print("3. ☕ แดกกาแฟ (เพิ่ม Sanity เยอะ แต่มีจำกัด)")
    
    choice = input("\nเลือกมา (1-3): ")

    if choice == '1':
        player.code()
    elif choice == '2':
        player.google_stack()
    elif choice == '3':
        player.drink_coffee()
    else:
        slow_print("❌ มึงกดเหี้ยไรเนี่ย เสียเทิร์นฟรีๆ เลยไอ้ควาย!")
    
    time.sleep(1)
    
    # AI สวนกลับถ้างานยังไม่เสร็จ
    if player.progress < 100:
        if random.random() < 0.7: # โอกาสเจอ AI ป่วน 70%
            ai_attack(player)
        else:
            slow_print("\n✨ โชคดี! รอบนี้ AI ไม่กวนตีนมึง")
    
    input("\n[กด Enter เพื่อไปต่อ...]")
    clear_screen()

# --- GAME OVER / WIN ---
if player.progress >= 100:
    slow_print("\n🎉🎉 เชรดดดด! มึงเขียนโค้ดเสร็จแล้ว! 🎉🎉")
    slow_print("มึงเอาชนะเหล่า AI ปัญญาอ่อนพวกนี้ได้! ไปนอนได้แล้วเพื่อน!")
else:
    slow_print("\n💀💀 GAME OVER 💀💀")
    slow_print("มึงสติแตกตายคาคอม... AI ครองโลกสำเร็จ")
    slow_print("RIP.")