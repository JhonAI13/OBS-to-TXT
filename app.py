import os
from datetime import datetime

def juntar_notas_em_txt(pasta_inicial, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo_txt:
        for root, dirs, files in os.walk(pasta_inicial):
            for file in files:
                if file.endswith(".md"):
                    caminho_completo = os.path.join(root, file)
                    
                    # Obtém a data de última modificação
                    ultima_modificacao = os.path.getmtime(caminho_completo)
                    data_formatada = datetime.fromtimestamp(ultima_modificacao).strftime('%Y-%m-%d %H:%M:%S')

                    # Adiciona o caminho do arquivo e a data de edição no txt
                    arquivo_txt.write(f"\n\n### Caminho: {caminho_completo}\n")
                    arquivo_txt.write(f"### Última modificação: {data_formatada}\n\n")

                    # Lê o conteúdo do arquivo .md
                    with open(caminho_completo, 'r', encoding='utf-8') as arquivo_md:
                        conteudo = arquivo_md.read()
                        arquivo_txt.write(conteudo)

    print(f"Arquivo consolidado criado: {arquivo_saida}")

# Caminho da pasta onde estão suas notas em .md
pasta_inicial = r"C:\Users\jonat\Dropbox\Obsidian\obsidian"
# Arquivo onde todas as notas serão concatenadas
arquivo_saida = "notas_consolidadas.txt"

juntar_notas_em_txt(pasta_inicial, arquivo_saida)

