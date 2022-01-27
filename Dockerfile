FROM python:3.10.2-bullseye

MAINTAINER jonas.eichwald@velux.com

COPY . /python-test-calculator

WORKDIR /python-test-calculator

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

RUN ["pytest", "-v", "--junitxml=reports/result.xml"]

CMD tail -f /dev/null