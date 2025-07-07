HISTORY_FILE="history.text"

def showHistory():
    file = open(HISTORY_FILE,'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
                
                
def clearHistory():
    file=open(HISTORY_FILE,'w')
    file.close()
    print("History are cleared.")
    
def saveToHistory(equation, result):
    file=open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()
    
def calculate(userInput):
    parts=userInput.split()
    if len(parts) !=3:
        print('Invalid input. Use format: number operator number (e.g 6 + 6)')
        return
    
    
    num1=float(parts[0])
    op=parts[1] 
    num2=float(parts[2])
    
    if op =="+":
        result= num1 + num2
    elif op == "-":
        result = num1 - num2 
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 ==0:
            print("You cannot divide by zero")
            return
        result=num1/num2
    else:
        print("Invalid operator. USE ONLY  + - * /")
        return
    if int (result) == result:
        result = int(result)   
    print("Result: ", result)  
    saveToHistory(userInput, result) 
    
def main():
    print("---SIMPLE CALCULATOR (Type history, clear or exit)")
    while True:
        userInput=input("Enter calculator (+ - * /) or command (history, clear or exit )= ") 
        if userInput == 'exit':
            print("Goodbye")
            break
        elif userInput == 'history':
            showHistory()
        elif userInput == 'clear':
            clearHistory()
        else:
            calculate(userInput)             
            
main()            