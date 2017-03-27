# api.3g.tudou.com
upstream auth {
   server 127.0.0.1:8897 ;
   check interval=3000 rise=2 fall=3 timeout=1000 type=http;
   check_keepalive_requests 100;
   check_http_expect_alive http_2xx http_3xx;
   keepalive 50;
}

upstream zhifubao {
   server 127.0.0.1:8888 ;
   check interval=3000 rise=2 fall=3 timeout=1000 type=http;
   check_keepalive_requests 100;
   check_http_expect_alive http_2xx http_3xx;
   keepalive 50;
}

upstream wanted {
   server 127.0.0.1:8890 ;
   check interval=3000 rise=2 fall=3 timeout=1000 type=http;
   check_keepalive_requests 100;
   check_http_expect_alive http_2xx http_3xx;
   keepalive 50;
}
upstream feed {
   server 127.0.0.1:8891 ;
   check interval=3000 rise=2 fall=3 timeout=1000 type=http;
   check_keepalive_requests 100;
   check_http_expect_alive http_2xx http_3xx;
   keepalive 50;
}
upstream board {
   server 127.0.0.1:8889 ;
   check interval=3000 rise=2 fall=3 timeout=1000 type=http;
   check_keepalive_requests 100;
   check_http_expect_alive http_2xx http_3xx;
   keepalive 50;
}
upstream censor {
   server 127.0.0.1:8989 ;
   check interval=3000 rise=2 fall=3 timeout=1000 type=http;
   check_keepalive_requests 100;
   check_http_expect_alive http_2xx http_3xx;
   keepalive 50;
}

server {
    listen 8000;
    index index.html index.htm index.jsp;
    charset utf-8;

    # auth
    location ~ /auth/ {
        proxy_connect_timeout 6;
        proxy_send_timeout 6;
        proxy_read_timeout 6;

        proxy_pass http://auth;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Real-IP $x_remote_addr;
        proxy_set_header    Host $proxy_host;
        proxy_set_header    Range $http_range;
        proxy_set_header X-NginX-Proxy true;
        access_log off;
    }
    # zhifubao
    location ~ /zhifubao/ {
        proxy_connect_timeout 6;
        proxy_send_timeout 6;
        proxy_read_timeout 6;

        proxy_pass http://zhifubao;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Real-IP $x_remote_addr;
        proxy_set_header    Host $proxy_host;
        proxy_set_header    Range $http_range;
        proxy_set_header X-NginX-Proxy true;
        access_log off;
    }
    # wanted
    location ~ /wanted/ {
        proxy_connect_timeout 6;
        proxy_send_timeout 6;
        proxy_read_timeout 6;

        proxy_pass http://wanted;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Real-IP $x_remote_addr;
        proxy_set_header    Host $proxy_host;
        proxy_set_header    Range $http_range;
        proxy_set_header X-NginX-Proxy true;
        access_log off;
    }
    # feed
    location ~ /feed/ {
        proxy_connect_timeout 6;
        proxy_send_timeout 6;
        proxy_read_timeout 6;

        proxy_pass http://feed;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Real-IP $x_remote_addr;
        proxy_set_header    Host $proxy_host;
        proxy_set_header    Range $http_range;
        proxy_set_header X-NginX-Proxy true;
        access_log off;
    }
    # board
    location ~ /board/ {
        proxy_connect_timeout 6;
        proxy_send_timeout 6;
        proxy_read_timeout 6;

        proxy_pass http://board;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Real-IP $x_remote_addr;
        proxy_set_header    Host $proxy_host;
        proxy_set_header    Range $http_range;
        proxy_set_header X-NginX-Proxy true;
        access_log off;
    }
    # censor
    location ~ /censor/ {
        proxy_connect_timeout 6;
        proxy_send_timeout 6;
        proxy_read_timeout 6;

        proxy_pass http://censor;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Real-IP $x_remote_addr;
        proxy_set_header    Host $proxy_host;
        proxy_set_header    Range $http_range;
        proxy_set_header X-NginX-Proxy true;
        access_log off;
    }

}
