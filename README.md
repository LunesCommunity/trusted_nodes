# Trusted_Nodes

Para auxiliar as pessoas que querem realizar seus leasings, vamos colocar uma página aqui no lunescommunity.org com os nodes Profissionais, ou seja, aqueles que realmente estão nisto para ter um retorno financeiro verdadeiro.

Para ser justo com todos, criamos os seguintes pre-requisitos para identificar aqueles que fazem disto uma profissão.

## Pré Requisitos

1) **Ter um site para seu node** – Não dá para ganhar dinheiro sem ter uma “porta de entrada” para o seu negócio.

2) o site ter **HTTPS** – Hoje, com o LetsEncrypt, não há custos para se ter um ambiente com HTTPS;

3) Ter um arquivo **address.txt** na raiz do site, com o address de sua carteira como conteúdo. Quem não tiver como colocar, por conta do seu provedor de hospedagem, deverá criar um registro TXT de DNS para seu NODE_ADDRESS:

```name IN TXT "NODE_ADDRESS=xxxxxxxxxxxxxxxx"```

4) Criação de um **Alias para sua Wallet**, contendo o seu domínio de verificação.

5) Todos podem se inscrever… Porém, para ser listado, deve estar entre os TOP 20 Profissionais em Share, nos últimos 1500 blocos. Este script rodará diariamente e atualizará a página. Iremos filtrar somente os inscritos (mesmo que algumas baleias montem seu node próprio, com zilhões de Lunes) e os mostraremos para a comunidade.

## Como isto será feito?

O Objetivo é validar o domínio do node e sua Wallet. 

Ao ler o Alias no Blockchain, iremos validar o Domínio:
* Tem arquivo address.txt? Se não tem, Tem TXT de DNS? Se, não tiver um dos dois, não será incluído.
⋅⋅⋅ Assumindo que uma das duas validações existam, verificaremos o Alias, com o endereço da wallet:
* O endereço validado é diferente do endereço do Alias? Se sim, descartado.
⋅⋅⋅ Validações concluídas, o node será incluído na lista.

Mais alguma sugestão ou comentário? Estamos numa comunidade onde todos podem opinar….

