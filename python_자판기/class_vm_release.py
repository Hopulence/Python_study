import sys

# 가격은 100원 단위
PRICE_UNIT = 100

class texts:
    title   = "### %s 자판기 입니다. ###"
    product = "%s:%s(%s원)"
    insert_coin =   "동전을 넣어 주세요. : "
    n_enough_coin = "동전이 부족합니다. \n거스름돈을 %원 입니다."
    select_product = "원하시는 상품번호를 선택해주세요."
    select_falut = "잘 못 누르셨습니다."
    product_out = "선택하신 %s 입니다. 거스름돈은 %s원 입니다. \n감사합니다."

class Product:
    productType = []
    productValue = []

class CoffeeVM(Product):
    _product_info_file = "coffee.txt"
    _name = "커피"

    def __init__(self):
        print( texts.title %self._name)

    def set_products(self):
        #초기화
        Product.productType = []
        Product.productValue = []

        with open(self._product_info_file, "r", encoding="UTF-8") as fd:
            for line in fd:
                list = line.strip('\n').split(',')
                Product.productType.append((list[0] + ',' + list[1]))
                Product.productValue.append((list[0] + ',' + list[2]))

    def run(self):
        self.set_products()

        while True:
            try:
                inputCoin = float(input(texts.insert_coin))
            except ValueError:
                print(texts.select_falut)
            else:
                self.selectProduct(inputCoin)

    def selectProduct(self, coin):

        description = ''
        for line in Product.productType:
            list = line.split(',')

            price = self.getProductValue(list[0])
            description += list[0] + ':' + list[1] + '(' + str(price) + ')원 '

        print(description)
        inputProduct = input( texts.select_product )
        productValue = self.getProductValue(inputProduct)

        if productValue:
            productName = self.getProductName(inputProduct)
            self.payment(coin, productName, productValue)
        
        else:
            print(texts.select_falut)
            self.selectProduct(coin)

    def getProductValue(self, product):
        returnValue = 0
        for line in Product.productValue:
            list = line.split(',')
            if list[0] == product:
                returnValue = list[1]

        return int(returnValue)

    def getProductName(self, product):
        for line in Product.productType:
            list = line.split(',')
        if list[0] == product:
            return list[1]

    def payment(self, coin, name, value):
        coinValue = coin * PRICE_UNIT
        if coinValue >= value:
            balance = coinValue - value
            print( texts.product_out %(name, int(balance)))
        else:
            print(texts.n_enough_coin %int(coinValue))
        
        self.run()
            
class SnackVM(CoffeeVM):
    _product_info_file = "snack.txt"
    _name = "과자"

if __name__ == '__main__':

    print("1: Coffee\n2: Snack")
    select_vm = input("구동할 자판기를 선택해주세요.").strip()

    if select_vm == "1":
        vm = CoffeeVM()

    elif select_vm == "2":
        vm = SnackVM()

    else:
        print(texts.select_falut)
        sys.exit(-1)

    try:
        vm.run()

    except KeyboardInterrupt as exc:
        print("판매를 종료합니다.")        