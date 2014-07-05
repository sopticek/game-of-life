test:
	@nosetests tests

test-coverage:
	@nosetests --with-coverage --cover-package life \
		--cover-erase --cover-html --cover-html-dir coverage tests
