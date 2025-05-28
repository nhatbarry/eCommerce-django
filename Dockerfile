FROM python

WORKDIR /app

COPY ecommerce ecommerce
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "cd ecommerce", "python3 manage.py runserver" ]

