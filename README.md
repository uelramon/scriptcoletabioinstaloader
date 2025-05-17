✅ README.md
markdown
Copiar
Editar
# 📊 Coleta de Dados de Bios no Instagram

Este script realiza a coleta automatizada de informações públicas das bios de contas do Instagram, utilizando a biblioteca [Instaloader](https://instaloader.github.io/). Ele foi desenvolvido para fins de pesquisa e análise de perfis públicos, com salvamento incremental e checagem de erros comuns durante o scraping.

## 🧩 Funcionalidades

- Autenticação via cookie de sessão (extraído do navegador)
- Leitura de lista de contas a partir de um arquivo Excel (`contas_instagram.xlsx`)
- Coleta dos seguintes dados:
  - `username`
  - `full_name`
  - `bio`
  - `seguidores` (followers)
  - `seguindo` (followees)
  - `publicacoes` (posts)
  - `is_verified` (verificação da conta)
- Salvamento incremental dos dados em `coleta_temp.xlsx`, com retomada automática em caso de interrupção
- Tratamento de erros para perfis inexistentes, removidos ou com bloqueios temporários de conexão

## 📦 Requisitos

Instale os requisitos com:

```bash
pip install -r requirements.txt
🚀 Como executar
Exporte o cookie de sessão do seu navegador para que o Instaloader consiga acessar sua conta. Salve o arquivo em:

swift
Copiar
Editar
/Users/mac/.config/instaloader/session-seunomeusuario
O nome do arquivo deve coincidir com o nome de usuário utilizado na autenticação.

Edite o script Coleta_Instagram_BIO.py e ajuste:

O caminho da planilha contas_instagram.xlsx

O nome de usuário da sua conta Instagram (usuario)

Execute o script:

bash
Copiar
Editar
python Coleta_Instagram_BIO.py
O script irá salvar os dados coletados no arquivo coleta_temp.xlsx.

📝 Observações
Este script respeita os limites da plataforma do Instagram, com pausas programadas (time.sleep) para evitar bloqueios.

Perfis privados, removidos ou com restrições não serão incluídos.

O uso deste script deve seguir as políticas de uso do Instagram e destina-se exclusivamente à análise de contas públicas para fins de pesquisa.

🔒 Aviso: Certifique-se de não compartilhar publicamente cookies, senhas ou dados pessoais sensíveis.

yaml
Copiar
Editar

---

### ✅ `requirements.txt`

```txt
pandas
openpyxl
instaloader
