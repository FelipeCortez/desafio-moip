import sys
import re
import argparse
from collections import Counter

by_count_then_lex = lambda lex_count: (-lex_count[1], lex_count[0])

def parse_file(
        filename: str,
        site_count: int = 3,
        all_sites: bool = False):
    try:
        with open(filename, 'rb') as f:
            output_str = []
            url_list = []
            status_list = []

            for l in f:
                # ignora caracteres especiais no arquivo de log
                line = l.decode('utf-8', errors="ignore")

                url = re.search('request_to=\"([^\"]*)\"', line)
                if url: url_list.append(url.group(1).lower())

                status = re.search('response_status=\"([^\"]*)\"', line)
                if status: status_list.append(status.group(1))

            site_count = site_count if not all_sites else None
            counter_url = Counter(url_list).most_common(site_count)
            for item in sorted(counter_url, key=by_count_then_lex):
                output_str.append(f"{item[0]} - {item[1]}")

            output_str.append("")

            counter_status = Counter(status_list)
            for item in sorted(counter_status):
                output_str.append(f"{item} - {counter_status[item]}")

        if counter_url and counter_status:
            return "\n".join(output_str)
        else:
            raise ValueError("Malformed log file")

    except OSError as e:
        print("File not found")
        sys.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='URLs e status codes')
    parser.add_argument('-n', required=False, type=int,
                        help='how many URLs should be shown', default=3)
    parser.add_argument('-a', '--all', action="store_true",
                        help='show all sites')
    parser.add_argument('filename', help='log file')

    args = parser.parse_args()

    try:
        print(parse_file(args.filename, args.n, args.all))
    except IndexError:
        print("Please specify the log file")
        sys.exit()
