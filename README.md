![Image alt](https://github.com/AngelOfDeath-UA/pictures/blob/main/rd3.png)

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=30&duration=4000&pause=1500&color=805FA6&width=500&lines=%D0%92%D1%87%D0%B8%D0%BC%D0%BE+%D0%BA%D0%BE%D0%B4%D1%83%D0%B2%D0%B0%D1%82%D0%B8+%D0%BC%D0%B0%D0%B9%D0%B1%D1%83%D1%82%D0%BD%D1%94...;%D0%92%D1%87%D0%B8%D0%BC%D0%BE+%D0%B2%D0%B5%D1%80%D1%81%D1%82%D0%B0%D1%82%D0%B8+%D0%BC%D0%B0%D0%B9%D0%B1%D1%83%D1%82%D0%BD%D1%94...;%D0%92%D1%87%D0%B8%D0%BC%D0%BE+%D1%82%D0%B5%D1%81%D1%82%D1%83%D0%B2%D0%B0%D1%82%D0%B8+%D0%BC%D0%B0%D0%B9%D0%B1%D1%83%D1%82%D0%BD%D1%94...)](https://git.io/typing-svg)

Pet-project Telegram Bot for Shop
===============================================

### Written by: Nikita Tsivinsky ![](https://komarev.com/ghpvc/?username=AngelOfDeath-UA)
### Github: https://github.com/Nikitatsivinsky/
### Contributors & Mentors: @klymenok and @acman
# Description
#### This is the Pet-Project Telegram Bot Repository of the "Python Developer" course from robot_dream, student Nikita Tsivinsky.
[![](https://github.com/AngelOfDeath-UA/angelofdeath-ua.github.io/blob/main/img/button_doc.png)](https://angelofdeath-ua.github.io/)                       [![](https://raw.githubusercontent.com/AngelOfDeath-UA/angelofdeath-ua.github.io/main/img/button.png)](https://t.me/nike_shop_delivery_bot)

# Installation:
#### Follow the steps below to get started your tests of Telegram Bot:
* <b>Create your own .env file.</b> <br>
⋅⋅⋅You need to create your environment variables. In file .env.template you can see example of your .env file:
```env
#FLASK
SECRET_KEY - your secret key of Flask application.
DEBUG - Bool value of Flask application.
HOST - Address of your host of Flask application (default = 0.0.0.0)
PORT - Address of your port of Flask application (default = 8443)
#AUTO START POSTGRESQL SERVER AND NGROK WITH TELEGRAM WEBHOOK (TESTED ON UBUNTU)
AUTO_START - Bool value Auto Start Postgres Server (you need to install Server on your operating system) and NGROK (inside app.start_postgresql_ngrok.StartNGROK you can see function "register_webhook" - this function set WebHook to Telegram API)
#DATABASE
DATABASE_URI - Database Uniform Resource Identifier
SQLALCHEMY_TRACK_MODIFICATIONS - Bool variable of configuration keys for Flask application.
#POSTGRESQL SERVER AUTOSTART
USER_PASSWORD - Password of your Operational System User (inside app.start_postgresql_ngrok.StartProcess you can see function "startprocess" which start your Postgres Server from bash. So, to start Server App use "sudo", and password needs for this.)
#TELEGRAM
TG_TOKEN - Token of your Telegram Bot.
#NOVA POSHTA
NOVA_POSHTA_API_KEY - Your personal Nova Poshta Api Key (Get it!)
COMPANY_TELEPHONE - Your personal or your company telephone number for tracking parcels using Nova Poshta Api method getStatusDocuments.
```
* <b>Install and set up a server Postgres</b> <br>
⋅⋅⋅For Linux:
```bash
sudo apt update                           
sudo apt upgrade
sudo apt install postgresql
```
to check your server use:
```bash
sudo service postgresql status 
```
⋅⋅⋅For Mac:
1. Visit the PostgreSQL downloads page
2. Download and open the downloaded package (.dmg) file.
3. Follow the on-screen instructions to run the installer and complete the installation process.
to check your server use:
```bash
psql --version  
```



















# My statistic:
![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=AngelOfDeath&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=daniilshat&theme=solarized_dark)

