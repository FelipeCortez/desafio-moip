#!/bin/sh

# cut separa pelas aspas e -f2 pega a segunda parte
# tr deixa tudo em minúsculas
# sort uniq -c sort -nr conta linhas repetidas e ordena pelas mais repetidas
# awk troca as colunas para deixar no formato solicitado na especificação
order_by_freq() {
    cut -d '"' -f2 | tr '[A-Z]' '[a-z]' | sort | uniq -c | sort -k1nr -k2 | awk '{print $2 " - " $1}'
}

# não continuar se não encontrar arquivo
set -o pipefail
# o primeiro GREP seleciona casamentos para request_to="..."
# head -n 3 seleciona as três primeiras linhas do resultado
grep --text -o -E 'request_to=\"[^\"]*\"' $1 | order_by_freq | head -n 3 &&
echo &&
grep --text -o -E 'response_status=\"\d+\"' $1 | order_by_freq
