![Image alt](https://github.com/Nikitatsivinsky/pictures/blob/main/rd3.png)

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=30&duration=4000&pause=1500&color=805FA6&width=500&lines=%D0%92%D1%87%D0%B8%D0%BC%D0%BE+%D0%BA%D0%BE%D0%B4%D1%83%D0%B2%D0%B0%D1%82%D0%B8+%D0%BC%D0%B0%D0%B9%D0%B1%D1%83%D1%82%D0%BD%D1%94...;%D0%92%D1%87%D0%B8%D0%BC%D0%BE+%D0%B2%D0%B5%D1%80%D1%81%D1%82%D0%B0%D1%82%D0%B8+%D0%BC%D0%B0%D0%B9%D0%B1%D1%83%D1%82%D0%BD%D1%94...;%D0%92%D1%87%D0%B8%D0%BC%D0%BE+%D1%82%D0%B5%D1%81%D1%82%D1%83%D0%B2%D0%B0%D1%82%D0%B8+%D0%BC%D0%B0%D0%B9%D0%B1%D1%83%D1%82%D0%BD%D1%94...)](https://git.io/typing-svg)

Pet-project Telegram Bot for Shop
===============================================

### Written by: Nikita Tsivinsky ![](https://komarev.com/ghpvc/?username=Nikitatsivinsky)
### Github: https://github.com/Nikitatsivinsky/
### Contributors & Mentors: @klymenok and @acman
# Description
#### This is the Pet-Project Telegram Bot Repository of the "Python Developer" course from robot_dream, student Nikita Tsivinsky.
[![](https://github.com/AngelOfDeath-UA/angelofdeath-ua.github.io/blob/main/img/button_doc.png)](https://angelofdeath-ua.github.io/)                       [![](https://raw.githubusercontent.com/AngelOfDeath-UA/angelofdeath-ua.github.io/main/img/button.png)](https://t.me/nike_shop_delivery_bot)

# Installation:
#### Follow the steps below to get started your tests of Telegram Bot:
1. <b>Create you own environment file.</b> <br>
You need to create your environment variables. In file .env.template you can see example of your .env file:
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
2. <b>Install server Postgres</b> <br>
* For Linux:
```bash
sudo apt update                           
sudo apt upgrade
sudo apt install postgresql
```
to check your server use:
```bash
sudo service postgresql status 
```
* For Mac:
1. <code>[Visit the PostgreSQL downloads page](https://www.postgresql.org/download/macosx/)</code>
2. Download and open the downloaded package (.dmg) file.
3. Follow the on-screen instructions to run the installer and complete the installation process.
to check your server use:
```bash
psql --version  
```
* For Windows::
1. <code>[Visit the PostgreSQL downloads page](https://www.postgresql.org/download/windows/)</code>
2. Download and open the downloaded installer (.exe) file.
3. Follow the on-screen instructions to run the installer and complete the installation process. Make sure to remember the password you set for the "postgres" user during the installation.
to check your server use:
```bash
psql --version  
```

<div align="center"><b>⚠️ You can use Docker container instead installing Postgresql on your OS.⚠️<b></div>
<br>
  
3. <b>Set up server Postgres</b><br>
1. Open a command prompt or terminal and log in as a user with superuser privileges (such as a root user or a user with sudo privileges). <br>
  Run the psql command to enter an interactive Postgres shell:
 ```bash
 sudo -u postgres psql
 ```
  
 * Create a new table named tgbot:
 ```bash
 CREATE DATABASE tgbot;
 ```
    
 * Create a new user with the CREATE USER command:
 ```bash
 CREATE USER "user" WITH PASSWORD "user";
 ```
  
 * Assign the required privileges to the user. For example, to give it full rights to all databases, you can run the following command:
 ```bash
 GRANT ALL PRIVILEGES ON DATABASE tgbot TO "user";
 ```
  
 * Connect to the tgbot database:
 ```bash
 \c tgbot
 ```
  
 * Activate the uuid-ossp extension with the following command:
 ```bash
 CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
 ```
  
 * Exit the interactive Postgres shell by typing \q or pressing Ctrl+D.
 ```bash
 \q
 ```
4. <b>Add test values in the database (possible via PyCharm or DataGrid)</b><br>
Connect via: ```bash postgresql://user:user@localhost:5432/tgbot ```
  1. Add the user entity to the profile table (leave telegram_id empty, it will be filled in automatically)
specify the phone number that will connect to the Telegram bot.
  2. Add to the order table an order with a real TTN of Nova Poshta for tests.

5. <b>Install NGROK</b><br>
 * For all OS - on <code>[Web Site](https://ngrok.com/download)</code> - download and install NGROK.
<br>
6. <b>Create Python Virtual Environment and install requirements.txt</b> <br>
  
```python
pip install -r requirements.txt 
```
<br>
  
7. <b> Run Flask Web application</b> <br>

```bash
python run.py
```
<br>
<br>
<p align="center">
  <a href="https://nikitatsivinsky.github.io/telegram/telegrambot.html">
    <img src="https://github.com/Nikitatsivinsky/pictures/blob/main/telegram_documentation.png" alt="Image alt" />
  </a>
</p>
<br>


# My statistic:
![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Nikitatsivinsky&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Nikitatsivinsky&theme=solarized_dark)
![](http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Nikitatsivinsky&theme=solarized_dark)


