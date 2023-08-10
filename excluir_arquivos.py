import os
import shutil
import time
import datetime

def delete_folders_with_progress(folder_list):
    total_folders = len(folder_list)
    bar_length = 40

    for i, folder in enumerate(folder_list, 1):
        progress = i / total_folders
        arrow = '=' * int(round(progress * bar_length))
        spaces = ' ' * (bar_length - len(arrow))
        print(f'\rDeleting [{arrow}{spaces}] {progress:.0%}', end='', flush=True)

        try:
            # Deletar a pasta e seu conteúdo
            shutil.rmtree(folder)
            print(f"\nDeletado: {folder}")
        except Exception as e:
            print(f"\nErro ao deletar {folder}: {e}")
        
        time.sleep(0.1)  # Simulando alguma latência
    print("\nArquivos Deletados com sucesso.")

# Diretório onde as pastas serão deletadas (alterar de acordo com o local de exclusão de arquivos)
target_directory = "C:\geste"

# Obter o dia atual do mês
current_day = datetime.datetime.now().day

# Mapear as letras do alfabeto para os dias do mês (a=1, b=2, ..., z=26)
alphabet_to_day = {chr(ord('a') + i): i + 1 for i in range(26)}

# Obter a lista de pastas a serem deletadas de acordo com o dia do mês
folders_to_delete = [os.path.join(target_directory, folder) for folder in os.listdir(target_directory)
                     if os.path.isdir(os.path.join(target_directory, folder))
                     and folder[0].lower() in alphabet_to_day
                     and alphabet_to_day[folder[0].lower()] == current_day]

delete_folders_with_progress(folders_to_delete)
