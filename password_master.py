
import random
import string
import os

# Function for auto password generation
def auto_generate_passwords(count, length):
    names = ["John", "Alice", "Bob", "Charlie", "Eve", "Grace", "Mallory", "Oscar", "Peggy", "Victor"]
    passwords = [
        random.choice(names) + ''.join(random.choice(string.digits) for _ in range(length - len(random.choice(names))))
        for _ in range(count)
    ]
    return passwords

# Function for multi-word password generation
def multi_word_passwords(count, words):
    password_list = [' '.join(random.choice(words) for _ in range(7)) for _ in range(count)]
    return password_list

# Function for name-based password generation
def name_based_password(name, count, length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = [
        name + ''.join(random.choice(characters) for _ in range(length - len(name)))
        for _ in range(count)
    ]
    return passwords

# Main Function
def main():
    os.system('clear')

    # Display HEX logo
    print("\n" * 2)
    print("\033[1;32m" + " " * 20 + "HH   HH  \033[1;31m EEEEE   \033[1;32m XX   XX")
    print("\033[1;32m" + " " * 20 + "HH   HH  \033[1;31m EE      \033[1;32m  XX XX ")
    print("\033[1;32m" + " " * 20 + "HHHHHHH  \033[1;31m EEEE    \033[1;32m   XXX  ")
    print("\033[1;32m" + " " * 20 + "HH   HH  \033[1;31m EE      \033[1;32m  XX XX ")
    print("\033[1;32m" + " " * 20 + "HH   HH  \033[1;31m EEEEE   \033[1;32m XX   XX \033[0m")
    print("\n")

    # Programmer and coder details
    print("\033[1;32m" + " " * 20 + "Programmer: Hacker Hex")
    print(" " * 20 + "Coder: Ali Sher\033[0m")
    print("\n")

    while True:
        # Menu options
        print("\033[1;32m1. Auto Password Generator (1000 passwords)\033[0m")  # Green
        print("\033[1;34m2. 1 to 7 Words Password Generator (1000 passwords)\033[0m")  # Blue
        print("\033[1;32m3. Name-based Password Generator (10,000 passwords)\033[0m")  # Green
        print("\033[1;34m4. Exit\033[0m")  # Blue
        
        option = input("\033[1;32mEnter your choice (1/2/3/4): \033[0m")

        if option == '1':
            print("\n\033[1;32mGenerating 1000 passwords...\033[0m")
            passwords = auto_generate_passwords(1000, 12)
            for password in passwords:
                print(password)
        
        elif option == '2':
            words = ["apple", "banana", "cherry", "dog", "elephant", "fish", "grape", "hat", "ice", "jungle"]
            print("\n\033[1;32mGenerating 1000 passwords with 1 to 7 words...\033[0m")
            passwords = multi_word_passwords(1000, words)
            for password in passwords:
                print(password)
        
        elif option == '3':
            name = input("\n\033[1;32mEnter the name for generating passwords: \033[0m")
            print("\033[1;32mGenerating 10,000 passwords for the name...\033[0m")
            passwords = name_based_password(name, 10000, 12)
            for password in passwords:
                print(password)
        
        elif option == '4':
            print("\n\033[1;32mExiting the tool. Goodbye!\033[0m")
            break
        else:
            print("\033[1;31mInvalid option. Please try again.\033[0m")

# Run the tool
if __name__ == "__main__":
    main()

