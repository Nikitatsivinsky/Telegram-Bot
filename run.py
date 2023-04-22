import os
from tg_bot import app
from tg_bot.app.start_postgresql_ngrok import StartPostgresqlServer, StartNGROK

if __name__ == '__main__':
    # start PostgreSQL server on ubuntu
    StartPostgresqlServer(os.getenv('USER_PASSWORD'))
    # start ngrok on ubuntu
    StartNGROK(port=os.getenv('PORT'), tg_token=os.getenv('TG_TOKEN'))

    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'),
            debug=app.config.get('DEBUG'),
            use_reloader=False)

