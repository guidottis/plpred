setup:
	conda env create --file environment.yml || conda env update --file environment.yml

run_exploratory_data_analysis:
	cd notebooks && ipython 'exploratory_data_analysis.ipynb' \
	&& jupyter nbconvet -- to html 'exploratory_data_analysis.ipynb'

preprocessing:
	plpred-preprocess -m data/raw/membrane.fasta \
	-c data/raw/cytoplasm.fasta \
	-o data/processed/processed.csv

training:
		plpred-train -p data/processed/processed.csv \
		-o data/models/models.pickle \
		-r 

server: 
	plpred-server --host 0.0.0.0 --port 8000 --model data/models/model.pickle

test:
	python -m pytest

