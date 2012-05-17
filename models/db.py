import sqlite3
import os
import functools    
class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned 
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

class DB(object):
    db_file = "data.sql"
    def __init__(self,data_file=None):
        #super(object,self).__init__()
        if not data_file:data_file = self.db_file
        self.db_file = data_file
        if not os.path.exists(data_file):
            self.initDB(data_file)
        print "initialized Database!"
        self.connection = sqlite3.Connection(data_file)
        
    def initDB(self,fname):
        conn = sqlite3.Connection(fname)
        qry = open('schema.sql',"r").read()
        conn.executescript(qry)
        conn.close()
    def query(self,qry,parts=[]):
        cur = self.connection.cursor()
        cur.execute(qry,parts)
        if qry.startswith("SELECT"):
            return cur.fetchall()
    @memoized
    def questionMarks(self,ct):
        return ",".join(["?" for i in range(ct)])
    @memoized
    def sqlColStr(self,cols):
        return ",".join(["'%s'"%c for c in cols])
    def Insert(self,table,cols,vals):
        qry = "INSERT INTO %s (%s) VALUES (%s)"%(table,self.sqlColStr(cols),
                                               self.questionMarks(len(vals)))
        
        self.query(qry, vals)
    def InsertFromDict(self,table,insertDict):
        keys = insertDict.keys()
        vals = [insertDict[k] for k in keys]
        return self.Insert(table, keys, vals)
    
    def Update(self,table,cols,vals,where):
        qry = "UPDATE %s (%s) VALUES (%s) %s"%(table,self.sqlColStr(cols),
                                               self.questionMarks(vals),where)
        self.query(qry, vals)
    
    def UpdateFromDict(self,table,key,updateDict):
        keys =updateDict.keys()
        vals = [updateDict[k] for k in keys]
        where = "WHERE %s=%s"%(key,updateDict[key])
        self.Update(table, keys, vals, where)
    @memoized            
    def colNamesAndTypes(self,table):
        #print self.connection
        cursor = self.connection.cursor()
        cursor.execute("PRAGMA table_info(%s)"%table)
        return cursor.fetchall()
    def selectCols(self,cols,table,where=''):
        qry = "SELECT %s FROM %s %s"%(",".join(cols),table,where)
        result = self.query(qry)
        rtn = []
        for row in result:
            print row
            r = {}
            for i in range(len(cols)):
                r[cols[i]]=row[i]
            rtn.append(r)
        return rtn
    @memoized
    def whereFromDict(self,whereDict):
        if not whereDict:return ''
        s = "WHERE "
        s1 = []
        for k in whereDict:
            
            s1.append("`%s`='%s' "%(k,whereDict[k]))
        s+="AND ".join(s1)
        return s
    def commit(self):
        self.connection.commit( )
        
    def select(self,table,**where):
        cnt = self.colNamesAndTypes(table)
        colNames = [i[1] for i in cnt]
        where = self.whereFromDict(where)
        #print "Where:",where
        return self.selectCols(colNames, table,where)

class Model:
    table_name = None
    def __init__(self,db):
        #super(object,self).__init__()
        assert self.table_name,"Error You Must subclass Model with a tabel_name field!"
        self.db = db
        self.pk = self.findPK()
    @memoized
    def findPK(self):
        try:return [c[1] for c in self.db.colNamesAndTypes(self.table_name) if c[5]==1][0]
        except:return None
       
    def get(self,*args,**wherecond):
        if not wherecond and len(args) == 1:
            pk = {self.pk:args[0]}
            return self.get(**pk)
        return self.db.select(self.table_name,**wherecond)
        
    def add(self,**kwargs):
        self.db.InsertFromDict(self.table_name, kwargs)
        self.db.commit()
class Race(Model):
    table_name="races"
    
class Racer(Model):
    table_name="racers"
    def __init__(self,db,pk):
        Model.__init__(self,db)
        self.id = pk
        self.__getData__()
    
        
    def __getData__(self):
        pk = {self.findPK():self.id}
        self.data = self.db.select('racers',**pk)[0]
    def getRaces(self):
        rids = self.db.selectCols(['UNIQUE(race_id)'],'heats_racers',racer_id=self.id)
        pass
    
    def getCars(self,xclass=None):
        if not xclass:
            return self.db.select('cars',owner=self.id)
        else:
            return self.db.select('cars',owner=self.id,xclass=xclass)
        
    def addCar(self,name,xclass):
        self.db.InsertFromDict('cars',{"owner":self.id,"name":name,"xclass":xclass})
        self.db.commit()
        
if __name__ == "__main__":
    x = DB()
    print x.select('cars')
    r = Racer(x,1)
    r.addCar("camero","muscle")
    print r.data['name']
    print r.getCars()
    #r.add(name="joran")
    
    #print x.colNamesAndTypes('racers')
    