## Script para salvar dos de excel em banco de dados

Este script lê um arquivo excel e salva os dados em um banco de dados neste exemplo, `SQLite`.

#### Etapas aplicadas:
- 1 - Normaliza o texto das colunas com função `normalize_column_name()`, substituindo caracteres espaciais;

- 2 - Processa os nomes das colunas `process_column_names()`;

- 3 - Salva os dados no banco de dados com a função `save_to_db()`.


#### Instalar depedências:

Windows:
```PowerShell
py -m pip install -r requirements.txt
```

Linux/MAC:
```Bash
python3 -m pip install -r requirements.txt
```
