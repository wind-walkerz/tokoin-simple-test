import utils
import sys
import re

class Questionnaires:
    def get_search_entity(self, entities):
        print("Select ")

        for index, key in enumerate(entities):
            print(f"{index + 1}) {utils.capitalize(key)}")

        choice = ''
        while not re.search("^[123]$", choice):
            choice = input()

            if re.search("^[123]$", str(choice)):
                return entities[(int(choice) - 1)]
            elif choice == "quit":
                sys.exit(1)
            else:
                print("\n Invalid option please choose again. \n")


    def get_search_prop(self, searchable_props):
        print("Enter search prop ")
        choice = ''

        while choice not in searchable_props:
            choice = input()

            if choice in searchable_props:
                return choice
            elif choice == "quit":
                sys.exit(1)
            else:
                print("Property does not exist. \n")
                print("List of property that you can search")
                for i in searchable_props:
                    print(i)
                print("\n")


    def get_search_query(self):
        print("Enter search value")
        choice = input()
        if choice == "quit":
            sys.exit(1)
        else:
            return choice
