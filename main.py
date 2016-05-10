
from d.mysql import MySQLDatabase
from settings import db_config

db = MySQLDatabase(db_config.get('db_name'),
             db_config.get('user'),
             db_config.get('pass'),
             db_config.get('host'))


tables = db.get_available_tables()
print tables

columns_p = db.get_columns_for_table('profiles')
print 'profiles columns: ', columns_p

columns_o = db.get_columns_for_table('orders')
print 'orders columns: ', columns_o

columns_a = db.get_columns_for_table('articles')
print 'articles columns: ', columns_a

