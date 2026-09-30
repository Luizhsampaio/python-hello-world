# Python Hello World

Exemplo simples de dois servidores HTTP executados simultaneamente com Python.
O projeto usa apenas módulos da biblioteca padrão, sem dependências externas.

## Servidores

Cada servidor possui uma porta e uma resposta diferentes:

| Servidor | Endereço | Resposta |
| --- | --- | --- |
| Servidor 1 | http://localhost:8001 | Hello World 1 |
| Servidor 2 | http://localhost:8002 | Hello World 2 |

Os servidores são executados em threads dedicadas. A thread principal permanece
ativa aguardando o encerramento do programa.

## Como executar

É necessário ter o Python instalado. No terminal, execute:

```bash
python main.py
```

Depois, abra os endereços dos servidores no navegador.

## Como parar

No mesmo terminal em que o programa está rodando, pressione `Ctrl+C`. Os dois
servidores serão encerrados de forma controlada.

Fechar o terminal também encerra o processo Python e, consequentemente, os
servidores.
