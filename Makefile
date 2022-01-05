PROJECT="sockxml"
DIST="dist"
BUILD="build"

test:
	python -m unittest sockxml __test__/main_test.py -v

clean:
	rm -rf $DIST
	rm -rf $BUILD
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf *.egg
	rm -rf *.egg-info

build:
	python setup.py sdist bdist_wheel
	twine check dist/* && twine upload dist/*

publish:
	python -m twine upload --repository testpypi dist/*