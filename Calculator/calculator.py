import tkinter as tk

counter = 0
firstNumber = 0
secondNumber = 0
operand = 0
calcCounter = 0

def inputNumber(params):
    global counter
    inputAngka.config(state='normal')
    if(counter == 0):
        inputAngka.delete(0, 'end')
        inputAngka.insert(counter, params)
        counter += 1
    else:
        inputAngka.insert(counter, params)
        counter += 1
    inputAngka.config(state='readonly')

def resetCalculator():
    global counter, firstNumber, secondNumber
    counter = 0
    firstNumber = 0
    secondNumber = 0
    inputAngka.config(state='normal')
    inputAngka.delete(0, 'end')
    inputAngka.insert(0, '0')
    inputAngka.config(state='readonly')

def startOperation():
    global counter, firstNumber, secondNumber, calcCounter, operand
    if(operand == 1):
        firstNumber = firstNumber * secondNumber
    elif(operand == 2):
        firstNumber = firstNumber / secondNumber
    elif(operand == 3):
        firstNumber = firstNumber + secondNumber
    else:
        firstNumber = firstNumber - secondNumber
    
    inputAngka.config(state='normal')
    inputAngka.delete(0, 'end')
    inputAngka.insert(0, str(firstNumber))
    inputAngka.config(state='readonly')
    
    secondNumber = 0

def operationReset():
    global counter, firstNumber, secondNumber, calcCounter, operand
    firstNumber = 0
    secondNumber = 0
    operand = 0
    calcCounter = 0
    counter = 0
    
    inputAngka.config(state='normal')
    inputAngka.delete(0, 'end')
    inputAngka.insert(0, str(firstNumber))
    inputAngka.config(state='readonly')

def operationGeneric():
    global counter, firstNumber, secondNumber, calcCounter, operand
    secondNumber = float(inputAngka.get())
    startOperation()
    operand = 0
    calcCounter = 0
    counter = 0
    

def operationMultiplication():
    global counter, firstNumber, secondNumber, calcCounter, operand
    if(calcCounter == 0):
        firstNumber = float(inputAngka.get())
        operand = 1
        calcCounter += 1
    else:
        secondNumber = float(inputAngka.get())
        startOperation()
        operand = 1
    counter = 0

def operationDivision():
    global counter, firstNumber, secondNumber, calcCounter, operand
    if(calcCounter == 0):
        firstNumber = float(inputAngka.get())
        operand = 2
        calcCounter += 1
    else:
        secondNumber = float(inputAngka.get())
        startOperation()
        operand = 2
    counter = 0

def operationAddition():
    global counter, firstNumber, secondNumber, calcCounter, operand
    if(calcCounter == 0):
        firstNumber = float(inputAngka.get())
        operand = 3
        calcCounter += 1
    else:
        secondNumber = float(inputAngka.get())
        startOperation()
        operand = 3
    counter = 0

def operationSubtraction():
    global counter, firstNumber, secondNumber, calcCounter, operand
    if(calcCounter == 0):
        firstNumber = float(inputAngka.get())
        operand = 4
        calcCounter += 1
    else:
        secondNumber = float(inputAngka.get())
        startOperation()
        operand = 4
    counter = 0
    

master = tk.Tk()
master.title("Simple Calc")
#change the geometry here
master.geometry("193x150")

inputAngka = tk.Entry(master, justify="right")

inputAngka.grid(row=0, column=0, columnspan=4, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='7', command= lambda: inputNumber('7')).grid(row=1, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='8', command= lambda: inputNumber('8')).grid(row=1, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='9', command= lambda: inputNumber('9')).grid(row=1, column=2, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='x', command= operationMultiplication).grid(row=1, column=3, sticky=tk.N+tk.E+tk.S+tk.W)

tk.Button(master, text='4', command= lambda: inputNumber('4')).grid(row=2, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='5', command= lambda: inputNumber('5')).grid(row=2, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='6', command= lambda: inputNumber('6')).grid(row=2, column=2, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text=':', command= operationDivision).grid(row=2, column=3, sticky=tk.N+tk.E+tk.S+tk.W)

tk.Button(master, text='1', command= lambda: inputNumber('1')).grid(row=3, column=0, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='2', command= lambda: inputNumber('2')).grid(row=3, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='3', command= lambda: inputNumber('3')).grid(row=3, column=2, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='+', command= operationAddition).grid(row=3, column=3, sticky=tk.N+tk.E+tk.S+tk.W)

tk.Button(master, text='0', command= lambda: inputNumber('0')).grid(row=4, column=0, columnspan=2, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='=', command= operationGeneric).grid(row=4, column=2, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text='-', command= operationSubtraction).grid(row=4, column=3, sticky=tk.N+tk.E+tk.S+tk.W)

tk.Button(master, text='AC', command=operationReset).grid(row=5, column=0, columnspan=4, sticky=tk.N+tk.E+tk.S+tk.W)

inputAngka.insert(0, '0')
inputAngka.config(state='readonly')
tk.mainloop()
