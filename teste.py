import os
import re
from datetime import datetime
import csv

def process_markdown_files(pasta_inicial, arquivo_saida):
    """
    Processa arquivos Markdown em uma pasta, extraindo informações como título, tags, data, contagem de palavras, links e caminho,
    e salva os resultados em um arquivo CSV.
    """
    with open(arquivo_saida, 'w', encoding='utf-8', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['Nome da Nota', 'Data da Última Modificação', 'Data da Nota', 'Tags', 'Contagem de Palavras', 'Links', 'Caminho da Nota'])

        for root, dirs, files in os.walk(pasta_inicial):
            for file in files:
                if file.endswith(".md"):
                    caminho_completo = os.path.join(root, file)
                    
                    try:
                        with open(caminho_completo, 'r', encoding='utf-8') as arquivo_md:
                            conteudo = arquivo_md.read()
                            
                            nome_nota = os.path.splitext(file)[0]
                            
                            # Data da última modificação
                            ultima_modificacao = os.path.getmtime(caminho_completo)
                            data_formatada = datetime.fromtimestamp(ultima_modificacao).strftime('%Y-%m-%d %H:%M:%S')

                            # Data da nota
                            data_match = re.search(r'data:\s*(\d{4}-\d{2}-\d{2})', conteudo, re.IGNORECASE)
                            data_nota = data_match.group(1) if data_match else ""
                            
                            # Tags
                            tags_match = re.findall(r'tags:\s*([^\n]+)', conteudo, re.IGNORECASE)
                            tags = ""
                            if tags_match:
                                all_tags = []
                                for match in tags_match:
                                    tags_lines = match.strip().split('\n')
                                    for line in tags_lines:
                                        tag = re.sub(r'^-\s*', '', line).strip()
                                        if tag:
                                            all_tags.append(tag)

                                tags = ", ".join(all_tags)
                            
                            # Contagem de palavras
                            palavras = re.findall(r'\b\w+\b', conteudo)
                            contagem_palavras = len(palavras)

                            # Contagem de links
                            contagem_links = len(re.findall(r'\[\[.*?\]\]', conteudo))

                            # Caminho da nota
                            caminho_nota = os.path.relpath(caminho_completo, pasta_inicial)  # Usa relpath para obter caminho relativo


                            # Escreve os resultados no CSV
                            writer.writerow([nome_nota, data_formatada, data_nota, tags, contagem_palavras, contagem_links, caminho_nota])


                    except Exception as e:
                        print(f"Erro ao processar {file}: {e}")
                        
    print(f"Arquivo CSV criado: {arquivo_saida}")


# Caminho da pasta onde estão suas notas em .md
pasta_inicial = r"C:\Users\jonat\Dropbox\Obsidian\obsidian" # Substitua pelo caminho correto
# Arquivo onde todas as notas serão concatenadas
arquivo_saida = "notas_organizadas.csv"

process_markdown_files(pasta_inicial, arquivo_saida)