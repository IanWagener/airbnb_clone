import peewee
from config import *
from datetime import datetime

database = peewee.MySQLDatabase( DATABASE['database'],
                          user=DATABASE['user'],
                          charset=DATABASE['charset'],
                          host=DATABASE['host'],
                          port=DATABASE['port'],
                          passwd=DATABASE['password'] )

class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)
    created_at = peewee.DateTimeField(default=datetime.now, formats='%Y/%m/%d %H:%M:%S') 
    updated_at = peewee.DateTimeField(default=datetime.now, formats='%Y/%m/%d %H:%M:%S')



    def save(self, *args, **kwargs):
        self.updated_at = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        peewee.Model.save(self)

    class Meta:
        database = database
        order_by = ("id", )
