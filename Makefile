BUILD_DIR = build

all: ${BUILD_DIR} MAKE_PYTHON COPY_FILES

${BUILD_DIR}:
	mkdir -p $@

MAKE_PYTHON:
	python make_html.py

COPY_FILES:
	cp global.css ${BUILD_DIR}
	cp logic.js ${BUILD_DIR}

clean:
	rm -r ${BUILD_DIR}
