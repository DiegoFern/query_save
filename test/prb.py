import pandas as pd
import sqlite3

from query_save import query_save,flask_launch,query_rec
conn = sqlite3.connect('example.db')

class R(flask_launch):

    @query_save(freq='D')
    def q():
        return 'select * from prb',conn

    @query_rec(q)
    def f(self):
        return self.q()
