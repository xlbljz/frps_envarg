FROM badgv/frp
WORKDIR /app
COPY frps.ini /conf/frps.ini
EXPOSE 7000
