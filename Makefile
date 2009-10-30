all: histpaint

histpaint:
	python ./histpaint.py && gnuplot histpaint.gp

movie:
	convert history_painting*.png history_painting.gif

clean:
	rm ./red.dat ./green.dat ./black.dat history_painting.eps
