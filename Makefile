DATA_DIR=$(realpath ./data)
DATA_DIR_RAW=$(DATA_DIR)/raw
DATA_DIR_CLEAN=$(DATA_DIR)/clean

FRAMEWORK_DIR=$(realpath ./docs)
DATA_DIR_OBS=$(FRAMEWORK_DIR)/data

SCRIPT_DIR=./src

TIMELINE_RESEARCHERS_PQT=$(DATA_DIR_RAW)/researchers.parquet

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

.PHONY: data

data-dirs:
	mkdir -p $(DATA_DIR_CLEAN)

data: | data-dirs
	python $(SCRIPT_DIR)/timeline_import.py -i $(TIMELINE_RESEARCHERS_PQT) \
		-o $(DATA_DIR_CLEAN)