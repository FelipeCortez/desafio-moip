import sys
import re
from collections import Counter

by_count_then_lex = lambda lex_count: (-lex_count[1], lex_count[0])

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please specify the log file")
        sys.exit()

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

            counter_url = Counter(url_list).most_common(3)
            for item in sorted(counter_url, key=by_count_then_lex):
                output_str.append(f"{item[0]} - {item[1]}")

            output_str.append("")

            counter_status = Counter(status_list).most_common()
            for item in sorted(counter_status, key=by_count_then_lex):
                output_str.append(f"{item[0]} - {item[1]}")

        if counter_url and counter_status:
            print("\n".join(output_str))
        else:
            print("Malformed log file")

    except OSError:
        print("File not found")
