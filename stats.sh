#!/bin/sh

# cut separa pelas aspas e pega a segunda parte
# sort uniq -c sort -nr conta linhas repetidas e ordena pelas mais frequentes
# awk troca as colunas para deixar no formato pedido na especificação
order_by_freq() {
    cut -d '"' -f2 | sort | uniq -c | sort -nr | awk '{print $2 " - " $1}'
}

# o primeiro GREP seleciona matches para request_to="..."
# head -n 3 seleciona as três primeiras linhas
grep --text -o -E 'request_to=\"[^\"]*\"' $1 | order_by_freq | head -n 3;
echo;
grep --text -o -E 'response_status=\"\d+\"' $1 | order_by_freq
