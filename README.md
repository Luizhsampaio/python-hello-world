# Python Hello World

Aplicação HTTP simples, implementada com módulos da biblioteca padrão do Python.
A versão atual inicia um servidor na porta 80 e apresenta diferentes páginas de
acordo com a rota acessada.

## Rotas

| Endereço | Resposta |
| --- | --- |
| `http://localhost/` | Página inicial com links para as páginas Hello World |
| `http://localhost/hello` | Página inicial (alias de `/`) |
| `http://localhost/1` | Hello World 1 (v1.3.0) |
| `http://localhost/hello1` | Hello World 1 (alias de `/1`) |
| `http://localhost/2` | Hello World 2 (v1.3.0) |
| `http://localhost/hello2` | Hello World 2 (alias de `/2`) |

Rotas não reconhecidas retornam o status HTTP `404`.

## Estrutura do projeto

- `main.py`: cria e inicia o servidor HTTP.
- `server_factory.py`: configura o servidor e associa o handler de roteamento.
- `hello_world_handlers.py`: implementa as respostas HTML e o roteamento.
- `.gitignore`: ignora caches, ambientes virtuais e arquivos locais do projeto.

## Como executar

É necessário ter o Python instalado. No terminal, execute:

```bash
python main.py
```

O servidor será iniciado em `http://localhost` e ficará ativo até receber uma
interrupção. A aplicação usa a porta 80, que pode já estar ocupada ou exigir
permissões elevadas dependendo do sistema. Para usar outra porta, altere o
argumento `port` na chamada a `create_server` em `main.py`.

## Como parar

Pressione `Ctrl+C` no terminal em que o servidor está rodando.
