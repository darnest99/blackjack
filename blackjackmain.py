'''
-me.tot equals zero and it fucks the whole thing up idk why good luck
    -FIXED
-Dealer doesnt bust
    -FIXED
-clean up. play() has lots of repeating stuff thats also in hit()
    -FIXED
-bust even when 11
    -FIXED
-doesnt end game when asked
'''


from carddeck import Deck

won = False

class Player:
    def __init__(self, balance=100, bust = False, pot = 0, stand=False, tot=0, broke=False):
        self.hand = []
        self.balance = balance
        self.bust = bust
        self.pot = pot
        self.stand = stand
        self.tot = tot
        self.broke = broke

    def __str__(self):
        return f"You have a hand of {self.hand} and ${self.balance}."

    def begin(self):
        self.hand += [game.deal(), game.deal()]

    def bet(self, cash):
        self.balance = self.balance - cash
        if self.balance < 0:
            print("You're broke!")
            self.broke = True
            return self.broke

        self.pot += cash*2

        print('Deposited')

    def hit(self):
        card = game.deal()
        self.hand += [card]
        print(self.hand)
        nums = [k[0] for k in self.hand]
        self.tot = sum(nums)
        if self.tot <= 21:
            print(self.tot)
            return self.hand
        elif 31 >= self.tot > 21:
            if 11 in nums:
                self.tot = self.tot - 10
                self.hand[nums.index(11)][0] -= 10
                print(self.tot)
                return self.hand

    def play(self):
        option = input('Would you like to hit or stand?')
        if option == 'hit':
            me.hit()
            nums = [k[0] for k in self.hand]
            self.tot = sum(nums)
            return self.tot
        elif option == 'stand':
            self.stand = True
            nums = [k[0] for k in self.hand]
            self.tot = sum(nums)
            return self.tot


class Dealer:
    def __init__(self, bust=False, stand=False, tot=0):
        self.hand = []
        self.bust = bust
        self.stand = stand
        self.tot = tot
    def begin(self):
        self.hand += [game.deal(), game.deal()]
    def house(self):
        nums = [k[0] for k in self.hand]
        self.tot = sum(nums)
        if self.tot < 16:
            card = game.deal()
            self.hand += [card]
            self.stand = False
            if self.tot <= 21:
                return self.hand
            elif 31 >= self.tot > 21:
                if 11 in nums:
                    self.tot = self.tot - 10
                    self.hand[nums.index(11)][0] -= 10
                    print(self.tot)
                    return self.hand

        else:
            self.stand = True
            return self.stand


##################################################################################################################

while __name__ == '__main__':
    game = Deck()
    game.build()
    me = Player()
    you = Dealer()
    while True:
        keepgo = input('Would you like to begin?')
        if keepgo == 'yes' or 'y':
            you.begin()
            me.begin()
            print(me)
            while won == False:
                try:
                    cash = int(input('Enter a bet or forfeit'))
                    me.bet(cash)
                    if me.broke == True:
                        print(f'You lost ${me.pot / 2}')
                        won = True
                    print(f'You have ${me.balance}')
                except:
                    break
                me.play()
                you.house()

                numsme = [k[0] for k in me.hand]
                totme = sum(numsme)
                numsyou = [k[0] for k in you.hand]
                totyou = sum(numsyou)
                if totme > 21:
                    print('bust')
                    me.balance -= (me.pot/2)
                    print(f'You lost ${me.pot / 2}')
                    me.pot = 0
                    won = True
                elif totyou > 21:
                    print('Dealer busts')
                    print(f"Dealer's hand: {you.hand}")
                    me.balance += me.pot
                    print(f'You Won ${me.pot}!')
                    me.pot = 0
                    won = True

                elif me.stand == True and you.stand == True:
                    if me.tot > you.tot:
                        me.balance += me.pot
                        print(f'You Won ${me.pot}!')
                        print(f"Dealer's hand: {you.hand}")
                        me.pot = 0
                        won = True
                    elif me.tot < you.tot:
                        me.balance -= (me.pot/2)
                        print(f'You lost ${me.pot / 2}')
                        print(f"Dealer's hand: {you.hand}")
                        print(me.tot)
                        me.pot = 0
                        won = True
                    else:
                        print('TIE')
                        print(f"Dealer's hand: {you.hand}")
                        won = True
            me.hand = []
            you.hand = []
            won = False
        else:
            break
    else:
        break
