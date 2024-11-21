def dividir_arquivo(arquivo_original, num_arquivos, linhas_por_arquivo):
    """
    Divide um arquivo em um número específico de arquivos menores.

    Args:
        arquivo_original (str): Nome do arquivo a ser dividido.
        num_arquivos (int): Número de arquivos a serem criados.
        linhas_por_arquivo (int): Número de linhas por arquivo de saída.
    """

    try:
        with open(arquivo_original, 'r') as f:
            linhas = f.readlines()

        total_linhas = len(linhas)
        linhas_por_arquivo = min(linhas_por_arquivo, total_linhas)  # Limita o número de linhas por arquivo

        if num_arquivos > total_linhas:
            print(f"O número de arquivos desejado ({num_arquivos}) é maior que o número de linhas no arquivo original ({total_linhas}).")
            return

        # Calcula o número de linhas por arquivo, considerando o número total de arquivos
        linhas_por_arquivo = total_linhas // num_arquivos

        for i in range(num_arquivos):
            inicio = i * linhas_por_arquivo
            fim = min((i + 1) * linhas_por_arquivo, total_linhas)
            novo_arquivo = f"parte_{i+1}.txt"
            with open(novo_arquivo, 'w') as f:
                f.writelines(linhas[inicio:fim])
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_original}' não encontrado.")

# Exemplo de uso
arquivo = "Spanish.txt"
num_arquivos = 26
linhas_por_arquivo = 21157

dividir_arquivo(arquivo, num_arquivos, linhas_por_arquivo)