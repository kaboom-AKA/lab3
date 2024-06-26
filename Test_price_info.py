import price_info as pi

price_list={'bannana':1.00, 'watermelon': 6.50, 'pineapple': 2.70, 'papaya': 2.90, 'grapes': 4.90 }

quantity_list= {'bannana':5, 'watermelon': 2, 'pineapple': 9, 'papaya': 1, 'grapes': 2}


def test_total_cost_shopping():
    result= 55
    assert(result==pi.total_cost_shopping(price_list,quantity_list))

def test_cost_of_fruit() :

    input_fruit='watermelon'
    input_quantity=10
    result= 65
    assert(result==pi.cost_of_fruits(input_fruit,input_quantity))
