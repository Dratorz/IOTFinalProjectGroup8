import mysql.connector

class DB(object):
    
    #connect to the db
    def __init__(self):
        try:
            self.config_file = "db.conf"
            self.connection = mysql.connector.connect(option_files=self.config_file)
        except mysql.connector.Error as err:
            print(err)
            self.close()
            
    
    def execute_select_query(self, table_name, params=None):
        return_set = []
        cursor = self.connection.cursor(dictionary=True)
        
        if params is None:
            cursor.execute("select * from {}".format(table_name))
        else:
            where_clause = " WHERE " + " AND ".join(['`' + x + '` = %s' for x in params.keys()])
            values = list(params.values())
            sql = "SELECT * FROM {}".format(table_name) + where_clause
            
            cursor.execute(sql, values)
        
        for i in cursor:
            return_set.append(i)
            
        cursor.close()
        return return_set
    
    
    def execute_insert_query(self, schema_name, table_name, params=None):
        return_set = []
        cursor = self.connection.cursor(dictionary=True)
        
        if params is None:
            return return_set
        else:
            sql = "INSERT INTO " + schema_name + "." + table_name + "(" + ", ".join([x for x in params.keys()]) + ") " + "VALUES(" + "%s, " * (len(params.keys())-1) + "%s)"
            print(sql)
            values = list(params.values())
            
            cursor.execute(sql, values)
            self.connection.commit()
            print(cursor.rowcount, " record(s) inserted!")
            
        for i in cursor:
            return_set.append(i)
        
        cursor.close()
        return return_set
    
    
    def execute_update_query(self, schema_name, table_name, params=None):
        return_set = []
        cursor = self.connection.cursor(dictionary=True)
        
        if params is None:
            return return_set
        else:
            columns = []
            newParams = dict()
            for(key, value) in params.items():
                if key != 'where':
                    newParams[key] = value
            
            for (key, value) in newParams.items():
                columns.append(key + "=" + str(value))
            
            sql = "UPDATE " + schema_name + "." + table_name + " SET " + ", ".join([c for c in columns])
            sql += " WHERE " + params['where']
            print(sql)
            
            cursor.execute(sql)
            self.connection.commit()
            print(cursor.rowcount, " record(s) updated!")
            
        for i in cursor:
            return_set.append(i)
        
        cursor.close()
        return return_set
    
    
    def close(self):
        self.connection.close()
        
    
    
    
    
            
            
            