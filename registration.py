#!/usr/bin/env python3
""" Account registration system"""

import csv
import sys
import time

file_written = False
file = "user_data.csv"


def get_first_name() -> str:
    while True:
        try:
            first_name = input("First Name: ")
            if first_name == "":
                raise ValueError
            break
        except ValueError:
            print("Field is empty, please enter your First Name.")

    return first_name


def get_last_name() -> str:
    while True:
        try:
            last_name = input("Last Name: ")
            if last_name == "":
                raise ValueError
            break
        except ValueError:
            print("Field is empty, please enter your last name.")

    return last_name


def get_email() -> str:
    while True:
        try:
            email = input("Email: ")
            if email == "":
                raise ValueError
            break
        except ValueError:
            print("Field is empty, please enter your email.")

    return email


def get_password() -> str:
    while True:
        try:
            password = input("Password: ")
            if password == "":
                raise ValueError
            break
        except ValueError:
            print("Field is empty, please enter your password.")

    return password


def input_user_data() -> list:
    print("Sign Up!")
    first_name = get_first_name()
    last_name = get_last_name()
    email = get_email()
    password = get_password()
    user_data = [first_name, last_name, email, password]

    return user_data


def user_registration(file: str, file_written: bool):
    user_data = input_user_data()
    header = ["first_name", "last_name", "email", "password"]
    if file_written == False:
        with open(file, "w") as out:
            csv_writer = csv.writer(out, delimiter="\t")
            csv_writer.writerow(header)
            csv_writer.writerow(user_data)
    else:
        data_read = []
        with open(file, "r") as in_data:
            csv_reader = csv.reader(in_data, delimiter="\t")

            for line in csv_reader:
                data_read.append(line)
            data_read.append(user_data)

            with open(file, "w") as out:
                csv_writer = csv.writer(out, delimiter="\t")

                for line in data_read:
                    csv_writer.writerow(line)


def read_user_data(file):
    with open(file, "r") as in_data:
        csv_reader = csv.reader(in_data, delimiter="\t")
        print("\n")
        print("=" * 50)
        print("        USERS")
        print("=" * 50)

        for line in csv_reader:
            for data in line:
                print(data, end=" ")
            print()
        print("=" * 50, "\n")


def menu() -> None:
    print("What do you wish to do by now?")
    print(
        """
        1) Register Users
        2) Read Users Data
        3) Quit
        """
    )


def choice_selection(choice: int, file: str, file_written: bool):
    if choice == 1:
        user_registration(file, file_written)
    elif choice == 2:
        read_user_data(file)
    else:
        print("Bye!")
        sys.exit()


def get_menu_choice(file: str, filewritten: bool):
    while True:
        menu()
        try:
            choice = int(input("-> "))
            if choice not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("ERROR: Invalid choice")
            time.sleep(2)
            continue

        choice_selection(choice, file, file_written)


if __name__ == "__main__":
    try:
        get_menu_choice(file, file_written)
    except KeyboardInterrupt:
        print("See you around!")
        print("Bye!")
        time.sleep(2)
