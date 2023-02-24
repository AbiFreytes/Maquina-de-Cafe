
class NoCoinException(Exception):
    pass
class NoMilk(Exception):
    pass
class NoCoffee(Exception):
    pass
class NoChocolate(Exception):
    pass
class NoSugar(Exception):
    pass


class Maquina:
    def __init__(self):
        self.coins = 0
        self.coffee = 0
        self.sugar = 0
        self.milk = 0
        self.chocolate = 0
        self.options = {1: 'Cafe solo', 
        2: 'Cafe doble', 
        3: 'Cafe con leche', 
        4: 'Capuccino', 
        5: 'Cortado', 
        6: 'Lagrima', 
        7: 'Chocolate'}
        self.final_option = 0

    def choose_option(self, option):
        self.final_option = self.options[option]
        return self.final_option

    def insert_coins(self):
        self.coins += 1
    
    def no_coins(self):
        self.coins == 0
    
    def hay_coins(self):
        if self.coins >= 1:
            return True
    
    def hay_azucar(self):
        if self.sugar >= 15:
            return True

    def hay_cafe(self):
        if self.coffee >= 30:
            return True
    
    def hay_leche(self):
        if self.milk >= 30:
            return True

    def hay_chocolate(self):
        if self.chocolate >= 15:
            return True

    def insert_coffee(self, coffee):
        self.coffee += coffee

    def insert_sugar(self, sugar):
        self.sugar += sugar

    def insert_milk(self, milk):
        self.milk += milk
    
    def insert_chocolate(self, chocolate):
        self.chocolate += chocolate

    def count_coffee_left(self):
        count_coffee_because_coffee = self.coffee // 30
        count_coffee_because_sugar = self.sugar // 5
        count_coffee_because_milk = self.milk // 30
        count_coffee_because_chocolate = self.chocolate // 15
        return min(count_coffee_because_coffee, 
        count_coffee_because_sugar, 
        count_coffee_because_milk, 
        count_coffee_because_chocolate)
    
    def make_coffee(self):
        if not self.hay_coins():
            raise NoCoinException('No se han ingresado monedas')
        if not self.hay_azucar():
            raise NoSugar

        if self.final_option == 'Cafe solo':
            if not self.hay_cafe():
                raise NoCoffee('No hay suficiente cafe')
            if self.hay_coins() and self.hay_cafe() and self.hay_azucar():
                self.coins -= 1
                self.coffee -= 15
                self.sugar -= 5
                return self.final_option + ' con azucar'

        if self.final_option == 'Cafe doble':
            if not self.hay_cafe():
                raise NoCoffee('No hay suficiente cafe')
            if self.hay_coins() and self.hay_cafe() and self.hay_azucar():
                self.coins -= 2
                self.coffee -= 30
                self.sugar -= 5
                return self.final_option

        if self.final_option == 'Cafe con leche':
            if not self.hay_cafe():
                raise NoCoffee('No hay suficiente cafe')
            if not self.hay_leche():
                raise NoMilk('No hay leche disponible')
            if self.hay_coins() and self.hay_cafe() and self.hay_azucar() and self.hay_leche():
                self.coins -= 1
                self.coffee -= 15
                self.sugar -= 5
                self.milk -= 15
                return self.final_option + ' con azucar'

        if self.final_option == 'Capuccino':
            if not self.hay_cafe():
                raise NoCoffee('No hay suficiente cafe')
            if not self.hay_leche():
                raise NoMilk('No hay leche disponible')
            if not self.hay_chocolate():
                raise NoChocolate('No hay suficiente chocolate')
            if self.hay_coins() and self.hay_cafe() and self.hay_azucar() and self.hay_leche() and self.hay_chocolate():
                self.coins -= 1
                self.coffee -= 10
                self.sugar -= 5
                self.milk -= 10
                self.chocolate -= 10
                return self.final_option
        
        if self.final_option == 'Cortado':
            if not self.hay_cafe():
                raise NoCoffee('No hay suficiente cafe')
            if not self.hay_leche():
                raise NoMilk('No hay leche disponible')
            if self.hay_coins() and self.hay_cafe() and self.hay_azucar() and self.hay_leche():
                self.coins -= 1
                self.coffee -= 15
                self.sugar -= 5
                self.milk -= 5
                return self.final_option
                
        if self.final_option == 'Lagrima':
            if not self.hay_cafe():
                raise NoCoffee('No hay suficiente cafe')
            if not self.hay_leche():
                raise NoMilk('No hay leche disponible')
            if self.hay_coins() and self.hay_cafe() and self.hay_azucar() and self.hay_leche():
                self.coins -= 1
                self.coffee -= 10
                self.sugar -= 5
                self.milk -= 20
                return self.final_option

        if self.final_option == 'Chocolate':
            if not self.hay_chocolate():
                raise NoChocolate('No hay suficiente chocolate')
            if not self.hay_leche():
                raise NoMilk('No hay leche disponible')
            if self.hay_coins() and self.hay_azucar() and self.hay_leche() and self.hay_chocolate():
                self.coins -= 1
                self.sugar -= 5
                self.milk -= 15
                self.chocolate -= 15
                return self.final_option

    