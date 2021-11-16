FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
COPY http.js /etc/nginx/http.js
