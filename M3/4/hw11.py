class Good:
    def __init__(self,name,price,quantity = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculation(self):
        total = self.price * self.quantity
        return total

    def __str__(self):
        return f'{self.name:20}  {self.price:7.2f} * {self.quantity:3} =  {self.calculation():3.2f}'


class DiscountGood(Good):
    def __init__(self,name,price,quantity,discount):
        super().__init__(name,price,quantity)
        self.discount = discount

    def calculation(self):
        return super().calculation() * (1 - self.discount / 100)

    def __str__(self):
        return super().__str__() + f' ({-self.discount}%)'


class Cart:
    def __init__(self):
        self.goods = []


    def __str__(self):
        check = f'{"Name":20}  {"PPU":7} * {"CNT":3} =  {"Price":3}  Discount '
        check += '\n================================================================='
        for product in self.goods:
            check += f'\n{product}'
        check += '\n================================================================='
        check += f'\n{"Total":20}                 = {self.total():3.2f}'
        return check

    def fill_up(self,product):
        self.goods.append(product)

    def total(self):
        array = []
        for good in self.goods:
            array.append(good.calculation())
        return sum(array)


cart_1 = Cart()
good_1 = Good('Bread',17,3)
good_2 = Good('Water',19,2)
good_3 = DiscountGood('Juice',80,1,20)
good_4 = Good('Toilet Paper',19,10)
cart_1.fill_up(good_1)
cart_1.fill_up(good_2)
cart_1.fill_up(good_3)
cart_1.fill_up(good_4)
print(cart_1)




