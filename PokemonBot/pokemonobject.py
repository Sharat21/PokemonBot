class Pokemon:
    name: str
    health: int
    attack: int
    special: int
    have_special: bool
    special_counter: int

    def __init__(self, pokemon, health, attack, defense, special):
        self.name = pokemon
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special = special
        self.have_special = False
        self.special_counter = 2

    def take_damage(self, damage_taken) -> None:
        '''
        Update health of pokemon after taking damage
        '''
        self.health -= damage_taken
        int(self.health)

    def deal_damage(self, damageType) -> int:
        '''
        Return amount of damage a pokemon will deal
        '''
        from random import randint

        if damageType == "special":
            return self.special_attack()
        return randint(self.attack -5, self.attack + 5) / 5

    def special_attack(self) -> int:
        '''
        Designate attack as a special attack, dealing bonus damage
        '''
        print(self.name)
        from random import randint
        if not self.have_special:
            return False

        self.special_counter = randint(1,3)
        self.have_special = False
        return randint(self.special -5 + self.attack, self.special + 5 + self.attack) / 5

    def is_dead(self) -> bool:
        '''
        check if pokemon has fainted
        '''
        return self.health <= 0

    async def special_cooldown(self, ctx) -> int:
        '''
        Update cooldown of special attack
        '''
        if not self.have_special:
            self.special_counter -= 1

        if self.special_counter == 0:
            self.have_special = True
            await ctx.send(self.name + " has charged their special attack")