import random

def guess_number():
    global i
    global target_num
    while True:
        try:
            num = input("Enter your guess:")
            num = int(num)
        except ValueError:
            print("choose correct number")
            continue
        if num<target_num:
            print("Too low!")
            i+=1
        elif num>target_num:
            print("Too high!")
            i+=1
        else:
            print(f"Congratulations! You've guessed the number in {i} attempts.")
            break
    

target_num = random.randint(1,100)
print(target_num)
i=1

guess_number()

