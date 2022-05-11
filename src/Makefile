TP=graph-cr3
AUTHOR=pather-larafi
CC      = python3
GSM     = gsm.py
MAP     = map.py
SUDOKU  = sudoku.py
MAKE    = make
ARCHIVE_FILES = exemples/* algorithms.py $(GSM) $(MAP) $(SUDOKU) output/* README.md Makefile

all: main

main:
	$(MAKE) gsm in=exemples/gsm.txt out=output/gsm_output.txt
	$(MAKE) map in=exemples/map.txt out=output/map_output.txt
	#$(MAKE) sudoku in=exemples/sudoku.txt out=output/sudoku_output.txt
	$(MAKE) sudoku
gsm:
	$(CC) $(GSM) -i ${in} -o ${out}

map:
	$(CC) $(MAP) -i ${in} -o ${out}

sudoku:
	#$(CC) $(SUDOKU) -i ${in} -o ${out}
	$(CC) $(SUDOKU) exemples/sudoku.txt > output/sudoku_output.txt

archive: dm-$(TP).zip
dm-$(TP).zip: $(ARCHIVE_FILES)
	zip $@ $(ARCHIVE_FILES)


clean:
	rm -f output/*.txt

.PHONY: all clean

