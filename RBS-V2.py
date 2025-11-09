# Made by XLRC888
print("Random Battle Simulator (RBS) V2")
import random
import time

runsuccessplayerhard = 4
currentrunfailenemy = 0
currentrunsuccessplayer = 0
currentrunfailplayer = 0
currentchanceenemyrun = 0
currentchanceplayerattack = 0
currentchanceenemyattack = 0
currentenemydmg = 0
currentplayerdmg = 0

easyenemydmg = 8
mediumenemydmg = 14
hardenemydmg = 20

easyplayerdmg = 22
mediumplayerdmg = 18
hardplayerdmg = 13

easychanceplayerattack = 3
mediumchanceplayerattack = 4
hardchanceplayerattack = 5

easychanceenemyattack = 4
mediumchanceenemyattack = 3
hardchanceenemyattack = 2

easychanceenemyrun = 5
mediumchanceenemyrun = 4
hardchanceenemyrun = 3

runfailplayereasy = 8
runfailplayermedium = 12
runfailplayerhard = 18

runfailenemyeasy = 18
runfailenemymedium = 12
runfailenemyhard = 8

user_hpstart = 100
enemy_hpstart = 100
user_hp = 100
enemy_hp = 100
enemytookdmg = enemy_hpstart - enemy_hp
usertookdmg = user_hpstart - user_hp

def close():
    time.sleep(3)
    print("Closing in 5...")
    for i in range(4, 0, -1):
        time.sleep(1)
        print(f"Closing in {i}...")

def user_defeated():
    if user_hp <= 0:
        print("[💀] You've been defeated!")
        close()

def enemy_defeated():
    if enemy_hp <= 0:
        print(f"[🎉] You've defeated the {enemy}!")
        close()

while True:
    difficulty = input("Choose your difficulty (easy, medium, hard): ").lower()
    if difficulty == "easy":
        user_hp = user_hpstart = 150
        enemy_hp = enemy_hpstart = 80
        print("You have chosen easy difficulty! You have 150 HP and the enemy has 80 HP.")
        currentrunfailplayer = runfailplayereasy
        currentrunsuccessplayer = 2
        currentrunfailenemy = runfailenemyeasy
        currentchanceenemyrun = easychanceenemyrun
        currentchanceplayerattack = easychanceplayerattack
        currentchanceenemyattack = easychanceenemyattack
        currentplayerdmg = easyplayerdmg
        currentenemydmg = easyenemydmg
        break
    elif difficulty == "medium":
        user_hp = user_hpstart = 120
        enemy_hp = enemy_hpstart = 120
        print("You have chosen medium difficulty! You have 120 HP and the enemy has 120 HP.")
        currentrunfailplayer = runfailplayermedium
        currentrunsuccessplayer = 2
        currentrunfailenemy = runfailenemymedium
        currentchanceenemyrun = mediumchanceenemyrun
        currentchanceplayerattack = mediumchanceplayerattack
        currentchanceenemyattack = mediumchanceenemyattack
        currentplayerdmg = mediumplayerdmg
        currentenemydmg = mediumenemydmg
        break
    elif difficulty == "hard":
        user_hp = user_hpstart = 100
        enemy_hp = enemy_hpstart = 160
        print("You have chosen hard difficulty! You have 100 HP and the enemy has 160 HP.")
        currentrunfailplayer = runfailplayerhard
        currentrunsuccessplayer = runsuccessplayerhard
        currentrunfailenemy = runfailenemyhard
        currentchanceenemyrun = hardchanceenemyrun
        currentchanceplayerattack = hardchanceplayerattack
        currentchanceenemyattack = hardchanceenemyattack
        currentplayerdmg = hardplayerdmg
        currentenemydmg = hardenemydmg
        break
    else:
        print("[❓] Unknown difficulty")

def hps():
    if enemy_hp <= 0:
        print(f"[🎉] You've defeated the {enemy}!")
        close()
    elif user_hp <= 0:
        print("[💀] You've been defeated!")
        close()
    else:
        print(f"[❤️] Enemy's HP: {enemy_hp}, Your HP: {user_hp}")

def player_run():
    global user_hp
    if random.randint(1, currentrunsuccessplayer) == 1:
        print("[✅] You safely ran away!")
        print(f"{enemytookdmg} damage was dealt to the enemy before you ran away.")
        print(f"{usertookdmg} damage was dealt to you before you ran away.")
        close()
    else:
        print(f"[‼️] You failed to run away and got caught! The enemy dealt {currentrunfailplayer} damage to you")
        user_hp -= currentrunfailplayer
        hps()

def enemy_run():
    global enemy_hp
    if random.randint(1, currentchanceenemyrun) == 1:
        print("[‼️] The enemy ran away safely!")
        close()
        return True
    else:
        print(f"[✅️] The enemy tried to run away but failed! You dealt {currentrunfailenemy} damage to the enemy")
        enemy_hp -= currentrunfailenemy
        hps()
        return False

def enemy_attack():
    global user_hp
    if random.randint(1, currentchanceenemyattack) <= 2:
        print(f"[‼️] The enemy attacked you, dealing {currentenemydmg} damage!")
        user_hp -= currentenemydmg
        hps()
    else:
        print("[✅️] You dodged the enemy's attack!")

def player_attack():
    global enemy_hp
    if random.randint(1, currentchanceplayerattack) <= 2:
        print(f"[✅] You hit the enemy! It took {currentplayerdmg} damage.")
        enemy_hp -= currentplayerdmg
        hps()
    else:
        print("[⚠️] The enemy dodged your attack!")

enemy_list = [
    "Snaggit", "Kruk", "Fizznox", "Grubbit", "Gutmire", "Rotshuffler", "Deadrick", "Plagueborn", "Rattclaw", "Marrowjack",
    "Bonescourge", "Skellion", "Dravok", "Emberfang", "Vyrthul", "Kaelrex", "Murkfang", "Rotjaw", "Skulkrend", "Venmire",
    "Blightmaw", "Gnashroot", "Dripspine", "Festerclaw", "Grimewretch", "Crawlshade", "Pusgul", "Spinegnaw", "Moldreaper",
    "Scabvine", "Toxwretch", "Grubflare", "Oozeborn", "Rotsnare", "Dregthorn", "Wretchcoil"
]

enemy = random.choice(enemy_list)
article = "an" if enemy[0].lower() in "aeiou" else "a"
print(f"You've come across {article} wild {enemy}!")

while True:
    raw = input("What will you do? (type help for the inputs): ").lower()
    if raw == "attack":
        player_attack()

        if enemy_run():
            break
        else:
            enemy_attack()
            user_defeated()
        enemy_defeated()

    elif raw == "run":
        player_run()
        user_defeated()
        if user_hp > 0:
            continue
        else:
            break


    elif raw in ["hp", "hps", "health", "status"]:
        hps()

    elif raw == "help":
        print("Available commands: attack, run, hp/status/hps/health, help (You can type help <command> for more info on a command)")
    elif raw == "help attack":
        print("attack - Attempt to deal damage to the enemy. Success chance and damage depends on difficulty.")
    elif raw == "help run":
        print("run - Attempt to flee from the battle. Success chance depends on difficulty.")
    elif raw in ["help hp", "help hps", "help health", "help status"]:
        print("hp/status/hps/health - Check the current HP of you and the enemy.")
    elif raw == "help help":
        print("help - Show this help message. You can also type help <command> for more info on a specific command.")
    else:
        print("[❓] Unknown move, try something like 'attack'")
