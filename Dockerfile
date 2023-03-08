FROM snowdreamtech/frps
WORKDIR /app
CMD ["python", "main.py"]
COPY frps.ini /etc/frp/frps.ini
