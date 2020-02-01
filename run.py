import json
from module import CoronaTracker


if __name__ == '__main__':
    ct = CoronaTracker()
    ct.parse()

    print(json.dumps(
        ct.get_all_statistics(),
        indent=4,
    ))

    print(json.dumps(
        ct.get_country_statistics(),
        indent=4,
    ))