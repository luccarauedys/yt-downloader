## Instruções para rodar no Windows

> É necessário ter o Python instalado no computador.

<br/>

1. Criar um ambiente virtual.

```
python -m venv venv
```

2. Ativar o ambiente virtual.

```
.\venv\Scripts\Activate.ps1
```

3. Instalar as libs necessárias.

```
pip install -r requirements.txt
```

4. Rodar o arquivo main.py.

```
python .\script.py
```

5. Fornecer as informações solicitadas no terminal (link do vídeo ou playlist para baixar).

<br/>

- Observação: Se der erro no passo 2, abrir o terminal do computador como administrador e rodar o comando:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
