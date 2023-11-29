install:
	@echo "Checking for ANTLR..."
	@command -v antlr4 >/dev/null 2>&1 || { echo >&2 "ANTLR is not installed. Please install ANTLR and ensure it's in your PATH."; exit 1; }
	pip install -r requirements.txt
	antlr4 -Dlanguage=Python3 -o python uvl/UVLPython.g4
	cp README.md python
	cd python && python setup.py build
