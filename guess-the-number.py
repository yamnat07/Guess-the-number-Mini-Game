import random
secret_num=random.randint(1,100)

def guess_it(secret_num):
    
    print("="*20)
    print("GUESS THE NUMBER")
    print("="*20)
    print("I have chosen a number, can you guess it?")
    attempts=0
    while True:   
        try:
            your_guess=int(input("Enter your Guess: "))
            if your_guess<1 or your_guess>100:
                print("Enter a number from 1 to 100.")
                continue
            attempts+=1       
            if your_guess>secret_num:
                print("Too High! Try a smaller number.")
            elif your_guess<secret_num:
                print("Too Low! Try a higher number.")
            else:
                print("Congratulations!!! You Guessed the right number.")
                print(f"Correct number:{secret_num}")
                print("===RESULTS===")
                print(f"Total Attempts:{attempts}")
                break
        except ValueError:
            print("Enter a number.")

def main():
    guess_it(secret_num)
    while True:
        print("1.Play again")
        print("2.Exit")
        try:
            choice=int(input("Enter your choice: "))
            if choice==1:
                secret_num2=random.randint(1,100)
                guess_it(secret_num2)
            elif choice==2:
                print("Thanks For Playing!Hope you beat your score next time.")
                break
            else:
                print("Enter a valid choice!!!!")
        except ValueError:
            print("Enter a valid number!!")
main()                       