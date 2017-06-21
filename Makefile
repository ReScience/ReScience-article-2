all:
	pdflatex draft.tex
	biber draft.bcf
	pdflatex draft.tex

clean:
	-rm draft.bcf draft.pdf
