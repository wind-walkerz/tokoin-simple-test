import utils
import json


class Broadcaster:
    def display_title(self):
        print("\n Type 'quit' to  exit at any time, Press 'Enter' to continue")
        print("\n Select search options:")

    def display_main_menu(self):
        print("\n  * Type 1 to search")
        print("\n  * Type 2 to view a list of searchable fields")
        print("\n  * Type 'quit' to exit")

    def display_searchable_properties(self, instance):
        name = utils.capitalize(instance.name)

        print("\n----------------------------------------------------------")
        print(f"Search {name} with")

        for i in instance.get_searchable_props():
            print(i)

    def display_search_result(self, result):
        # full_result = list(
        #     map(
        #         lambda x: get_related_data(entity_name, x),
        #         result
        #     ))
        #
        print(json.dumps(result, indent=4))
        #
        with open('result.json', 'w') as outfile:
            json.dump(result, outfile)
