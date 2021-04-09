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