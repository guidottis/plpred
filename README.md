# plpred

By Isadora leitzke Guidotti

a protein subcellular location prediction program 

## Setup

```
$ make setup
```
## Project Structure

- `environment.yml`: arquivo de confirgurção do conda, usado para definir os canais usados e as ferramentas que serão usadas pelo nosso ambiente, além de definir um outro arquivo requirements que vai definir as bibliotecas. 

- `requirements.txt`: é similar ao environment, porém exclusivo para as bibliotecas do python e ferramentas do sistema que serão usadas no projeto.

- `makefile`: usado para criar regras e encurtar comandos. 

- `Pasta Data`: contém os dados brutos e os dados armazenados. Os dados brutos ficam na pasta raw enquanto os dados processados ficam na pasta processed. 

- `Pasta Plpred`: diretório principal do pacote. Onde as funções de aplicação ficam armazenadas.

-