import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


def process(raw):
    locations = []
    for line in raw:
        entry = {}
        log.debug("Line: {}".format(line))
        line = line.strip()
        if len(line) == 0 or line[0] == "#":
            log.debug("Skipping")
            continue
        parts = line.split(',')
        for i in range(len(parts)):
            entry["Description"], entry["lat"], entry["lon"] = parts[0], float(parts[1]), float(parts[2])
        locations.append(entry)
    return locations


def main():
    f = open("data/POI.txt")
    parsed = process(f)
    print(parsed)


if __name__ == "__main__":
    main()
