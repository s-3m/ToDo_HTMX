FROM python:3.10
WORKDIR /ToDo_HTMX
COPY ./ ./
RUN ls
RUN pip3 install -r requarements.txt
RUN pip3 install gunicorn
COPY wait.sh .
RUN chmod +x wait.sh
