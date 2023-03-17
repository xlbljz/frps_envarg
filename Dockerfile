FROM gogost/gost
ENTRYPOINT gost -L=socks5://:1080
EXPOSE 1080