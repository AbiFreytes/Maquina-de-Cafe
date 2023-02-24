import unittest

from numpy import insert
from main import (Maquina, NoChocolate, NoCoinException, NoCoffee, NoSugar, NoMilk)


class TestMaquina(unittest.TestCase):
    def test_coinsTrue(self):
        machine = Maquina()
        machine.insert_coins()
        self.assertEqual(machine.coins, 1)

    def test_coinsFalse(self):
        machine = Maquina()
        machine.no_coins()
        self.assertEqual(machine.coins, 0)
    
    def test_choose_options(self):
        machine = Maquina()
        product = machine.choose_option(1)
        self.assertEqual(product, 'Cafe solo')

    def test_errorCoins(self):
        machine = Maquina()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        with self.assertRaises(NoCoinException):
            machine.make_coffee()

    def test_error_no_sugar(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_sugar(0)
        with self.assertRaises(NoSugar):
            machine.make_coffee()

    def test_errorCafe(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_sugar(1000)
        machine.insert_coffee(0)
        machine.choose_option(1)
        with self.assertRaises(NoCoffee):
            machine.make_coffee()

    def test_errorMilk(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_sugar(1000)
        machine.insert_milk(0)
        machine.insert_chocolate(1000)
        machine.choose_option(7)
        with self.assertRaises(NoMilk):
            machine.make_coffee()
    
    def test_errorChocolate(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_sugar(1000)
        machine.insert_milk(1000)
        machine.choose_option(7)
        machine.insert_chocolate(0)
        with self.assertRaises(NoChocolate):
            machine.make_coffee()
    
    def test_get_coffee_ok(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        machine.choose_option(1)
        coffee_result = machine.make_coffee()
        self.assertEqual(coffee_result, 'Cafe solo con azucar')
        self.assertEqual(machine.coffee, 1000-15)
        self.assertEqual(machine.sugar, 1000-5)
        self.assertEqual(machine.coins, 1)

    def test_get_coffee_doble(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        machine.choose_option(2)
        coffee_result = machine.make_coffee()
        self.assertEqual(coffee_result, 'Cafe doble')
        self.assertEqual(machine.coffee, 1000-30)
        self.assertEqual(machine.sugar, 1000-5)
        self.assertEqual(machine.coins, 0)
    
    
    def test_get_coffee_with_milk_ok(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        machine.insert_milk(1000)
        machine.choose_option(3)
        coffee_result = machine.make_coffee()
        self.assertEqual(coffee_result, 'Cafe con leche con azucar')
        self.assertEqual(machine.coffee, 1000-15)
        self.assertEqual(machine.sugar, 1000-5)
        self.assertEqual(machine.milk, 1000-15)
        self.assertEqual(machine.coins, 1)

    def test_get_capuccino_ok(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        machine.insert_milk(1000)
        machine.insert_chocolate(1000)
        machine.choose_option(4)
        coffee_result = machine.make_coffee()
        self.assertEqual(coffee_result, 'Capuccino')
        self.assertEqual(machine.coffee, 1000-10)
        self.assertEqual(machine.sugar, 1000-5)
        self.assertEqual(machine.milk, 1000-10)
        self.assertEqual(machine.chocolate, 1000-10)
        self.assertEqual(machine.coins, 1)
    
    def test_get_cortado_ok(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        machine.insert_milk(1000)
        machine.insert_chocolate(1000)
        machine.choose_option(5)
        coffee_result = machine.make_coffee()
        self.assertEqual(coffee_result, 'Cortado')
        self.assertEqual(machine.coffee, 1000-15)
        self.assertEqual(machine.sugar, 1000-5)
        self.assertEqual(machine.milk, 1000-5)
        self.assertEqual(machine.coins, 1)

    def test_get_lagrima_ok(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        machine.insert_milk(1000)
        machine.insert_chocolate(1000)
        machine.choose_option(6)
        coffee_result = machine.make_coffee()
        self.assertEqual(coffee_result, 'Lagrima')
        self.assertEqual(machine.coffee, 1000-10)
        self.assertEqual(machine.sugar, 1000-5)
        self.assertEqual(machine.milk, 1000-20)
        self.assertEqual(machine.coins, 1)
    
    def test_get_chocolate_ok(self):
        machine = Maquina()
        machine.insert_coins()
        machine.insert_coins()
        machine.insert_coffee(1000)
        machine.insert_sugar(1000)
        machine.insert_milk(1000)
        machine.insert_chocolate(1000)
        machine.choose_option(7)
        coffee_result = machine.make_coffee()
        self.assertEqual(coffee_result, 'Chocolate')
        self.assertEqual(machine.sugar, 1000-5)
        self.assertEqual(machine.milk, 1000-15)
        self.assertEqual(machine.chocolate, 1000-15)
        self.assertEqual(machine.coins, 1)


if __name__ == '__main__':
    unittest.main()