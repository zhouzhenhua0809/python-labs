
class Rocket:
    
    def __init__(self, mass, fuel, bool):
        self.mass = mass
        self.fuel = fuel
        self.bool = bool
        self.mass = mass + fuel 
    #Расход топлива и определение если оно осталось после расхода
    def spend_fuel(self, count): 
        
        if (self.fuel - count) >= 0:    
            self.mass = self.mass - count
            self.fuel = self.fuel - count
            return True
        #Если топливо недостаточно, вернётся  false
        else:
            if self.fuel < count:
                self.fuel = 0 
            self.bool = False
            self.mass = self.mass - self.fuel
            return False
       
  #Количество топлива в двигателе
            
    def get_fuel_level(self):
        return self.fuel
        
        
 #Определение общую массу Двигателя
 
    def get_total_weight(self):
        return self.mass
    
#Работает ли двигатель
    
    def get_is_engine_running(self):
        return self.bool
        
        
        

test_ = Rocket(700, 400, True)

while test_.bool == True:
    test_.spend_fuel(30)
    print(test_.get_total_weight(), test_.get_fuel_level(), test_.bool)