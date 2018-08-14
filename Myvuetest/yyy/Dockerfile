FROM centos:7

ENV PYTHON_VERSION=3.6.1
ENV PYTHON_HOME=/root/Python-$PYTHON_VERSION

RUN mkdir /root/Python-3.6.1

RUN echo "root:password" | chpasswd

RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf \
 && echo "nameserver 8.8.4.4" >> /etc/resolv.conf \
 && echo "search localdomain" >> /etc/resolv.conf \
 && yum install -y gcc \
 && yum install -y zlib-devel \
 && yum install -y make \
 && yum install openssl-devel -y \
 && yum install sqlite-devel -y \
 && yum install unzip \
 && rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm \
 && yum install nginx

COPY libs/sqlite-autoconf-3081101.tar.gz /root/

RUN cd /root/ \
 && tar zxvf /root/sqlite-autoconf-3081101.tar.gz \
 && cd sqlite-autoconf-3081101 \
 && ./configure \
 && make && make install


COPY libs/Python-3.6.1.tgz /root/

RUN tar xf /root/Python-3.6.1.tgz --strip-components 1 -C /root/Python-3.6.1 \
 && cd /root/Python-3.6.1 \
 && ./configure -prefix=/usr/local -with-shared-without-debug --with-ssl \
 && make && make install \
 && rm -f /root/Python-3.6.1.tgz \
 && rm -rf /root/Python-3.6.1
RUN pip3 install reload json hashlib django

COPY yyy.zip /root/
RUN cd /root/ \
    && unzip yyy.zip
#ENTRYPOINT [ "sh", "-c", "python3 /root/web/manage.py runserver 0.0.0.0:8000" ]

COPY web_nginx.conf /etc/nginx/conf.d/web_nginx.conf
CMD service nginx start

EXPOSE 22
EXPOSE 8000