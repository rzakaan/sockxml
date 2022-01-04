PROJECT="sockxml"

test:
	python -m unittest sockxml __test__/main_test.py -v
dist:
	python setup.py sdist