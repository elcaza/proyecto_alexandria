# Resolución de capitulo
FROM debian
RUN apt-get update 
RUN apt-get install apache2 -y
# RUN rm /var/www/index.html
WORKDIR /var/www/
COPY index.html /var/www/
RUN useradd -ms /bin/bash admin
USER admin