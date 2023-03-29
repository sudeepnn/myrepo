FROM python:3.10.2-alpine3.15
# Create directories  
RUN mkdir -p /root/workspace/src
# Switch to project directory
COPY ./pr.py  /root/workspace/src
WORKDIR /root/workspace/src
RUN pip install --upgrade pip
RUN pip install requests
CMD ["pr.py"]
ENTRYPOINT ["python"]
