'''
PROGRAM LATIHAN ARITMATIKA RADIX
'''
from random import randint
import time, os

def main():
    running = True
    print("Welcome to the radix arithmetic practice!")
    
    while running:
        print("What do you want to practice today?\n" + 40*"=")
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Challenge Mode")
        practice_type = input("Your pick: ").strip().upper()
        if practice_type == 'E':
            challenge_mode()
        elif practice_type in ["A", "B", "C", "D"]:
            score, time = normal_mode(practice_type)
        else:
            print("Pick an actual option, you dolt")
            continue
        exit = input("Do you want to play again? (y/n): ").lower().strip()
        if exit != 'y':
            running = False
            print('bbye')
            time.sleep(1)
          
        
def normal_mode(practice_type):
    while True:
        try: 
            radix = int(input("Radix: "))
            digit = int(input("Digit Amounts: "))
            break
        except ValueError:
            print("Input invalid")
            
    upper = radix ** digit - 1
    jumlah_soal = 10
    correct = False
    start_time = time.time()
    score = 0
    
    for i in range(jumlah_soal):
        if correct:
            print(f"Correct! The answer is {converted_answer}")
        dec_num2 = randint(0, upper)
        if practice_type in ["B", "D"]:
            dec_num1 = randint(dec_num2, upper)
        else:
            dec_num1 = randint(0, upper)
        converted_num1 = num_converter(dec_num1, radix)
        converted_num2 = num_converter(dec_num2, radix)
        
        if practice_type == "A":
            dec_answer = dec_num1 + dec_num2
            operator = '+'
        elif practice_type == "B":
            dec_answer = dec_num1 - dec_num2
            operator = '-'
        elif practice_type == "C":
            dec_answer = dec_num1 * dec_num2
            operator = '*'
        elif practice_type == "D":
            dec_answer = dec_num1 // dec_num2
            operator = '//'

        converted_answer = num_converter(dec_answer, radix)
        correct = False
    
        while not correct:
            clear()
            print(f'Question {i + 1}: What is {converted_num1} {operator} {converted_num2}?')
            answer = input('Insert your answer: ')
            if answer == converted_answer:
                correct = True
                score += 1
            else:
                print("Incorrect answer! Try again.")
    return score, time.time() - start_time

# TODO: make challenge mode a function
def challenge_mode():
    pass

'''Function that returns a tuple of a random decimal function and the conversion result'''
def num_converter(dec_num, radix):
    # chars = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    chars = "0123456789ABCDEF"
    converted_num = ""
    while dec_num:
        index = dec_num % radix
        converted_num = chars[index] + converted_num
        dec_num //= radix
    return converted_num


def clear(): # Code by Google
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
        
main()