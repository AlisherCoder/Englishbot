import colorama
from colorama import Fore, Style
import os
import time
def clear_screen():
    os.system('cls')

colorama.init(autoreset=True)

print(Fore.CYAN + "Onlayn Bozoriga Xush Kelibsiz")

class Market:
    def __init__(self, nom) -> None:
        self.nom = nom
        self.mahsulotlar = []

    def mahsulot_qoshish(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def mahsulot_ochirish(self, nom):
        for mahsulot in self.mahsulotlar:
            if mahsulot.nom == nom:
                tasdiqlash = input(Fore.RED + f"{nom}ni o'chirishni tasdiqlaysizmi? (HA/YO'Q): ")
                if tasdiqlash.lower() == 'ha':
                    self.mahsulotlar.remove(mahsulot)
                    print(Fore.RED + f"{nom} o'chirildi.")
                else:
                    print(Fore.YELLOW + f"{nom} o'chirilmadi.")
                return
        print(Fore.YELLOW + f"{nom} topilmadi.")

    def mahsulot_yangilash(self, nom, narx, kg):
        for mahsulot in self.mahsulotlar:
            if mahsulot.nom == nom:
                mahsulot.narx = narx
                mahsulot.kg = kg
                print(Fore.GREEN + f"{nom} yangilandi.")
                return
        print(Fore.YELLOW + f"{nom} topilmadi.")

    def mahsulotlar_korsatish(self):
        if not self.mahsulotlar:
            print(Fore.RED + "Mahsulotlar mavjud emas.")
        else:
            for mahsulot in self.mahsulotlar:
                print(Fore.MAGENTA + mahsulot.info())
        print("")

    def mahsulot_by_id(self, id):
        for mahsulot in self.mahsulotlar:
            if mahsulot.id == id:
                print(Fore.MAGENTA + mahsulot.info())
                return
        print(Fore.YELLOW + f"{id} IDli mahsulot topilmadi.")

class Mahsulot:
    def __init__(self, nom, narx, id, kg) -> None:
        self.nom = nom
        self.narx = narx
        self.id = id
        self.kg = kg

    def info(self):
        return f"Nomi: {self.nom} Narxi: {self.narx} ID: {self.id} Kg: {self.kg}"

market = Market("Uzum")

class Admin:
    def __init__(self, foydalanuvchi, parol):
        self.foydalanuvchi = foydalanuvchi
        self.parol = parol

    def admin_tekshirish(self):
        if self.foydalanuvchi in admin_royxati and self.parol == "1234":
            return True
        return False

admin_royxati = ["Bunyod", "Alisher", "Rustam"]

def print_header(text):
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print(Fore.CYAN + Style.BRIGHT + text.center(40))
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)

def print_menu(options):
    for i, option in enumerate(options, 1):
        print(Fore.GREEN + f"[{i}] {option}")

def admin_panel():
    while True:
        clear_screen()
        print_header("Admin Paneli")
        print_menu([
            "Mahsulot qo'shish", "Mahsulot o'chirish",
            "Mahsulotni yangilash", "Mahsulotlarni ko'rish",
            "ID orqali mahsulotni ko'rish", "Chiqish"
        ])
        
        tanlov = int(input(">>>> "))
        match tanlov:
            case 1:
                while True:
                    nom = input("Mahsulot nomini kiriting: ")
                    narx = float(input("Narxni kiriting: "))
                    id = int(input("ID ni kiriting: "))
                    kg = float(input("Kg ni kiriting: "))
                    mahsulot = Mahsulot(nom, narx, id, kg)
                    market.mahsulot_qoshish(mahsulot)
                    yana = input("Yana mahsulot qo'shasizmi? [HA/YO'Q] ")
                    if yana.lower() == "yo'q":
                        break
            case 2:
                nom = input("O'chiriladigan mahsulot nomini kiriting: ")
                market.mahsulot_ochirish(nom)
            case 3:
                nom = input("Mahsulot nomini kiriting: ")
                narx = float(input("Yangi narxni kiriting: "))
                kg = float(input("Yangi kg ni kiriting: "))
                market.mahsulot_yangilash(nom, narx, kg)
            case 4:
                market.mahsulotlar_korsatish()
            case 5:
                id = int(input("Mahsulot ID sini kiriting: "))
                market.mahsulot_by_id(id)
            case 6:
                break
        time.sleep(2)

