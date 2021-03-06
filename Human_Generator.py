import random
import pickle

class Human:
    
    
    def __init__(self, name, real_hp, real_stamina, real_sex, real_physique, real_iq, real_money, real_age):
        self.name = name
        self.real_hp = 10
        self.real_stamina = 10
        self.real_sex = random.randint(1,2)
        self.real_physique = random.randint(30,200)
        self.real_iq = random.randint(30,200)
        self.real_money = random.randint(1,100000)
        self.real_age= random.randint(13,100)
  
    #def statcheck(self):
        #return ('{} {} {} {} {} {} {} {}'.format(self.name, self.real_hp, self.real_stamina, self.real_sex, self.real_physique, self.real_iq, self.real_money, self.real_age)) 
    
    def random_stats(self):
        self.real_age=random.randint(13,100)
        self.real_sex = random.randint(1,2)
        self.real_physique = random.randint(1,180)
        self.real_iq = random.randint(1,180)
        self.real_money = random.randint(1,70000)
    
    def stats_to_text_hp(self):
        if  self.real_hp == 10:
                self.stat_hp = 'Healthy'
        elif self.real_hp > int(4):
                self.stat_hp = 'Average Health'
        else:
                self.stat_hp = 'Haggard'
        return self.stat_hp

    def stats_to_text_stamina(self):
        if self.real_stamina == 10:
                self.stat_stamina = "Vigorous"
        elif self.real_stamina > 4:
                self.stat_stamina = 'Average Energy'
        else:
                self.stat_stamina = 'Feeling Exhausted' 
        
    def stat_to_gender(self):
        if self.real_sex == 1:
            self.stat_sex = 'Male'
        else:
            self.stat_sex = 'Female'
            
    def stat_how_buff(self):
        if self.real_physique > 140:
            self.stat_physique = 'Greek God'
        if self.real_physique  > 80:
            self.stat_physique = 'Human'
        else:
            self.stat_physique = 'Stick Person'
    
    def stat_how_smart(self):
        if self.real_iq > 140:
            self.stat_iq = 'Brainiac'
        if self.real_iq > 80:
            self.stat_iq = 'Average IQ'
        else:
            self.stat_iq = 'Smooth Brain'

            
    def stat_how_rich(self):
        if self.real_money > 100000:
            self.stat_money = 'Richer than rich'
        if self.real_money > 35000:
            self.stat_money = 'Middle Income'
        else:
            self.stat_money = 'Basically Homeless'
        
    def statcheck_convert(self):
        self.stats_to_text_hp()
        self.stats_to_text_stamina()
        self.stat_to_gender()
        self.stat_how_buff()
        self.stat_how_smart()
        self.stat_how_rich()
        return ('-----------------------\nMy name is [{}]\n    [{}]\n    [{}]\n    [{}]\n    [{}]\n    [{}]\n    [{}]\n    [{} years old]\n-----------------------'.format(self.name, self.stat_hp, self.stat_stamina, self.stat_sex, self.stat_physique, self.stat_iq, self.stat_money, self.real_age))        
    
    def satisfaction_yes_no(self):
        yes = 1
        no = 2
        end = 0
        while True:
            self.question1 = input('Are you satisfied with your result?\nYes 1 | No 2 | End 0 |  ')
            question = int(self.question1)
            if question == 1 and question:
                with open('savefile.dat', 'wb') as f:
                    pickle.dump([self], f, protocol = 2)
                return '\nCreation Success'
                break
            elif question == 2:
                print(self.statcheck_convert())
                self.random_stats()
                print('Your stats will now randomly change')
            elif question == 0:
                return ("Come again")
            else:
                print('invalid input. Enter the proper commands') 

            

name= (input('What is your name?\n'))
player=Human(name, {}, {}, {}, {}, {}, {}, {})
print(player.statcheck_convert())
print(Human.satisfaction_yes_no(player))
