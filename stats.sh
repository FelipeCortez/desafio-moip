#!/bin/sh

order_by_freq() {
    cut -d '"' -f2 | sort | uniq -c | sort -nr | awk '{print $2 " - " $1}'
}

grep --text -o -E 'request_to=\"[^\"]*\"' $1 | order_by_freq | head -n 3;
echo;
grep --text -o -E 'response_status=\"\d+\"' $1 | order_by_freq
