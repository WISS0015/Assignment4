# Dockerfile, Image, Container
FROM python:3.9

ADD main.py .

RUN pip install requests beautifulsoup4

CMD ["python", "./m-ain.py"]