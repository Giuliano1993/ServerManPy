#!/bin/bash

# Update and upgrade the system
sudo apt-get update -y
sudo apt-get upgrade -y

# Install necessary packages
sudo apt-get install -y nginx mysql-server php7.4 php7.4-fpm php7.4-mysql php7.4-xml php7.4-curl php7.4-zip php7.4-gd php7.4-mbstring

# Configure Nginx
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default
sudo touch /etc/nginx/sites-available/laravel
sudo ln -s /etc/nginx/sites-available/laravel /etc/nginx/sites-enabled/
sudo chmod -R 777 /var/www/html
sudo chown -R www-data:www-data /var/www/html

# Configure PHP
sudo sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 20M/g' /etc/php/7.4/fpm/php.ini
sudo sed -i 's/post_max_size = 8M/post_max_size = 20M/g' /etc/php/7.4/fpm/php.ini

# Configure MySQL
sudo mysql_secure_installation

# Install Composer
curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer

# Install Laravel
composer global require "laravel/installer"
export PATH=$PATH:~/.composer/vendor/bin/
