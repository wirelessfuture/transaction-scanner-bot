FROM python:3.9.2-slim-buster
ADD src / 
COPY src app/
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python", "main.py"]