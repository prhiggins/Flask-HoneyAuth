FROM python:3 AS build
MAINTAINER Patrick Higgins "phiggins@cs.uoregon.edu"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# pipreqs for resolving requirements, cryptography and openssl required for https service
RUN pip install pipreqs cryptography pyopenssl

FROM build
ADD . /app
WORKDIR /app

RUN pipreqs
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m"]
CMD ["unittest"]
