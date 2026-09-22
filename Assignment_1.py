
	# Program Name: Assignment1.py
	# Course: IT3883
	# Student Name: Michael Burrough
	# Assignment Number: Lab1
	# Due Date: 9/22/ 2026
	# Purpose: Program will append data and display as well. Program will also clear data on request.
	# Resources: https://stackoverflow.com/questions/38283475/how-to-create-an-interactive-text-menu-in-python
    #https://stackoverflow.com/questions/26965931/how-to-take-input-for-a-stringbuffer-object-in-java
    #https://stackoverflow.com/questions/26965931/how-to-take-input-for-a-stringbuffer-object-in-java








def main():

    input_buffer = ""

    while True:
        print("\n--- MENU ---")
        print("1.Append data")
        print("2.Clear the input ")
        print("3.Display the input ")
        print("4.Exit ")

        choice = input("\nEnter choice from (1-4): ").strip()

        if choice == "1":

            user_string = input("Enter string to append: ")
            input_buffer += user_string
            print("Data appended.")

        elif choice == "2":

            input_buffer = ""
            print("Input cleared")

        elif choice == "3":
            if input_buffer == "":
                print("[Input is empty]")

            else:
                print(f" Buffer: {input_buffer}")

        elif choice == "4":
            print("Exiting..")
            break

        else:

            print("Invalid")
            
if __name__ == "__main__":

    main()
