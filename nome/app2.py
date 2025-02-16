import os
import re
from datetime import datetime
import csv

def process_markdown_files(pasta_inicial, arquivo_saida):
    """
    Processa arquivos Markdown em uma pasta, extraindo informações como título, tags, data e contagem de palavras,
    e salva os resultados em um arquivo CSV.
    
    Args:
        pasta_inicial (str): O caminho para a pasta que contém os arquivos Markdown.
        arquivo_saida (str): O caminho para o arquivo CSV de saída.
    """
    with open(arquivo_saida, 'w', encoding='utf-8', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['Nome da Nota', 'Data da Última Modificação', 'Data da Nota', 'Tags', 'Contagem de Palavras'])
        
        for root, dirs, files in os.walk(pasta_inicial):
            for file in files:
                if file.endswith(".md"):
                    caminho_completo = os.path.join(root, file)
                    
                    # Obtém a data de última modificação
                    ultima_modificacao = os.path.getmtime(caminho_completo)
                    data_formatada = datetime.fromtimestamp(ultima_modificacao).strftime('%Y-%m-%d %H:%M:%S')
                    
                    try:
                        with open(caminho_completo, 'r', encoding='utf-8') as arquivo_md:
                            conteudo = arquivo_md.read()

                            # Extrai o nome do arquivo (sem extensão) como nome da nota
                            nome_nota = os.path.splitext(file)[0]
                            
                            # Busca a data dentro do conteúdo do arquivo
                            data_match = re.search(r'data: (\d{4}-\d{2}-\d{2})', conteudo)
                            data_nota = data_match.group(1) if data_match else ""

                            # Busca as tags no arquivo
                            tags_match = re.search(r'tags:\s*(\n\s*-\s*[\w\s]+)+', conteudo)
                            tags = ""
                            if tags_match:
                                tag_list = re.findall(r'- ([\w\s]+)', tags_match.group(0))
                                tags = ", ".join([tag.strip() for tag in tag_list])
                            
                            # Conta o número de palavras do conteúdo
                            palavras = re.findall(r'\b\w+\b', conteudo)
                            contagem_palavras = len(palavras)

                            # Escreve os resultados no CSV
                            writer.writerow([nome_nota, data_formatada, data_nota, tags, contagem_palavras])
                    except Exception as e:
                        print(f"Erro ao processar {file}: {e}")

    print(f"Arquivo CSV criado: {arquivo_saida}")

# Caminho da pasta onde estão suas notas em .md
pasta_inicial = r"C:\Users\jonat\Dropbox\Obsidian\obsidian"
# Arquivo onde todas as notas serão concatenadas
arquivo_saida = "notas_organizadas.csv"

process_markdown_files(pasta_inicial, arquivo_saida)