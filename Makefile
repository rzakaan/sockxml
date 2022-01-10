PROJECT="sockxml"
DIST="dist"
BUILD="build"

test:
	python -m unittest __test__/main_test.py -v

clean:
	rm -rf $DIST
	rm -rf $BUILD
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf *.egg
	rm -rf *.egg-info

build:
	python setup.py sdist bdist_wheel

test_publish:
	python -m twine check dist/* && python -m twine upload --repository testpypi dist/*

publish:
	python -m twine upload dist/*
