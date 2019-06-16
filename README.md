# 

Simple library which allows to make queries which are save in an auxiliary file as cache
in the relative folder .temporary.


This is useful to trial-error reports where every query takes a lot of time.

Use:

```python
from query_save import query_save
from ddbd import connector
class Report:

    @query_save(freq='D')
    def query_1(self):
        return ('select * from prb ',connector)

```
There is a solution which allows get the reports from the http protocol, which is uesful in the context of microservices:
i
```python
import pandas as pd
import sqlite3

from query_save import query_save,flask_launch,query_rec
conn = sqlite3.connect('example.db')

class R(flask_launch):

    @query_save(freq='D')
    def qA():
        return 'select * from prb where type=A',conn

    @query_save(freq='D')
    def qB():
        return 'select * from prb where type=B',conn
    
 
    @query_rec(qA,qB)#transformation from several queries
    def q(self):
        return pd.concat(self.qA(),self.qB())

```
When is executed R().run() makes a local server where:

```python
>>>GET localhost:5000
[
{'md5':'2E3421A','function':'qA'},
{'md5':'645556','function':'qB'}
{'md5':'64D878,'function':'q'}
]
```
Where you can get the solution of the query using the hash md5 code:
```python
>>>GET localhost:5000/2E3421A
```

TODO:
Transformations (query_rec) are not able to be saved in cache, cause I wolud need a stable hash from the functions.

