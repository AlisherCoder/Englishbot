print("English botga xush kelibsiz!")

def add():
    fen = open('english.txt','a+')
    fuz = open('uzbek.txt','a+')
    while True:
        soz = input("So'zni kiriting. ")
        tar = input("Tarjimasini kiriting. ")
        fen.write(soz+'\n')
        fuz.write(tar+'\n')
        stop = input("Yana so'z qo'shasizmi?[Ha | Yoq] ")
        if stop.title() != "Ha":
            break
    fen.close()
    fuz.close()
def repetition():
    fen = open('english.txt','r')
    fuz = open('uzbek.txt','r')
    tar = fuz.read().splitlines()
    eng = fen.read().splitlines()

    while True:
        for i in range(len(eng)):
            s = input(f"{eng[i]} >>> ")
            if s == tar[i]:
                print("to'g'ri.")
            else:
                print("Noto'g'ri.")
        break
    fen.close()
    fuz.close()
while True:
    num = input("[1] Lug'at qo'shish.\n"
                "[2] Takrorlash.\n"
                "[0] Stop >>> ")
    match num:
        case '1':
            add()
        case '2':
            repetition()
        case '0':
            break

