DATA_DIR=$(realpath ./data)
DATA_DIR_RAW=$(DATA_DIR)/raw
DATA_DIR_PROCESSED=$(DATA_DIR)/clean
DATA_DIR_TRAINING=$(DATA_DIR)/training

FRAMEWORK_DIR=$(realpath ./docs)
DATA_DIR_OBS=$(FRAMEWORK_DIR)/data

SCRIPT_DIR=./src

TIMELINE_RESEARCHERS_TSV=$(DATA_DIR_RAW)/researchers.tsv

#####################
#                   #
#       GLOBAL      #
#                   #
#####################

clean:
	rm -rf docs/.observablehq/cache

#####################
#                   #
#        DATA       #
#                   #
#####################

.PHONY: data preprocess

data-dirs:
	mkdir -p $(DATA_DIR_CLEAN)

data: | data-dirs
	python $(SCRIPT_DIR)/import/timeline.py -i $(TIMELINE_RESEARCHERS_TSV) \
		-o $(DATA_DIR_PROCESSED)

preprocess:
	python $(SCRIPT_DIR)/preprocessing/paper.py -i $(DATA_DIR_RAW) -o $(DATA_DIR_PROCESSED)
	python $(SCRIPT_DIR)/preprocessing/author.py -i $(DATA_DIR_RAW) -o $(DATA_DIR_PROCESSED)
	python $(SCRIPT_DIR)/preprocessing/coauthor.py -i $(DATA_DIR_RAW) -o $(DATA_DIR_PROCESSED)

ksplit:
	python $(SCRIPT_DIR)/split_training.py -i $(DATA_DIR_PROCESSED) -a $(DATA_DIR_RAW) -o $(DATA_DIR_TRAINING)

switchpoint:
	python $(SCRIPT_DIR)/switchpoint.py -i $(DATA_DIR_TRAINING) -o $(DATA_DIR_PROCESSED)