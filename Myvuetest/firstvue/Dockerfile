#  //使用Nginx
FROM hub.c.163.com/library/nginx

# //作者
MAINTAINER wangzehua <wangzehua5739@dingtalk.com 
# //删除nginx 默认配置
RUN rm /etc/nginx/conf.d/default.conf 
# //添加我们自己的配置 default.conf 在下面
ADD default.conf /etc/nginx/conf.d/ 
# //把刚才生成dist文件夹下的文件copy到nginx下面去
COPY dist/  /usr/share/nginx/html/  