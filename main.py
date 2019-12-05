import sys
import os
import utils
from src.records import Records
from src.questionnaires import Questionnaires
from src.broadcaster import Broadcaster

broadcaster = Broadcaster()
questionnaires = Questionnaires()
users = Records('users')
tickets = Records('tickets')
organizations = Records('organizations')
entities = ['users', 'tickets', 'organizations']
data_mapper = utils.read_file('data/relation_mapper.json')


def main():

    os.system('cls||clear')

    broadcaster.display_title()

    broadcaster.display_main_menu()

    choice = ""

    while not choice == 1:
        choice = input()
        if choice == '1':
            start_search()
        elif choice == "2":
            for entity in entities:
                broadcaster.display_searchable_properties(globals()[entity])

            broadcaster.display_main_menu()
        elif choice == "quit":
            sys.exit(1)
        else:
            print("\n Invalid option please choose again. \n")


def start_search():
    entity_name = questionnaires.get_search_entity(entities)
    instance = globals()[entity_name]
    prop = questionnaires.get_search_prop(instance.get_searchable_props())
    query = questionnaires.get_search_query()

    print(
        f"\n Searching {entity_name} for {prop} property with a value of {query}")

    result = instance.search(prop, query)

    if result:
        coerced_result = list(map(lambda x:get_related_data(entity_name, x), result))
        broadcaster.display_search_result(coerced_result)
    else:
        print("\n No results found")


def get_related_data(entity_name: str, context: dict) -> dict:
    _id, organization_id, assignee_id, submitter_id = utils.pluck(
        context, ['_id', 'organization_id', "assignee_id", "submitter_id"]
    )

    for statement in data_mapper[entity_name]:
        instance = globals()[statement['entity']]
        query = locals()[statement['query_key']]
        prop = statement['prop']
        subject = statement['subject']
        output_prop = 'subject' if statement['entity'] == 'tickets' else 'name'

        context[subject] = instance.find(prop, query, output_prop)

    return context


if __name__ == '__main__':
    main()
