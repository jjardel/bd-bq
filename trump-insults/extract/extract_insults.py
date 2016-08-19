from lw import get_logger, get_header, get_root_logger

import argparse

from src import InsultExtractor


def main(path):

    insults = InsultExtractor()
    insults.extract()
    insults.export_to_csv(path)


if __name__ == '__main__':

    root_logger = get_root_logger()
    get_header(root_logger, "Extracting all of Trump's insults.  This may take a while...")

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='where would you like to extract to?')

    args = parser.parse_args()

    main(args.path)