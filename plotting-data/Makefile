filename=plotting-data

pdf:
	jupyter nbconvert --to=latex --template=../cheme.tplx ${filename}.ipynb
	pdflatex ${filename}.tex
	pdflatex ${filename}.tex
	pdflatex ${filename}.tex
	rm -f ${filename}.{tex,ps,log,aux,out,dvi,bbl,blg}

clean:
	rm -f ${filename}.{ps,pdf,log,aux,out,dvi,bbl,blg}
