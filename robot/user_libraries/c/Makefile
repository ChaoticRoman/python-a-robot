all: py3

py2: swig
	gcc -O0 -fPIC -c example.c
	gcc -O0 -fPIC -c example_wrap.c -I/usr/include/python2.7/
	gcc -shared example.o example_wrap.o -o _example.so
	python -c "import example as ex; print(ex.my_mod(6,5), ex.fact(3), ex.cvar.My_variable)"

py3: swig
	gcc -O0 -fPIC -c example.c
	gcc -O0 -fPIC -c example_wrap.c -I/usr/include/python3.6m/
	gcc -shared example.o example_wrap.o -o _example.so
	python3 -c "import example as ex; print(ex.my_mod(6,5), ex.fact(3), ex.cvar.My_variable)"

swig:
	swig -python example.i

clear:
	rm -f *.h.gch example.py *.pyc *.so *_wrap.c *.o
	rm -rf __pycache__
