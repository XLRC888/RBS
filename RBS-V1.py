
# Made by XLRC888
print("Random Battle Simulator (RBS) V1")
import random
import math
import time
#goddamn it its nearly 3 am and im so tired
runsuccessplayerhard = 4

currentrunfailenemy = 0
currentrunsuccessplayer = 0
currentrunfailplayer = 0
currentchanceenemyrun = 0
currentchanceplayerattack = 0
currentchanceenemyattack = 0
currentenemydmg = 0
currentplayerdmg = 0

easyenemydmg = 5
mediumenemydmg = 15
hardenemydmg = 25

easyplayerdmg = 25
mediumplayerdmg = 15
hardplayerdmg = 5

easychanceplayerattack = 2
mediumchanceplayerattack = 4
hardchanceplayerattack = 7

easychanceenemyattack = 7
mediumchanceenemyattack = 4
hardchanceenemyattack = 2

easychanceenemyrun = 7
mediumchanceenemyrun = 4
hardchanceenemyrun = 2

runfailplayereasy = 5 #dmg for player
runfailplayermedium = 15 #dmg for player
runfailplayerhard = 25 #dmg for player

runfailenemyeasy = 25 #dmg for enemy
runfailenemymedium = 15 #dmg for enemy
runfailenemyhard = 5 #dmg for enemy

user_hpstart = 100
enemy_hpstart = 100
user_hp = 100
enemy_hp = 100
enemytookdmg = enemy_hpstart - enemy_hp
usertookdmg = user_hpstart - user_hp

def close():
    time.sleep(3)
    print("Closing in 5...")
    time.sleep(1)
    print("Closing in 4...")
    time.sleep(1)
    print("Closing in 3...")
    time.sleep(1)
    print("Closing in 2...")
    time.sleep(1)
    print("Closing in 1...")
    time.sleep(1)

while True:
    difficulty = input("Choose your difficulty (easy, medium, hard): ")
    if difficulty.lower() == "easy":
        user_hp = 150
        user_hpstart = 150
        enemy_hp = 75
        enemy_hpstart = 75
        print("You have chosen easy difficulty! You have 150 HP and the enemy has 75 HP.")
        currentrunfailplayer = runfailplayereasy
        currentrunsuccessplayer = 2
        currentrunfailenemy = runfailenemyeasy
        currentchanceenemyrun = easychanceenemyrun
        currentchanceplayerattack = easychanceplayerattack
        currentchanceenemyattack = easychanceenemyattack
        currentplayerdmg = easyplayerdmg
        currentenemydmg = easyenemydmg
        break
    elif difficulty.lower() == "medium":
        user_hp = 100
        user_hpstart = 100
        enemy_hp = 100
        enemy_hpstart = 100
        print("You have chosen medium difficulty! You have 100 HP and the enemy has 100 HP.")
        currentrunfailplayer = runfailplayermedium
        currentrunsuccessplayer = 2
        currentrunfailenemy = runfailenemymedium
        currentchanceenemyrun = mediumchanceenemyrun
        currentchanceplayerattack = mediumchanceplayerattack
        currentchanceenemy = mediumchanceenemyattack
        currentplayerdmg = mediumplayerdmg
        currentenemydmg = mediumenemydmg
        break
    elif difficulty.lower() == "hard":
        user_hp = 75
        user_hpstart = 75
        enemy_hp = 150
        enemy_hpstart = 150
        print("You have chosen hard difficulty! You have 75 HP and the enemy has 150 HP.")
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
    print("[❤️] Enemy's HP:", enemy_hp, ",", "Your HP:", user_hp)
    if enemy_hp <= 0:
                print("[🎉] You've defeated the", enemy+"!")
                close()

def player_run():
    global user_hp
    random_chanceplayerrun = random.randint(1, currentrunsuccessplayer)
    if random_chanceplayerrun == 1:
        print("[✅] You safely ran away!")
        print(enemytookdmg, "damage was dealt to the enemy before you ran away.")
        print(usertookdmg, "damage was dealt to you before you ran away.")
        close()
    else:
        print("[‼️] You failed to run away and got caught! The enemy dealt", currentrunfailplayer, "damage to you")
        user_hp -= currentrunfailplayer
        hps()

def enemy_run():
    global enemy_hp
    random_chanceenemyrun = random.randint(1, currentchanceenemyrun)
    if random_chanceenemyrun == 1:
        print("[‼️] The enemy ran away safely!")
        close()
    else:
        print("[✅️] The enemy tried to run away but failed! You dealt", currentrunfailenemy, "damage to the enemy")
        enemy_hp -= currentrunfailenemy
        hps()


def enemy_attack():
    global user_hp
    random_chanceenemyattack = random.randint(1, currentchanceenemyattack)
    if random_chanceenemyattack == 1:
        print("[‼️] The enemy succesfully attacked you, it dealt", currentenemydmg, "damage to you")
        user_hp -= currentenemydmg
        hps()
    else:
        print("[✅️] The enemy tried to attack you, succesfully dodged the enemy's attack")

def player_attack():
    global enemy_hp
    random_chanceattack = random.randint(1, currentchanceplayerattack)
    if random_chanceattack == 1:
        print("[✅] You succesfully attacked, it dealt", currentplayerdmg, "damage to the enemy")
        enemy_hp -= currentplayerdmg
        hps()
    else:
        print("[⚠️] The enemy dodged your attack")

enemy_list = ["Snaggit", "Kruk", "Fizznox", "Grubbit", "Gutmire", "Rotshuffler", "Deadrick", "Plagueborn", "Rattclaw", "Marrowjack", "Bonescourge", "Skellion",  "Dravok", "Emberfang", "Vyrthul", "Kaelrex"] 
enemy = random.choice(enemy_list)
article = "an" if enemy[0].lower() in "aeiou" else "a"
print("You've come across", article, "wild", enemy+"!")
while True:
    raw = input("What will you do? (type help for the inputs): ")
    if raw.lower() == "attack":
        player_attack()
        random_chanceenemyrun = random.randint(1, currentchanceenemyrun)
        if random_chanceenemyrun == 1:
            enemy_run()
            break
        else:
            enemy_attack()
        if user_hp <= 0:
                print("[💀] You've been defeated!")
                close()
                break

        if enemy_hp <= 0:
                print("[🎉] You've defeated the", enemy+"!")
                close()
                break
    elif raw.lower() == ["hp", "hps", "health", "status"]:
        hps()
    
    elif raw.lower() == "run":
        player_run()
        if user_hp <= 0:
                print("[💀] You've been defeated!")
                close()
                break
        
    elif raw.lower() == "help":
        print("Available commands: attack, run, hp/status/hps/health, help (You can type help <command> for more info on a command)")
    elif raw.lower() == "help attack":
        print("attack - Attempt to deal damage to the enemy. Success chance and damage depends on difficulty.")
    elif raw.lower() == "help run":
        print("run - Attempt to flee from the battle. Success chance depends on difficulty.")
    elif raw.lower() in ["help hp", "help hps", "help health", "help status"]:
        print("hp/status/hps/health - Check the current HP of you and the enemy.")
    elif raw.lower() == "help help":
        print("help - Show this help message. You can also type help <command> for more info on a specific command.")
    else:
        print("[❓] Unknown move, try something like 'attack'")