from behave import given, when, then

from calculator import Calculator

@given('se usa la calculadora para {operation}')
def calculator_test_for(context,operation):
    context.operation = operation

@when('se introducen los numeros {number1:d} y {number2:d}')
def operation_test(context, number1, number2):
    #context.number1 = number1
    #context.number2 = number2
    context.calculator = Calculator(number1,number2)

@then('se muestra el resultado de {number3:d}')
def operation_result(context, number3):
	if context.operation == 'sumar':
	    assert(context.calculator.add() == number3)
	elif context.operation == 'restar':
	    assert(context.calculator.subtract() == number3)
	elif context.operation == 'multiplicar':
	    assert(context.calculator.multiply() == number3)
	elif context.operation == 'dividir':
	    assert(context.calculator.divide() == number3)

