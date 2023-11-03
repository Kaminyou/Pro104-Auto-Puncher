FROM python:3.9
COPY . /root/app/
WORKDIR /root/app/
RUN pip install -r requirements.txt
CMD ["/bin/bash"]
