# Time-stamp: <2017-09-04 11:01:02 cp983411>

#PANDOC_OPTS := --standalone -S --toc -t slidy -V slidy-url=../css 
PANDOC_OPTS :=  -s -S -c pandoc.css --toc

INPUT_MDS := $(wildcard *.md)

OUTPUT_HTML = $(INPUT_MDS:.md=.html)

OUTPUT_PDF = $(INPUT_MDS:.md=.pdf) 

.PHONY: all html clean pdf

all: html pdf

html: $(OUTPUT_HTML)


%.html: %.md
	pandoc $(PANDOC_OPTS) $< -o $@

pdf: $(OUTPUT_PDF)

%.pdf: %.md
	pandoc -s --toc $< -o $@

clean:
	@rm -f $(OUTPUT_HTML) $(OUTPUT_PDF)
