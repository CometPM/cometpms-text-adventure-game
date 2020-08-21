# Made by Peter Morgan (CometPM)
# Version 1

while True:

    loop=1

    while loop == 1:

        notfinished=True
        win=False

        characterchoice=input("Which character would you like to play as?(Dwarf/Human/Wizard) ").lower().strip()

        if characterchoice == "dwarf":
            startchoice=input("You chose 'Dwarf', a strong character who weilds an upgradable axe. Would you like to continue as a Dwarf?(yes/no) ").lower().strip()
            if startchoice == "no":
                loop=1
            else:
                character="dwarf"
                weaponname="axe"
                weapondamage=6
                weaponhitchance=75
                maxhealthpotions=3
                maxhp=12
                hp=12
                loop=0
        elif characterchoice == "wizard":
            startchoice=input("You chose 'Wizard', a weaker character who is able to cast spells. Would you like to continue as a Wizard?(yes/no) ").lower().strip()
            if startchoice == "no":
                loop=1
            else:
                character="wizard"
                weaponname="staff"
                weapondamage=4
                weaponhitchance=90
                maxhealthpotions=3
                maxhp=10
                hp=10
                loop=0
        else:
            startchoice=input("You chose 'Human', an average strength character who can hold more Health Potions and can pick up different weapons. Would you like to continue as a Human?(yes/no) ").lower().strip()
            if startchoice == "no":
                loop=1
            else:
                character="human"
                weaponname="sword"
                weapondamage=5
                weaponhitchance=75
                maxhealthpotions=5
                maxhp=11
                hp=11
                loop=0

    import random
    import time
    healthpotions=0
    critbattles=0
    fireballspell=0
    fireballspellused=0
    icespell=0
    icespellused=0
    lightningspell=0
    lightningspellused=0
    icespellactive=0
    lightningspellactive=0
    monstername="slime"
    monsterattack=1
    monsterhp=10
    monsterhitchance=90
    monstersslain=0
    increase=0
    bossnumber=0
    comfy=0

    print("You enter into a dark cave which is lit with laterns hanging from the wall so you are able to see a path forward. You may no longer turn back and the only way out is to venture forward.")
    time.sleep(3)
    print("You can carry {0} Health Potions, your weapon ({1}) does {2} damage, and your max HP is {3}.".format(maxhealthpotions,weaponname,weapondamage,maxhp))
    time.sleep(3)

    class slime():
        monstername="slime"
        monsterattack=1
        monsterhp=10
        monsterhitchance=90

    class bat():
        monstername="bat"
        monsterattack=2
        monsterhp=5
        monsterhitchance=70

    class goblin():
        monstername="goblin"
        monsterattack=3
        monsterhp=12
        monsterhitchance=70

    class wolf():
        monstername="wolf"
        monsterattack=4
        monsterhp=15
        monsterhitchance=80

    class orc():
        monstername="orc"
        monsterattack=5
        monsterhp=20
        monsterhitchance=60

    class wight():
        monstername="wight"
        monsterattack=5
        monsterhp=30
        monsterhitchance=85

    class hammer():
        weaponname="hammer"
        weapondamage=8
        weaponhitchance=70

    class bow():
        weaponname="bow"
        weapondamage=5
        weaponhitchance=95

    class mace():
        weaponname="mace"
        weapondamage=7
        weaponhitchance=75

    def fight():
        global monstername,monsterhp,monsterattack,monsterhitchance,hp,maxhp,healthpotions,weaponname,weapondamage,weaponhitchance,fireballspell,icespell,lightningspell,icespellactive,lightningspellactive,monstersslain,critbattles,fireballspellused,icespellused,lightningspellused,win,comfy
        x=0
        def playermove():
            global monstername,monsterhp,hp,maxhp,healthpotions,weaponname,weapondamage,weaponhitchance,fireballspell,icespell,lightningspell,icespellactive,lightningspellactive,monstersslain,critbattles,fireballspellused,icespellused,lightningspellused,win,comfy
            attack=input("Would you like to attack or use a potion?(attack/potion) ").lower().strip()
            if attack == "potion":
                if character == "wizard":
                    potion=input("Would you like to use a Health Potion, a Magic Potion or no potion?(Health/Magic/no) ").lower().strip()
                    if potion == "no":
                        rnumber=random.randint(1,100)
                        if 1 <= rnumber <= weaponhitchance:
                            if 1 <= rnumber <= 33 or critbattles > 0:
                                monsterhp-=weapondamage*1.5
                                print("Your next strike will deal critical damage.")
                                time.sleep(3)
                                print("Instead of using a potion, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage*1.5,monstername,monsterhp))
                                time.sleep(3)
                            else:
                                monsterhp-=weapondamage
                                print("Instead of using a potion, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage,monstername,monsterhp))
                                time.sleep(3)
                        else:
                            if weaponname == "bow":
                                print("You fired your bow but missed dealing 0 damage.")
                                time.sleep(3)
                            else:
                                print("You swung your {0} but missed dealing 0 damage.".format(weaponname))
                                time.sleep(3)
                    elif potion == "health" and healthpotions == 0:
                        rnumber=random.randint(1,100)
                        if 1 <= rnumber <= weaponhitchance:
                            if 1 <= rnumber <= 33 or critbattles > 0:
                                monsterhp-=weapondamage*1.5
                                print("Your next strike will deal critical damage.")
                                time.sleep(3)
                                print("Because you have no Health Potions, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage*1.5,monstername,monsterhp))
                                time.sleep(3)
                            else:
                                monsterhp-=weapondamage
                                print("Because you have no Health Potions, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage,monstername,monsterhp))
                                time.sleep(3)
                        else:
                            if weaponname == "bow":
                                print("You fired your bow but missed dealing 0 damage.")
                                time.sleep(3)
                            else:
                                print("You swung your {0} but missed dealing 0 damage.".format(weaponname))
                                time.sleep(3)
                    elif potion == "health":
                        healthpotions-=1
                        hp=maxhp
                        print("You used a Health Potion ({0} remaining) restoring you hp to full ({1}).".format(healthpotions,maxhp))
                        time.sleep(3)
                    elif potion == "magic" and fireballspell == 0 and icespell == 0 and lightningspell == 0:
                        rnumber=random.randint(1,100)
                        if 1 <= rnumber <= weaponhitchance:
                            if 1 <= rnumber <= 33 or critbattles > 0:
                                monsterhp-=weapondamage*1.5
                                print("Your next strike will deal critical damage.")
                                time.sleep(3)
                                print("Because you have no Magic Potions, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage*1.5,monstername,monsterhp))
                                time.sleep(3)
                            else:
                                monsterhp-=weapondamage
                                print("Because you have no Magic Potions, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage,monstername,monsterhp))
                                time.sleep(3)
                        else:
                            if weaponname == "bow":
                                print("You fired your bow but missed dealing 0 damage.")
                                time.sleep(3)
                            else:
                                print("You swung your {0} but missed dealing 0 damage.".format(weaponname))
                                time.sleep(3)
                    else:
                        magicchoice=input("You have {0} Fireball spell(s), {1} Ice spell(s), and {2} Lightning spell(s). Which spell would you like to use?(fire/ice/lightning) ".format(fireballspell,icespell,lightningspell)).lower().strip()
                        if magicchoice == "ice" and icespell > 0:
                            icespell-=1
                            icespellused+=1
                            monsterhp-=5
                            icespellactive=1
                            print("You cast an ice spell causing 5 damage to the {0} and halving it's attack next turn, it has {1}hp remaining.".format(monstername,monsterhp))
                            time.sleep(3)
                        elif magicchoice == "lightning" and lightningspell > 0:
                            lightningspell-=1
                            lightningspellused+=1
                            monsterhp-=6
                            lightningspellactive=1
                            print("You cast a lightning spell causing 6 damage to the {0} and stunning it, it has {1}hp remaining.".format(monstername,monsterhp))
                            time.sleep(3)
                        elif magicchoice == "fire" or "fireball" and fireballspell > 0:
                            fireballspell-=1
                            fireballspellused+=1
                            monsterhp-=11
                            print("You cast a fireball spell causing 11 damage to the {0}, it has {1}hp remaining.".format(monstername,monsterhp))
                            time.sleep(3)
                        else:
                            rnumber=random.randint(1,100)
                            if 1 <= rnumber <= weaponhitchance:
                                if 1 <= rnumber <= 33 or critbattles > 0:
                                    monsterhp-=weapondamage*1.5
                                    print("Your next strike will deal critical damage.")
                                    time.sleep(3)
                                    print("Because the spell wasn't recognised or you didn't have any of the spell, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage*1.5,monstername,monsterhp))
                                    time.sleep(3)
                                else:
                                    monsterhp-=weapondamage
                                    print("Because the spell wasn't recognised or you didn't have any of the spell, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage,monstername,monsterhp))
                                    time.sleep(3)
                            else:
                                if weaponname == "bow":
                                    print("You fired your bow but missed dealing 0 damage.")
                                    time.sleep(3)
                                else:
                                    print("You swung your {0} but missed dealing 0 damage.".format(weaponname))
                                    time.sleep(3)      
                else:
                    potion=input("Would you like to use a Health Potion?(yes/no) ").lower().strip()
                    if potion == "no":
                        rnumber=random.randint(1,100)
                        if 1 <= rnumber <= weaponhitchance:
                            if 1 <= rnumber <= 33 or critbattles > 0:
                                monsterhp-=weapondamage*1.5
                                print("Your next strike will deal critical damage.")
                                time.sleep(3)
                                print("Instead of using a potion, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage*1.5,monstername,monsterhp))
                                time.sleep(3)
                            else:
                                monsterhp-=weapondamage
                                print("Instead of using a potion, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage,monstername,monsterhp))
                                time.sleep(3)
                        else:
                            if weaponname == "bow":
                                print("You fired your bow but missed dealing 0 damage.")
                                time.sleep(3)
                            else:
                                print("You swung your {0} but missed dealing 0 damage.".format(weaponname))
                                time.sleep(3)
                    elif potion == "yes" and healthpotions == 0:
                        rnumber=random.randint(1,100)
                        if 1 <= rnumber <= weaponhitchance:
                            if 1 <= rnumber <= 33 or critbattles > 0:
                                monsterhp-=weapondamage*1.5
                                print("Your next strike will deal critical damage.")
                                time.sleep(3)
                                print("Because you have no Health Potions, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage*1.5,monstername,monsterhp))
                                time.sleep(3)
                            else:
                                monsterhp-=weapondamage
                                print("Because you have no Health Potions, you attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage,monstername,monsterhp))
                                time.sleep(3)
                        else:
                            if weaponname == "bow":
                                print("You fired your bow but missed dealing 0 damage.")
                                time.sleep(3)
                            else:
                                print("You swung your {0} but missed dealing 0 damage.".format(weaponname))
                                time.sleep(3)
                    else:
                        healthpotions-=1
                        hp=maxhp
                        print("You used a Health Potion ({0} remaining) restoring you hp to full ({1}).".format(healthpotions,maxhp))
                        time.sleep(3)
            else:
                rnumber=random.randint(1,100)
                if 1 <= rnumber <= weaponhitchance:
                    if 1 <= rnumber <= 33 or critbattles > 0:
                        monsterhp-=weapondamage*1.5
                        print("Your next strike will deal critical damage.")
                        time.sleep(3)
                        print("You attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage*1.5,monstername,monsterhp))
                        time.sleep(3)
                    else:
                        monsterhp-=weapondamage
                        print("You attacked the {0} dealing {1} damage. The {2} has {3}hp remaining.".format(monstername,weapondamage,monstername,monsterhp))
                        time.sleep(3)
                else:
                    if weaponname == "bow":
                        print("You fired your bow but missed dealing 0 damage.")
                        time.sleep(3)
                    else:
                        print("You swung your {0} but missed dealing 0 damage.".format(weaponname))
                        time.sleep(3)
            if monsterhp <= 0:
                monstersslain+=1
                print("You have defeated the {0}!".format(monstername))
                time.sleep(3)
                if monstername == "wight":
                    win=True
                if critbattles > 0:
                    critbattles-=1
                    print("You feel the effects of the Critical Hit Potion wear off (you have {0} Critical Hit battles remaining).".format(critbattles))
                    time.sleep(3)
                rnumber=random.randint(1,3)
                if rnumber == 1:
                    rnumber=random.randint(1,3)
                    if 1 <= rnumber <= 2:
                        maxhp+=2
                        print("You feel healthier after defeating the {0}... Your max health is increased by 2 to {1}!".format(monstername,maxhp))
                        time.sleep(3)
                    else:
                        maxhp+=3
                        print("You feel healthier after defeating the {0}... Your max health is increased by 3 to {1}!".format(monstername,maxhp))
                        time.sleep(3)
                elif rnumber == 2:
                    rnumber=random.randint(1,3)
                    if 1 <= rnumber <= 2:
                        weapondamage+=1
                        comfy=1
                        print("You feel more comfortable with your weapon after defeating the {0}... Your weapon's damage is increased by 1 to {1}!".format(monstername,weapondamage))
                        time.sleep(3)
                    else:
                        weapondamage+=2
                        comfy=1
                        print("You feel more comfortable with your weapon after defeating the {0}... Your weapon's damage is increased by 2 to {1}!".format(monstername,weapondamage))
                        time.sleep(3)
            else:
                if monstername == "wight":
                    bossmove()
                else:
                    monstermove()
        def monstermove():
            global monstername,monsterhp,hp,icespellactive,lightningspellactive
            rnumber=random.randint(1,100)
            if 1 <= rnumber <= monsterhitchance:
                if lightningspellactive > 0:
                    lightningspellactive=0
                    print("The {0} was stunned so couldn't attack.".format(monstername))
                    time.sleep(3)
                else:
                    if icespellactive > 0:
                        icespellactive=0
                        hp-=monsterattack*0.5
                        print("The {0} was weakened by the ice spell so struck you for {1} damage, you are now on {2}hp.".format(monstername,monsterattack*0.5,hp))
                        time.sleep(3)
                    else:
                        hp-=monsterattack
                        print("The {0} struck you for {1} damage, you are now on {2}hp.".format(monstername,monsterattack,hp))
                        time.sleep(3)
            else:
                print("The {0} missed their strike dealing 0 damage".format(monstername))
                time.sleep(3)
            if hp <= 0:
                print("You have been defeated by the {0}!".format(monstername))
                time.sleep(3)
            else:
                playermove()
        def bossmove():
            global monsterattack,monstername,monsterhp,hp,icespellactive,lightningspellactive
            rnumber=random.randint(1,100)
            if 1 <= rnumber <= monsterhitchance:
                if lightningspellactive > 0:
                    lightningspellactive=0
                    print("The {0} was stunned so couldn't attack.".format(monstername))
                    time.sleep(3)
                else:
                    if icespellactive > 0:
                        icespellactive=0
                        hp-=monsterattack
                        print("The {0} was weakened by the ice spell so struck you for {1} damage, you are now on {2}hp.".format(monstername,monsterattack,hp))
                        time.sleep(3)
                    else:
                        rnumber=random.randint(1,4)
                        if rnumber == 1:
                            rnumber=random.randint(1,6)
                            if rnumber == 1:
                                hp-=monsterattack*1.5
                                monsterhp+=monsterattack
                                print("The {0} pierced you with a lifestealing longbow arrow dealing {1} (critical) damage, you are now on {2}hp. The {3} healed {4}hp and is now on {5}hp.".format(monstername,monsterattack*1.5,hp,monstername,monsterattack,monsterhp))
                                time.sleep(3)
                            else:
                                hp-=monsterattack*3
                                print("The {0} pierced you with two longbow arrows dealing {1} (critical) damage, you are now on {2}hp.".format(monstername,monsterattack*3,hp))
                                time.sleep(3)
                        else:
                            rnumber=random.randint(1,3)
                            if rnumber == 1:
                                hp-=monsterattack
                                monsterhp+=monsterattack
                                print("The {0} struck you with a lifestealing longsword blow dealing {1} damage, you are now on {2}hp. The {3} healed {4}hp and is now on {5}hp.".format(monstername,monsterattack,hp,monstername,monsterattack,monsterhp))
                                time.sleep(3)
                            else:
                                hp-=monsterattack*2
                                print("The {0} struck you twice with it's longsword dealing {1} damage, you are now on {2}hp.".format(monstername,monsterattack*2,hp))
                                time.sleep(3)
            else:
                print("The {0} missed their strike dealing 0 damage".format(monstername))
                time.sleep(3)
            if hp <= 0:
                print("You have been defeated by the {0}!".format(monstername))
                time.sleep(3)
            else:
                playermove()
        while x == 0:
            x=1
            playermove()

    def fightstart():
        global hp,monstername,monsterhp,monsterattack,monsterhitchance
        rnumber=random.randint(1,100)
        if 1 <= rnumber <= 25:
            monstername=slime().monstername
            monsterhp=slime().monsterhp
            monsterattack=slime().monsterattack
            monsterhitchance=slime().monsterhitchance
        elif 26 <= rnumber <= 50:
            monstername=bat().monstername
            monsterhp=bat().monsterhp
            monsterattack=bat().monsterattack
            monsterhitchance=bat().monsterhitchance
        elif 51 <= rnumber <= 76:
            monstername=goblin().monstername
            monsterhp=goblin().monsterhp
            monsterattack=goblin().monsterattack
            monsterhitchance=goblin().monsterhitchance
        elif 77 <= rnumber <= 90:
            monstername=wolf().monstername
            monsterhp=wolf().monsterhp
            monsterattack=wolf().monsterattack
            monsterhitchance=wolf().monsterhitchance
        elif 90 <= rnumber <= 100:
            monstername=orc().monstername
            monsterhp=orc().monsterhp
            monsterattack=orc().monsterattack
            monsterhitchance=orc().monsterhitchance
        print("A monster appears. It's a {0} with {1}hp and {2} attack (you have {3}hp)!".format(monstername,monsterhp,monsterattack,hp))
        time.sleep(3)
        flee=input("Do you want to flee and risk getting hit or fight?(flee/fight) ").lower().strip()
        if flee == "flee":
            rnumber=random.randint(1,3)
            if rnumber == 3:
                hp-=monsterattack
                print("While you were trying to flee you took {0} damage and now have {1}hp.".format(monsterattack,hp))
                time.sleep(3)
            else:
                print("You successfully fled without taking damage.")
                time.sleep(3)
        else:
            fight()

    def bossstart():
        global hp,monstername,monsterhp,monsterattack,monsterhitchance,bossnumber
        monstername=wight().monstername
        monsterhp=wight().monsterhp
        monsterattack=wight().monsterattack
        monsterhitchance=wight().monsterhitchance
        print("As you expect a monster to appear, you hear a deafening screech as a giant, undead wight draws closer. ")
        time.sleep(3)
        print("It appears to be blocking the exit of the cave and your chance to make it out. ")
        time.sleep(3)
        print("It has {0}hp with {1} attack and carries both a lightweight longsword and a longbow. It can also either attack twice or attack once using lifesteal on it's victim (you have {2}hp).".format(monsterhp,monsterattack,hp))
        time.sleep(3)
        flee=input("Do you want to flee and risk getting hit or fight?(flee/fight) ").lower().strip()
        if flee == "flee":
            rnumber=random.randint(1,3)
            if rnumber == 3:
                hp-=monsterattack
                print("While you were trying to flee the wight hit you once for {0} damage leaving you at {1}hp.".format(monsterattack,hp))
                time.sleep(3)
            else:
                print("You successfully fled without taking damage.")
                time.sleep(3)
            bossnumber=12
        else:
            fight()

    def findhealthpotion():
        global healthpotions,maxhealthpotions
        print("You see a shiny object on the floor. As you get closer it appears to be a Health Potion.")
        time.sleep(3)
        if healthpotions >= maxhealthpotions:
            print("You had to leave the Health Potion behind because you already have max.")
            time.sleep(3)
        else:
            healthpotions+=1
            print("You gained a Health Potion (you now have {0})!".format(healthpotions))
            time.sleep(3)

    def characterevent():
        global increase,hp,weaponname,weapondamage,weaponhitchance,fireballspell,lightningspell,icespell,comfy
        if character == "dwarf":
            useanvil=input("You see an avil on the floor. Should you use it?(yes/no) ").lower().strip()
            if useanvil == "no":
                pass
            else:
                rnumber=random.randint(1,16)
                if 1 <= rnumber <= 7:
                    increase=1
                    weapondamage+=1
                    print("You use the anvil and your weapon damage increased by {0} to {1}.".format(increase,weapondamage))
                    time.sleep(3)
                elif 8 <= rnumber <= 10:
                    increase=2
                    weapondamage+=2
                    print("You use the anvil and your weapon damage increased by {0} to {1}.".format(increase,weapondamage))
                    time.sleep(3)
                elif 10 <= rnumber <= 13:
                    increase=3
                    weapondamage+=3
                    print("You use the anvil and your weapon damage increased by {0} to {1}.".format(increase,weapondamage))
                    time.sleep(3)
                elif 14 <= rnumber <= 16:
                    weapondamage-=1
                    print("Oops, you hit your axe with an unproffesional blow and your damage has decreased by 1 to {0}".format(weapondamage))
                    time.sleep(3)
                    pass

        elif character == "wizard":
            openbox=input("You see a magic box on the floor. Should you open it?(yes/no) ").lower().strip()
            if openbox == "no":
                pass
            else:
                rnumber=random.randint(1,12)
                if 1 <= rnumber <= 5:
                    find="fireball spell"
                    fireballspell+=1
                    print("You opened the magic box and found a {0}. Use this on enemies to deal 11 damage.".format(find))
                    time.sleep(3)
                elif 6 <= rnumber <= 9:
                    find="ice spell"
                    icespell+=1
                    print("You opened the magic box and found a {0}. Use this on enemies to deal 5 damage and half the attack on their next strike.".format(find))
                    time.sleep(3)
                elif 10 <= rnumber <= 12:
                    find="lightning spell"
                    lightningspell+=1
                    print("You opened the magic box and found a {0}. Use this on enemies to deal 6 damage and to stop them attacking for a turn.".format(find))
                    time.sleep(3)
                elif 13 <= rnumber <= 14:
                    hp-=1
                    print("The magic box was trapped with a fire spell! You jump away from the chest as it explodes decreasing your health by 2 to {0}.".format(hp))
                    time.sleep(3)

        elif character == "human":
            openchest=input("You see a weapons chest on the floor. Should you open it?(yes/no) ").lower().strip()
            if openchest == "no":
                if comfy == 1:
                    comfy=2
                    print("You will no longer be drawn to the weapons chest.")
                    time.sleep(3)
                pass
            else:
                rnumber=random.randint(1,14)
                if 1 <= rnumber <= 6:
                    weaponname=bow().weaponname
                    weapondamage=bow().weapondamage
                    weaponhitchance=bow().weaponhitchance
                    print("You opened the chest and found a {0}.".format(weaponname))
                    time.sleep(3)
                elif 7 <= rnumber <= 10:
                    weaponname=mace().weaponname
                    weapondamage=mace().weapondamage
                    weaponhitchance=mace().weaponhitchance
                    print("You opened the chest and found a {0}.".format(weaponname))
                    time.sleep(3)
                elif 11 <= rnumber <= 12:
                    weaponname=hammer().weaponname
                    weapondamage=hammer().weapondamage
                    weaponhitchance=hammer().weaponhitchance
                    print("You opened the chest and found a {0}.".format(weaponname))
                    time.sleep(3)
                elif 13 <= rnumber <= 14:
                    hp-=2
                    print("It's trap! You jump away from the chest as it explodes decreasing your health by 2 to {0}.".format(hp))
                    time.sleep(3)

    def maxhpevent():
        global maxhp,hp
        drinkmaxhp=input("You see a shiny object on the floor. As you get closer it appears to be a Max Health Potion, do you want to drink it?(yes/no) ").lower().strip()
        if drinkmaxhp == "no":
            pass
        else:
            print("You decide to drink the Max Health Potion.")
            time.sleep(3)
            rnumber=random.randint (1,5)
            if rnumber == 1:
                hp-=1
                print("You drank the potion but it appears to have been poisoned, your health drops by 1 to {0}".format(hp))
                time.sleep(3)
            else:
                rnumber=random.randint (1,3)
                maxhp+=rnumber
                print("Your max health has been increased by {0} to {1}!".format(rnumber,maxhp))
                time.sleep(3)

    def critevent():
        global critbattles,hp
        drinkcrit=input("You see a shiny object on the floor. As you get closer it appears to be a Critical Hit Potion, do you want to drink it?(yes/no) ").lower().strip()
        if drinkcrit == "no":
            pass
        else:
            if critbattles < 5:
                print("You decide to drink the Critical Hit Potion.")
                time.sleep(3)
                rnumber=random.randint(1,5)
                if rnumber == 1:
                    hp-=1
                    print("You drank the potion but it appears to have been poisoned, your health drops by 1 to {0}".format(hp))
                    time.sleep(3)
                else:
                    critbattles+=1
                    print("Every strike in your next {0} battle(s) will be a critical hit!".format(critbattles))
                    time.sleep(3)
            else:
                print("You already have 5 Critical Hit battles remaining so you had to leave it behind.")
                time.sleep(3)

    def moving():
        global comfy
        rnumber=random.randint(1,100)
        if 1  <= rnumber <= 50:
            fightstart()
        if 51 <= rnumber <= 70:
            if healthpotions < maxhealthpotions:
                findhealthpotion()
            else:
                maxhpevent()
        if 71 <= rnumber <= 80:
            if comfy == 2:
                critevent()
            else:
                characterevent()
        if 81 <= rnumber <= 90:
            maxhpevent()
        if 91 <= rnumber <= 100:
            critevent()

    def movingcharacter():
        global comfy
        rnumber=random.randint(1,12)
        if 1  <= rnumber <= 2:
            fightstart()
        if rnumber == 3:
            if healthpotions < maxhealthpotions:
                findhealthpotion()
            else:
                maxhpevent()
        if 4 <= rnumber <= 10:
            if comfy == 2:
                critevent()
            else:
                characterevent()
        if rnumber == 11:
            maxhpevent()
        if rnumber == 12:
            critevent()

    def movinglife():
        global comfy
        rnumber=random.randint(1,17)
        if 1  <= rnumber <= 2:
            fightstart()
        if 3 <= rnumber <= 9:
            if healthpotions < maxhealthpotions:
                findhealthpotion()
            else:
                maxhpevent()
        if rnumber == 10:
            if comfy == 2:
                critevent()
            else:
                characterevent()
        if 11 <= rnumber <= 16:
            maxhpevent()
        if rnumber == 17:
            critevent()  

    while notfinished:
        if win == True:
            print("You have conquered the cave of monsters and will now move on to a better life in the beautiful village beyond the wall of evil...\n")
            time.sleep(5)
            print("Your final stats:\n\
hp={0},\n\
Maximum hp={1},\n\
Critical Battles remaining={2},\n\
Health Potions={3},\n\
Monsters slain={4},\n\
Your weapon={5},\n\
Weapon Damage={6}.\n\
Fireball spells={7},\n\
Fireball spells used={8},\n\
Ice spells={9},\n\
Ice spells used={10},\n\
Lightning spells={11},\n\
Lightning spells used={12}\n".format(hp,maxhp,critbattles,healthpotions,monstersslain,weaponname,weapondamage,fireballspell,fireballspellused,icespell,icespellused,lightningspell,lightningspellused))
            time.sleep(5)
            print("Congratulations.")
            time.sleep(3)
            notfinished=False
        if notfinished=False:
            break

        if hp > 0:
            bossnumber+=1
            x1=""
            x2=""
            y1=""
            y2=""
            z1=""
            z2=""
            rnumber=random.randint(1,8)
            if rnumber == 1 or rnumber == 2:
                if comfy == 2:
                    x1="There seems to be a calling to your weapon deriving from the "
                elif critbattles < 5:
                    x1="There seems to be a calling to your character deriving from the "
                else:
                    pass
                rnumber=random.randint(1,3)
                if rnumber == 1 and critbattles < 5:
                    x2="right. "
                elif rnumber == 2 and critbattles < 5:
                    x2="left. "
                elif rnumber == 3 and critbattles < 5:
                    x2="middle. "
                else:
                    pass
            elif rnumber == 3 or rnumber == 4:
                y1="There seems to be an aroma of health emerging from the "
                rnumber=random.randint(1,3)
                if rnumber == 1:
                    y2="right. "
                elif rnumber == 2:
                    y2="left. "
                else:
                    y2="middle. "
            elif rnumber == 5:
                z1="You hear the sound of a monster originating from the "
                rnumber=random.randint(1,3)
                if rnumber == 1:
                    z2="right. "
                elif rnumber == 2:
                    z2="left. "
                else:
                    z2="middle. "

            move=input("{0}{1}{2}{3}{4}{5}You see 3 paths in front of you, which way would you like to travel?(left/right/middle) ".format(x1,x2,y1,y2,z1,z2)).lower().strip()

            if move in x2 and x2 != "":
                movingcharacter()
            elif move in y2 and y2 != "":
                movinglife()
            elif move in z2 and z2 != "":
                fightstart()
            else:
                moving()
        else:
            print("Your health dropped to 0, game over.")
            time.sleep(3)
            notfinished=False
        if bossnumber >= 20 and monstersslain >= 7:
            bossstart()

    restart=input("Would you like to play again?(yes/no) ").lower().strip()
    if restart == "no":
        break