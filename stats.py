import sys
import re
from collections import Counter

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please specify the log file")
        sys.exit()

    with open(filename, 'rb') as f:
        count_url = Counter()
        count_status = Counter()

        url_list = []
        status_list = []

        for l in f:
            # tem uns caracteres especiais no começo do arquivo de log
            line = l.decode('utf-8', errors="ignore")

            url = re.search('request_to=\"([^\"]*)\"', line)
            if url: url_list.append(url.group(1))

            status = re.search('response_status=\"([^\"]*)\"', line)
            if status: status_list.append(status.group(1))

        for item in Counter(url_list).most_common(3):
            print(f"{item[0]} - {item[1]}")

        print()

        for item in Counter(status_list).most_common():
            print(f"{item[0]} - {item[1]}")
