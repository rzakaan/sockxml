PROJECT="sockxml"

ifeq (3.81, $(firstword $(sort $(MAKE_VERSION) 3.81)))
    # stuff that requires make-3.81 or higher
	.DEFAULT_GOAL := build
else
	.PHONY: build 
endif

# Directories
DIST_DIR="dist"
BUILD_DIR="build"
TEST_DIR="__test__"

# Applications
PY="python3"
PIP="pip3"

# Parameters
REQ="requirements.dev.txt"
LINT_IGNORE="E501,W293"

clean:
	rm -rf ${DIST_DIR}
	rm -rf ${BUILD_DIR}
	rm -rf __pycache__
	rm -rf *.pyc
	rm -rf *.egg
	rm -rf *.egg-info
	find . -name "__pycache__" -exec rm -rf {} \;

install:
	${PIP} install -r ${REQ}

test:
	${PY} -m unittest ${TEST_DIR}/main_test.py -v

lint:
	${PY} -m flake8 --ignore ${LINT_IGNORE} ${PROJECT}

build: clean
	${PY} setup.py sdist bdist_wheel

publish_test:
	${PY} -m twine check dist/* && ${PY} -m twine upload --repository testpypi dist/*

publish:
	${PY} -m twine upload dist/*