def user_panel():
    profillar = []
    keyingi_id = 1
    savatcha = []

    def menu():
        print_header("Foydalanuvchi Menyusi")
        print_menu(["Profil yaratish", "Profilga kirish"])
        tanlov = int(input("Menyudan tanlang: "))
        match tanlov:
            case 1:
                profil_yaratish()
            case 2:
                profilga_kirish()

    def profil_yaratish():
        nonlocal keyingi_id
        profil = {
            'ism': input("Ismingizni kiriting: "),
            'familiya': input("Familiyangizni kiriting: "),
            'telefon': int(input("Telefon raqamingizni kiriting: +998 ")),
            'id': keyingi_id
        }
        profillar.append(profil)
        keyingi_id += 1
        print(Fore.GREEN + "Profil yaratildi!")
        menu()

    def profilga_kirish():
        login_id = int(input("Profil ID ni kiriting: "))
        for profil in profillar:
            if profil['id'] == login_id:
                profil_boshqaruvi(profil)
                return
        print(Fore.RED + "Bunday ID mavjud emas!")
        menu()

    def profil_boshqaruvi(profil):
        while True:
            print_header("Profil Boshqaruvi")
            print_menu(["Ma'lumotlarni yangilash", "Mahsulotlarni ko'rish", "Buyurtma berish", "Chiqish"])
            tanlov = int(input("Menyu tanlang: "))
            match tanlov:
                case 1:
                    profil['ism'] = input("Ismingizni kiriting: ")
                    profil['familiya'] = input("Familiyangizni kiriting: ")
                    profil['telefon'] = int(input("Telefon raqamingizni kiriting: +998 "))
                    print(Fore.GREEN + "Profil yangilandi.")
                case 2:
                    market.mahsulotlar_korsatish()
                case 3:
                    buyurtma_berish()
                case 4:
                    return

    def buyurtma_berish():
        market.mahsulotlar_korsatish()
        mahsulot_id = int(input("Buyurtma berish uchun mahsulot ID sini kiriting: "))
        for mahsulot in market.mahsulotlar:
            if mahsulot.id == mahsulot_id:
                manzil = input("Uy manzilini kiriting: ")
                tolov_usuli = input("To'lov usulini kiriting (NAXD/KART): ")
                if tolov_usuli.upper() in ["NAXD", "KART"]:
                    print(Fore.GREEN + f"{mahsulot.nom} uchun buyurtma berildi.")
                    print(Fore.GREEN + f"Manzil: {manzil}")
                    print(Fore.GREEN + f"To'lov usuli: {tolov_usuli}")
                    savatcha.append(mahsulot)
                    return
                else:
                    print(Fore.RED + "Noto'g'ri to'lov usuli kiritildi.")
                    return
        print(Fore.RED + "Bunday IDli mahsulot mavjud emas.")

    menu()

while True:
    clear_screen()
    print_header("Asosiy Menyu")
    print_menu(["Admin uchun", "Foydalanuvchi uchun"])
    time.sleep(1)
    tanlov = int(input(">>> "))
    if tanlov == 1:
        foydalanuvchi = input("Foydalanuvchi nomini kiriting: ")
        parol = input("Parolni kiriting: ")
        admin = Admin(foydalanuvchi, parol)
        if admin.admin_tekshirish():
            admin_panel()
        else:
            print(Fore.RED + "Foydalanuvchi nomi yoki parol noto'g'ri.")
    elif tanlov == 2:
        user_panel()
