setup:
	conda env create --file environment.yml || conda env update --file environment.yml

run_exploratory_data_analysis:
	cd notebooks && ipython 'exploratory_data_analysis.ipynb' \
	&& jupyter nbconvet -- to html 'exploratory_data_analysis.ipynb'

preprocessing:
	python plpred/preprocessing.py

training:
		python plpred/training.py

test:
	python -m pytest