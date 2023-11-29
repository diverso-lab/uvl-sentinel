ANTLR_JAR = ./antlr-4.13.1-complete.jar 

install:
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -o . uvl/UVLPython.g4
	pip install -r requirements.txt
	python setup.py build