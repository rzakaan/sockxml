PROJECT="sockxml"
DIST="dist"
BUILD="build"
PY="python3"
PIP="pip3"
REQ="requirements.dev.txt"

clean:
	rm -rf $DIST
	rm -rf $BUILD
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf *.egg
	rm -rf *.egg-info

setup:
	${PIP} install -r ${REQ}

test:
	${PY} -m unittest __test__/main_test.py -v

pylint:


build:
	${PY} setup.py sdist bdist_wheel

test_publish:
	${PY} -m twine check dist/* && python -m twine upload --repository testpypi dist/*

publish:
	${PY} -m twine upload dist/*
