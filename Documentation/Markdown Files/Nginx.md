# NGINX 
NGINX is a open source software that serves webpages to clients. This means that when connecting to our app, we are connecting to NGINX. NGINX will then serve the webpage based on the route. NGINX can also act as a reverse proxy, cache, load balancer, and a streaming service. 

## Why use NGINX
NGINX allows us to act as a reverse proxy to serve our webpage. NGINX is placed in front of our application to serve the webpage. The image below shows how NGINX will be used. It will allow multiple users to use and access NGINX, which will then use NGINX to get the webpage. Credit to image: https://www.freecodecamp.org/news/an-introduction-to-nginx-for-developers-62179b6a458f/
<br>
<br>
<img src="..\user-guide-images\nignx.jpg"/>
<br><br>
## NGINX Installation
To use NGINX, we first install and run the NGINX service on our Linux System. We first install NGINX by using the command 
```sudo apt install nginx```
<br>
This will then install NGINX onto our system. To run NGINX we use the command
```sudo systemctl start nginx```
<br>
To allow NGINX to boot up everytime the system boots, we can enable with the command
```sudo systemctl enable nginx```
<br>
To stop the service and to disable the automatic start we can use the commands
```
sudo systemctl stop nginx
sudo systemctl disable nginx
```
<br>

## NGINX Configration
To use NGINX, we must modify the configuration file in the path `/etc/nginx/sites-enabled/`
To get here, we can use the command cd:
```
cd /etc/nginx/sites-enabled/
```
We will then use vim to access the file named `default`
```
sudo vim default
```
We will not be able to see the configuration file.
<br>
We only use NGINX as a reverse proxy to display and return our webpage back to the client. We do this by using a proxy pass to the correct IP and Port to where the webpage is being hosted. 
Our configuration file should look something like this:
```
location /{
    proxy_pass IP_Address:Port_Number;
}
```
This simple configuration will tell NGINX where to find the webpage, which port to access the service from, and the location or route the user will access from NGINX.

For more information on NGINX, you can visit the <a href="https://www.nginx.com/">NGINX Documentation</a>