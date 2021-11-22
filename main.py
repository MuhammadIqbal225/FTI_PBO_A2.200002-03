class Hero:

    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):

        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat Hero dengan nama " + inputName)

hero1 = Hero("yesi",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mila",100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("tila",1000, 100, 0)
print(Hero.jumlah)