import json
from module import CoronaTracker


if __name__ == '__main__':
    ct = CoronaTracker()
    ct.parse()

    print(json.dumps(
        ct.all_statistic,
        indent=4,
    ))

    print(json.dumps(
        ct.country_statistic,
        indent=4,
    ))