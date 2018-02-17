price = 100
vat_rate = 18
vat = price / 100 * vat_rate
print(vat)
price_no_vat = price - vat
print(price_no_vat)


def get_vat(price, vat_rate):
    if not isinstance(price, int):
    	print(isinstance(price,int) == (type(price) == "Int"))
    	return "Bad type"
    if not isinstance(vat_rate,int):
        return "Bad type"
    if price < 0:
    	return "Should be positive"
    if vat_rate <= 0:
    	return "Should be positive"
    vat = price / 100 * vat_rate
    price_no_vat = price - vat
    print(price_no_vat)

price1 = 100
vat_rate1 = 18
get_vat(price1, vat_rate1)

price1 = 100
vat_rate2 = 18
get_vat(price1, vat_rate2)

price2 = 500
vat_rate1 = 10
get_vat(price2, vat_rate1)

get_vat(50, '5')
get_vat(-100, 18)

print(get_vat(-150,5))
print(get_vat(-150.4,5))





def get_summ(one, two, delimeter=' '):
    return str(str(one) + str(delimeter) + str(two)).upper()

print(get_summ('Hello', "There", ","))
