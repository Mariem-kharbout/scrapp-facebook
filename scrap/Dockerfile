FROM python:3
RUN apt-get update -y
# Coping source in current directory into the image
# python:3-onbuild expects the source in /usr/src/app
COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirement.txt
EXPOSE 8000
# Commands in a list
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]