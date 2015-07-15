.PHONY: test clean

test:
        ./test/testConvert.py

clean:
        find . -type f -name \*.pyc -delete
        find . -type f -name \*.pyo -delete