import utils


class Records:
    def __init__(self, name):
        self.name = name
        self.data = self.import_data()

    def get_searchable_props(self) -> list:
        return self.data[0].keys()

    def search(self, prop, query):
        is_strict = prop == '_id'
        result = []
        for item in self.data:
            if prop in item and utils.search_text(query, item[prop], is_strict):
                result.append(item)
        return result

    def find(self, prop, query, output_prop) -> [str, list]:
        if query:
            result = list(
                filter(
                    lambda x: prop in x and utils.is_match(x[prop], query),
                    self.data)
            )

            if len(result) == 0:
                return ""
            elif len(result) == 1:
                print(result)
                return result[0][output_prop]
            else:
                return list(map(lambda x: x[output_prop], result))
        else:
            return ""

    def import_data(self):
        return utils.read_file(f'data/{self.name}.json')