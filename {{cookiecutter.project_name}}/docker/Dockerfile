FROM eqseqs/dl-work:latest
MAINTAINER Satoshi Murashige

RUN pip install chainer chainercv
RUN conda install -c pytorch pytorch==1.2.* torchvision==0.4.*
RUN pip install test_tube
RUN pip install optuna

WORKDIR /work
CMD ["/bin/bash"]

