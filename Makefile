all:
	pandoc -t beamer --variable fontsize=10pt -V theme=Darmstadt  presentation.md  -o output.pdf

presentation.pdf: presentation.tex
	pdflatex -shell-escape presentation.tex
