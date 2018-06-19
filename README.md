# Desafio Moip
"Você deve parsear o arquivo e no final mostrar as seguintes informações na saída:"
- 3 urls mais chamadas com a quantidade
- Uma tabela mostrando a quantidade de webhooks por status

## Modo de usar
Para stats.sh:
```sh
$ chmod +x stats.sh
$ ./stats.sh log.txt
```

Para stats.py (com Python 3.6):
```sh
$ python3 stats.py log.txt
```

Para testar stats.py:
```sh
$ python3 test.py
```

Também é possível passar os parâmetros "-n N" para escolher a quantidade de URLs exibidas e "-a/--all" para mostrar todas as URLs

```sh
$ python3 stats.py log.txt -n 10
```

```sh
$ python3 stats.py log.txt -a
```
