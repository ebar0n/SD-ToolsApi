FROM nginx:latest

COPY toolsapi.conf /etc/nginx/conf.d/default.conf

RUN sed -i 's/user  nginx;/user root;/' /etc/nginx/nginx.conf
RUN sed -i 's/\/var\/log\/nginx\/access.log  main/off/' /etc/nginx/nginx.conf
