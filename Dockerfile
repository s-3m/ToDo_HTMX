FROM python:3.10
WORKDIR /ToDo_HTMX
#COPY ./ ./
COPY ./requarements.txt .
RUN pip install -r requarements.txt
RUN pip install gunicorn
#COPY wait.sh .
#RUN chmod +x wait.sh
