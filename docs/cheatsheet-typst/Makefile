.PHONY: all clean watch

all: cheatsheet.pdf

cheatsheet.pdf: cheatsheet.typ
	typst compile cheatsheet.typ

watch:
	typst watch cheatsheet.typ

clean:
	rm -f cheatsheet.pdf