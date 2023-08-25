FROM nginx:1.21.6-alpine

#COPY wait.sh .
#RUN chmod +x wait.sh
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d