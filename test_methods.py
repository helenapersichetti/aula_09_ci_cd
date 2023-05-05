import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    valor1 = 6
    valor2 = 8

    output = methods.soma_valores(valor1, valor2)

    assert output == 10

def test_multiplicacao():
    valor1 = 4
    valor2 = 5

    output = methods.multiplicacao_valores(valor1, valor2)

    assert output == 15

def test_divisao():
    valor1 = 10
    valor2 = 5

    output = methods.divisao_valores(valor1, valor2)

    assert output == 2

def test_subtracao():
    valor1 = 10
    valor2 = 5

    output = methods.subtracao_valores(valor1, valor2)

    assert output == 2