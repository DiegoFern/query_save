import os
import pandas as pd
from itertools import repeat


class query_save:
    def __init__(self,freq='D'):
        self.freq=freq   
        #self.old=self.__self__
    def __call__(self,method):
        return query_save_method(method,self.freq,
                        )


class query_save_method:
    FREQ={'D':1,'W':7,'H':1/24.,'0':0}

    def __init__(self,m,freq,):
        self.freq=freq
        self.m=m
        self.query,self.con=self.m()
        import hashlib
        h = hashlib.md5()
        h.update((self.query).encode('utf-8'))
        self.md5=h.hexdigest()
        self.file = self.md5+'.json'
        self.__name__ = self.md5

    def period(self,file_):
        import time
        return time.time() - os.path.getmtime(file_) <= (self.FREQ[self.freq] * 30 * 24 * 60 * 60)

    def __call__(self,):
        print(type(self))
        if not os.path.isfile(self.file):
            P = pd.read_sql(self.query,self.con)
            P.to_json(self.file)
        return pd.read_json(self.file)

def query_rec(*methods):
    def funcion(f):
        f.md5=funcion.md5
        return f
    funcion.md5='O'.join(('O'+i.md5 for i in methods))
    return funcion

class flask_launch:
    

    def run(self):
        from flask import Flask
        app = Flask('__name__')
        ans = []
        for v,m in zip(map(getattr,repeat(self),dir(self)),dir(self)):
            try:
                print(v.md5)
            except:
                continue
            ans.append({'md5':v.md5,'name':m})
            def f():
                return str(f.v().to_json())
            f.v =v
            f.__name__ = v.md5
            app.route('/{}'.format(v.md5))(f)
        app.route('/')(lambda :str(ans))
        app.run()

