from random import randint

def guess_namber(number=randint(1,100)):
    try:
        print("Привет,это угадай число от  1 до 100!У тебя будет 10 попыток")
        user_apttems =10
        for i in range(10):
            user_choice =int(input(f"Введи число.У тебя осталось {user_apttems}"))
            if user_choice <1 or user_choice >100:
                print("Ты можешь угадывать числы только от 1 до 100")
            else:
                if user_choice ==number:
                    print(f"Ты угадал!Загаданное число было {number}")
                    return number
                else:
                    user_apttems -=1
                if user_apttems <=0:
                    print("Ты проиграл!У тебя закончились попытки")
    except ValueError:
        print("Ты не можешь вводить дробные числа")
        return ""
if __name__ =="__main__":
    guess_namber()