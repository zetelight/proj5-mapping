import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


def process(raw):
    print("TEST")


def main():
    f = open("data/POI.txt")
    parsed = process(f)
    print(parsed)


if __name__ == "__main__":
    main()
