# OBS-to-TXT: Ferramentas de Análise e Organização de Notas do Obsidian

Este repositório contém um conjunto de scripts e notebooks Jupyter projetados para analisar, organizar e extrair informações de notas do Obsidian. A principal funcionalidade é converter e processar arquivos Markdown (.md) do Obsidian em formatos mais estruturados, como CSV, facilitando a análise de dados e a geração de relatórios.

## Funcionalidades Principais

- **Conversão de Notas do Obsidian:** Scripts que extraem dados de arquivos Markdown do Obsidian, incluindo:
    - Nome da nota
    - Data da última modificação
    - Data da nota (se presente no conteúdo)
    - Tags (corrigindo o problema de detecção)
    - Contagem de palavras
    - Número de links internos (wiki-links `[[...]]`)
    - Caminho relativo da nota
- **Organização e Limpeza de Dados:** Notebooks Jupyter para limpar e preparar os dados extraídos, incluindo:
    - Conversão de strings de data para o tipo datetime.
    - Correção e padronização de tags.
    - Separação de tags em listas.
    - Criação de novas features (características) a partir dos dados existentes (ex: proporção palavras/links, contagem de tags, nível de profundidade no sistema de arquivos).
- **Análise Exploratória:** Notebooks para análise exploratória básica dos dados, com geração de estatísticas descritivas e visualizações (histogramas).

## Estrutura do Repositório
OBS-to-TXT/
├── 01Analize.ipynb # Notebook: Análise inicial dos dados limpos (sem output).
├── 02cleaning.ipynb # Notebook: Limpeza e pré-processamento dos dados (sem output).
├── 03Engenharia_de_características.ipynb # Notebook: Criação de novas features (sem output).
├── README.MD # Este arquivo.
├── app.py # Script Python (legado): Junta notas em um único arquivo .txt.
├── nome/
│ ├── app2.py # Script Python: Processamento de arquivos Markdown e extração de dados para CSV.
│ └── notas_consolidadas.txt # Exemplo de saída do script app2.py (notas concatenadas).
├── notas_consolidadas.txt # Exemplo de saída do script app.py (notas concatenadas).
└── teste.py # Script Python aprimorado: Processa arquivos MD e gera CSV (versão atualizada).

## Scripts Python

- **`app.py` (Legado):** Este script original junta todas as notas Markdown (.md) de uma pasta especificada em um único arquivo de texto (`notas_consolidadas.txt`).  Ele inclui o caminho completo do arquivo e a data da última modificação no arquivo de saída.  *Este script é considerado legado e foi substituído por `nome/app2.py` e `teste.py`.*

- **`nome/app2.py` (Versão anterior):** Uma versão aprimorada que extrai mais metadados dos arquivos Markdown e salva os resultados em um arquivo CSV (`notas_organizadas.csv`).  Extrai nome da nota, data de última modificação, data da nota (se presente no conteúdo), tags e contagem de palavras.  *Este script foi substituído por `teste.py`.*

- **`teste.py` (Versão Atual):** A versão mais recente e recomendada do script.  Ele *corrige problemas* encontrados em `nome/app2.py`, principalmente relacionados à extração de tags. Além das informações extraídas por `app2.py`, este script também inclui a contagem de links internos ([[...]]) e o caminho relativo do arquivo.

## Notebooks Jupyter (Sem Output)

Os notebooks Jupyter (`.ipynb`) na pasta raiz *não incluem as saídas das células de código*. Isso foi feito intencionalmente para manter o repositório limpo e permitir que você execute os notebooks e veja os resultados por si mesmo.

- **`01Analize.ipynb`:**  Análise exploratória inicial dos dados limpos. Inclui histogramas para contagem de palavras e links.

- **`02cleaning.ipynb`:**  Limpeza e pré-processamento dos dados. Inclui a conversão de datas, correção de tags (remoção de caracteres indesejados, separação em listas), e tratamento de valores ausentes.

- **`03Engenharia_de_características.ipynb`:** Criação de novas características (features) a partir dos dados existentes, como a proporção entre palavras e links, contagem de tags, e nível de profundidade da nota no sistema de arquivos (número de subpastas).

## Como Usar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/sua-conta/OBS-to-TXT.git
    cd OBS-to-TXT
    ```

2.  **Execute o script `teste.py`:**  
    Altere o caminho `pasta_inicial` no script `teste.py` para apontar para a pasta raiz do seu cofre do Obsidian (vault).  Execute o script:

    ```bash
    python teste.py
    ```
    Isso gerará um arquivo CSV (`notas_organizadas.csv`) com os dados extraídos dos seus arquivos Markdown.

3.  **Explore os notebooks Jupyter:**  
    Abra os notebooks (`01Analize.ipynb`, `02cleaning.ipynb`, `03Engenharia_de_características.ipynb`) com o Jupyter Notebook ou JupyterLab para explorar a análise, limpeza e criação de novas features.  Execute as células dos notebooks para ver os resultados.

## Notas Importantes

-   O script `teste.py` é a versão *mais atualizada* e *recomendada* para extrair dados dos seus arquivos Markdown do Obsidian. Os scripts `app.py` e `nome/app2.py` são versões anteriores e são mantidos para fins de histórico/referência.
-   Os notebooks Jupyter são fornecidos *sem as saídas*. Você precisará executá-los para ver os resultados.
-   O caminho para o seu cofre do Obsidian (variável `pasta_inicial` no script `teste.py`) *deve ser ajustado* antes de executar o script.

## Contribuições

Contribuições são bem-vindas! Se você encontrar bugs, tiver sugestões de melhorias ou quiser adicionar novas funcionalidades, sinta-se à vontade para criar um _pull request_.
