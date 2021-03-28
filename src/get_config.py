import json
import sys


def read_json(file):
    path = f'src/{file}'
    with open(path) as f:
        return json.loads(f.read())


if __name__ == '__main__':
    path = str(sys.argv[1])
    print(read_json(path))