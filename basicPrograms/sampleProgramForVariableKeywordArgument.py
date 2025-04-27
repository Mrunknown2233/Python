def db_connect(**options):
    conn_params = {
        'host' : options.get('host','127.0.0.1'),
        'port' : options.get('port','3306'),
        'user' : options.get('user','root'),
        'password' : options.get('password','')
    }

    print(conn_params)

db_connect()
db_connect(host = 'localhost',user = 'soumya',password = 'soumya')