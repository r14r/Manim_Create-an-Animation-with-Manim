HERE := ${CURDIR}

CONTAINER := pws-kurs-manim

default:
	cat Makefile | grep -E '^.*:'

build:
	docker build -t ${CONTAINER} .

run:
	docker run  -v ${HERE}/bin:/home/user/bin  -v ${HERE}/doc:/home/user/doc -v ${HERE}/etc:/home/user/etc -v ${HERE}/src:/home/user/src -it ${CONTAINER}

readme:
	cat doc/000_start/*md doc/*.md doc/999_end/*.md >README.md

build-all:
	bin/build-all

black:
	black     main.py src

isort:
	isort     main.py src

autopep:
	autopep8  --in-place --recursive --aggressive --aggressive --aggressive	main.py src

flake:
	flake8    main.py src

pylint:
	pylint --load-plugins pylint_flask	  	main.py src

mypy:
	mypy      								main.py src

lint: isort autopep black
	echo Linting
