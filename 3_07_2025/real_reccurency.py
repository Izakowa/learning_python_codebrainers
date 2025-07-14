data_json = {
            "glossary": {
                "title": "example glossary",
                "Alamakota": "var1",
                "GlossDiv": {
                    "title": "S",
                    "GlossList": {
                        "GlossEntry": {
                            "ID": "SGML",
                            "SortAs": "SGML",
                            "GlossTerm": "Standard Generalized Markup Language",
                            "Acronym": "SGML",
                            "Abbrev": "ISO 8879:1986",
                            "GlossDef": {
                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                "GlossSeeAlso": ["GML", "XML"]
                            },
                            "GlossSee": "markup"
                        }
                    }
                }
            }
        }

def find_paths(data, parent_key=''):
    paths = []
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, dict):
                sub_paths = find_paths(value, full_key)
                for sub_path in sub_paths:
                    paths.append(sub_path)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    sub_paths = find_paths(item, f"{full_key}[{i}]")
                    for sub_path in sub_paths:
                        paths.append(sub_path)
            else:
                paths.append(full_key)
    return paths


for element in (find_paths(data_json)):
    print(element)

