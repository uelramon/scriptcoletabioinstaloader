#!/usr/bin/env python
# coding: utf-8

# In[4]:


import instaloader
import getpass

L = instaloader.Instaloader()

usuario = "SEUUSUARIO"
senha = getpass.getpass("Digite sua senha do Instagram: ")

L.login(usuario, senha)
L.save_session_to_file()
print("Sessão salva com sucesso.")


# In[1]:


import pandas as pd
import instaloader
import time
import os
from instaloader.exceptions import ConnectionException, ProfileNotExistsException

# Caminho para o arquivo de sessão salvo pelo script de importação do Firefox
session_file_path = "/Users/mac/.config/instaloader/session-medialabfoz"  # Altere este nome se necessário
usuario = "uel.ramon@gmail.com"  # Substitua pelo seu nome de usuário do Instagram

# Inicializa o Instaloader
L = instaloader.Instaloader()

# Verifica se o arquivo de sessão existe e o carrega
if os.path.exists(session_file_path):
    try:
        L.load_session_from_file(usuario, filename=session_file_path)
        print("Sessão carregada com sucesso a partir do cookie do Firefox.")
    except Exception as e:
        print(f"Erro ao carregar a sessão: {e}")
else:
    raise FileNotFoundError(f"Arquivo de sessão não encontrado: {session_file_path}")

# Carregar a planilha com as contas
caminho_arquivo = "contas_instagram.xlsx"
df_contas = pd.read_excel(caminho_arquivo)

# Verificar se a coluna 'Contas' existe
if "Contas" not in df_contas.columns:
    raise ValueError("A coluna 'Contas' não foi encontrada na planilha.")

# Obter a lista de contas
lista_contas = df_contas["Contas"].dropna().astype(str).tolist()

# Exibir as contas carregadas para conferência
print(f"Total de contas carregadas: {len(lista_contas)}")
print(lista_contas[:10])  # Exibir as 10 primeiras como exemplo

# === 3. Verificar se já existe coleta parcial salva ===
arquivo_saida = "coleta_temp.xlsx"
if os.path.exists(arquivo_saida):
    df_existente = pd.read_excel(arquivo_saida)
    contas_coletadas = set(df_existente["username"].tolist())
    print(f"⚠️ {len(contas_coletadas)} contas já coletadas serão ignoradas.")
    dados = df_existente.to_dict('records')
else:
    contas_coletadas = set()
    dados = []

# === 4. Coleta dos dados com salvamento incremental ===
for conta in lista_contas:
    if conta in contas_coletadas:
        print(f"⏩ Já coletado: {conta}")
        continue

    try:
        profile = instaloader.Profile.from_username(L.context, conta)
        dados.append({
            'username': profile.username,
            'full_name': profile.full_name,
            'bio': profile.biography,
            'seguidores': profile.followers,
            'seguindo': profile.followees,
            'publicacoes': profile.mediacount,
            'is_verified': profile.is_verified
        })

        print(f"✅ Coletado: {conta}")

        # Salvar a cada conta coletada
        pd.DataFrame(dados).to_excel(arquivo_saida, index=False)

        time.sleep(3)  # Pausa para evitar bloqueios

    except ProfileNotExistsException:
        print(f"⚠️ Perfil não existe ou foi removido: {conta}")
        continue

    except ConnectionException as ce:
        print(f"❌ Conexão falhou para {conta}: {ce}")
        print("⏸️ Aguardando 60 segundos para tentar novamente...")
        time.sleep(60)
        continue

    except Exception as e:
        print(f"⚠️ Erro inesperado para {conta}: {e}")
        continue

print("\n✅ Coleta finalizada!")



# In[2]:


get_ipython().system('pip install instaloader')


# In[ ]:




