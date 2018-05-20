#######################################################################
##                                                                   ##
## Database Connector Class                                          ##
## @Author: Aaron Earl                                               ##
##                                                                   ##
## This will create a class for accessing and abstracting            ##
## a mysql database and running queries or uploading data.           ##
## There is also room for future functionality if needed             ##
#######################################################################

import csv, mysql.connector
from mysql.connector import errorcode
import os
import pandas as pd
import sys

class dbCommander():

    #Constructor
    def __init__(self):

        self.conn = mysql.connector.connect(host="urhost",
                                            port=3306,
                                            user="uruser",
                                            password = "urpass",
                                            db="urdb")
        self.cursor = self.conn.cursor()
    #Del method will close the connection automatically
    def __del__(self):
        self.conn.close()

    ########################################################################
    ##                            query                                   ##
    ## This method will take query data from the database and return it   ##
    ########################################################################
    def query(self, statement):

        if(statement == None or ""):
            print("In Method query: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute(statement)
            return self.cursor.fetchall()
    
    ########################################################################
    ##                       printLines                                   ##
    ## This method will take query data from the database and print it    ##
    ########################################################################
    def printLines(self, statement):
        
        if(statement == None or ""):
            print("In Method query: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute(statement)
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        
    ########################################################################
    ##                          queryLine                                 ##
    ## This method will take single line query data from the database     ## 
    ## and return it                                                      ##
    ########################################################################
    def queryLine(self, statement):
        
        if(statement == None or ""):
            print("In Method queryLine: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute(statement)
            return self.cursor.fetchone()
    
    ########################################################################
    ##                          printLine                                 ##
    ## This method will take single line query data from the database     ## 
    ## and print  it                                                      ##
    ########################################################################
    def printLine(self, statement):
        
        if(statement == None or ""):
            print("In Method queryLine: statement was null")
            self.dbHelp(self)
        else:
            self.cursor.execute(statement)
            print(self.cursor.fetchone())
    
    ########################################################################
    ##                        statementCommit                             ##
    ## This method will take a statement and run it against the database  ##
    ## with a commit statement (IE for dropping table or creating them)   ##
    ########################################################################
    def statementCommit(self, statement):
        
        if(statement == None or ""):
            print("In Method statementCommit: statement was null")
            self.dbHelp(self)
            return False
        else:
            self.cursor.execute(statement)
            self.conn.commit()
            return True
    
    ########################################################################
    ##                       statementNoCommit                            ##
    ## This method will take a statement and run it against the database  ##
    ## without commit statement (IE for Truncate or other operations with ##
    ## Implicit Commit)                                                   ##
    ########################################################################
    def statementNoCommit(self, statement):
        
        if(statement == None or ""):
            print("In Method statementNoCommit: statement was null")
            self.dbHelp(self)
            return False
        else:
            self.cursor.execute(statement)
            return True
            
    ########################################################################
    ##                          uploadOne                                 ##
    ## This method will take a single line data input and upload it to    ##
    ## the database using the execute statement                           ##
    ########################################################################
    def uploadOne(self, statement, data):
        
        if(statement == None or ""):
            print("In Method uploadOne: statement was null\n")
            self.dbHelp(self)
            return False
        elif(data == None):
            print("In Method uploadOne: data was null\n")
            self.dbHelp(self)
            return False
        else:
            self.cursor.execute(statement, data)
            self.conn.commit()
            return True
    
    ########################################################################
    ##                          uploadList                                ##
    ## This method will take a large(list) dataset and upload it to the   ##
    ## database using the executemany statment                            ##
    ########################################################################
    def uploadList(self, statement, data):
        
        if(statement == None or ""):
            print("In Method uploadMany: statement was null\n")
            self.dbHelp(self)
            return False
        elif(data == None):
            print("In Method uploadMany: data was null\n")
            self.dbHelp(self)
            return False
        elif(type(data) != list):
            print("In Method uploadMany: data was wrong datatype\n")
            self.dbHelp(self)
        else:
            self.cursor.executemany(statement, data)
            self.conn.commit()
            return True
    
    ########################################################################
    ##                          uploadDict                                ##
    ## This method will take a large(list) dataset and upload it to the   ##
    ## database using the executemany statment                            ##
    ########################################################################
    def uploadDict(self, statement, data):
        
        if(statement == None or ""):
            print("In Method uploadMany: statement was null\n")
            self.dbHelp(self)
            return False
        elif(data == None):
            print("In Method uploadMany: data was null\n")
            self.dbHelp(self)
            return False
        elif(type(data) != type(dict())):
            print("In Method uploadMany: data was wrong datatype\n")
            self.dbHelp(self)
        else:
            self.cursor.executemany(statement, data)
            self.conn.commit()
            return True
    
    ########################################################################
    ##                          writeCSV                                  ##
    ## This method will take a large dictionary dataset and turn it into  ## 
    ## a csv for storage or testing                                       ##
    ########################################################################        
    def writeCSV(self, data, fieldnames, filename, directory):
        
        if(data == None):
            print("In Method writeCSV: data was null")
            self.dbHelp(self)
            return False
        elif(type(data) != list):
            print("In Method writeCSV: data was the wrong datatype")
            self.dbHelp(self)
            return False
        elif(fieldnames == None or ""):
            print("In Method writeCSV: fieldnames were null")
            self.dbHelp(self)
            return False
        elif(filename == None or ''):
            print("In Method writeCSV: filename was null")
            self.dbHelp(self)
            return False
        elif(directory == None or ''):
            print("In Method writeCSV: directory was null")
            self.dbHelp(self)
            return False
        elif(os.path.exists(directory) == False):
            print("In Method writeCSV: directory does not exist")
            self.dbHelp(self)
            return False
        else:
            
            os.chdir(directory)
            
            with open(filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
            return True
    
    ########################################################################
    ##                          queryToCSV                                ##
    ## This method will take a large(list) dataset and turn it into a     ##
    ## csv for storage or testing                                         ##
    ########################################################################        
    def queryToCSV(self, statement, fieldnames, filename, directory):
        
        if(statement == None or ""):
            print("In Method query: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute(statement)
            data = self.cursor.fetchall()
        if(fieldnames == None or ""):
            print("In Method writeCSV: fieldnames were null")
            self.dbHelp(self)
            return False
        elif(filename == None or ''):
            print("In Method writeCSV: filename was null")
            self.dbHelp(self)
            return False
        elif(directory == None or ''):
            print("In Method writeCSV: directory was null")
            self.dbHelp(self)
            return False
        elif(os.path.exists(directory) == False):
            print("In Method writeCSV: directory does not exist")
            self.dbHelp(self)
            return False
        else:
            
            os.chdir(directory)
            
            with open(filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
            return True
    
    ########################################################################
    ##                          queryToList                               ##
    ## This method will query the database and return a list object       ##
    ########################################################################
    def queryToList(self, statement):
        
        data = []

        if(statement == None or ""):
            print("In Method query: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute(statement)
            data = self.cursor.fetchall()
            return data
    
    ########################################################################
    ##                          queryToDict                               ##
    ## This method will query the database and return a list of           ##
    ## dictionary objects                                                 ##
    ########################################################################
    def queryToDict(self, statement, columns):
        
        data = []

        if(statement == None or ""):
            print("In Method query: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute(statement)
            rows = self.cursor.fetchall()
            for row in rows:
                data.append(dict(zip(columns, row)))
            return data

    ########################################################################
    ##                         queryToDataFrame                           ##
    ## This method will query the database and return a DataFrame object  ##
    ########################################################################
    def queryToDataFrame(self, statement, columns):
        
        data = []

        if(statement == None or ""):
            print("In Method query: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute(statement)
            rows = self.cursor.fetchall()
            for row in rows:
                data.append(row)
            dOut = pd.DataFrame(data, columns=columns) #store data into a dataframe
            return dOut

    ########################################################################
    ##                         getDBPointers                              ##
    ## This method will return the connector and cursor objects from this ##
    ## class                                                              ##
    ########################################################################
    def getDBPointers(self):

        return (self.conn, self.cursor)

    ########################################################################
    ##                         getCols                                    ##
    ## This method will return a list of columns associated with a given  ##
    ## table name                                                         ##
    ########################################################################
    def getCols(self, dbName, tableName):

        cols = []

        if(tableName == None or ""):
            print("In Method getCols: statement was null")
            self.dbHelp(self)
            return None
        elif(dbName == None or ""):
            print("In Method getCols: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute("Select column_name from information_schema.columns where table_schema = " 
                                 + "'" + dbName + "'" + " and table_name = "+ "'" + tableName + "'")
            data = self.cursor.fetchall()
            for i in range(0, len(data)):
                cols.append(str(data.pop()).strip('(').strip(')').strip('\'').strip(',').strip('\''))
            return cols

    ########################################################################
    ##                         getColsAndCount                            ##
    ## This method will return a list of columns associated with a given  ##
    ## table name and the count of the columns                            ##
    ########################################################################
    def getColsAndCount(self, dbName, tableName):

        cols = []

        if(tableName == None or ""):
            print("In Method getCols: statement was null")
            self.dbHelp(self)
            return None
        elif(dbName == None or ""):
            print("In Method getCols: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute("Select column_name from information_schema.columns where table_schema = " 
                                 + "'" + dbName + "'" + " and table_name = "+ "'" + tableName + "'")
            data = self.cursor.fetchall()
            for i in range(0, len(data)):
                cols.append(str(data.pop()).strip('(').strip(')').strip('\'').strip(',').strip('\''))
            return (cols, len(cols))

    ########################################################################
    ##                         getColCount                                ##
    ## This method will return the number of columns in a given table     ##
    ########################################################################
    def getColCount(self, dbName, tableName):

        if(tableName == None or ""):
            print("In Method getCols: statement was null")
            self.dbHelp(self)
            return None
        elif(dbName == None or ""):
            print("In Method getCols: statement was null")
            self.dbHelp(self)
            return None
        else:
            self.cursor.execute("Select Count(column_name) from information_schema.columns where table_schema = "
                                 + "'" + dbName + "'" + " and table_name = "+ "'" + tableName + "'")
            cols = self.cursor.fetchOne()
            data = str(cols).strip('(').strip(')').strip('\'')
            return (data)

    ########################################################################
    ##                         getTableNames                              ##
    ## This method will return the table names of the current database    ##
    ## and return them in a list                                          ##
    ########################################################################
    def getTableNames(self):

        tables = []

        self.cursor.execute("show tables")
        data = self.cursor.fetchall()
        for i in range(0, len(data)):
            tables.append(str(data.pop()).strip('(').strip(')').strip('\'').strip(',').strip('\''))
        
        return (tables)

    ########################################################################
    ##                         getTableAndCount                           ##
    ## This method will return the table names of the current database    ##
    ## and return a list of names with a count of the tables              ##
    ########################################################################
    def getTablesAndCount(self):

        tables = []

        self.cursor.execute("show tables")
        data = self.cursor.fetchall()
        for i in range(0, len(data)):
            tables.append(str(data.pop()).strip('(').strip(')').strip('\'').strip(',').strip('\''))
        
        return (tables, len(tables))

    ########################################################################
    ##                         getTableCount                              ##
    ## This method will return the table names of the current database    ##
    ## and return them in a list                                          ##
    ########################################################################
    def getTableCount(self, dbName):

        self.cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = " + "'" + dbName + "'")
        data = self.cursor.fetchall()
        data = str(data.pop()).strip('(').strip(')').strip('\'').strip(',').strip('\'')
        
        return (data)

    ########################################################################
    ##                           dbHelp                                   ##
    ## This method will display help information                          ##
    ########################################################################
    def dbHelp(self):
        #TODO
        print("Stuff")

    ########################################################################
    ##                           dbHelp                                   ##
    ## This method will display help information for a specific method    ##
    ########################################################################
    def dbHelp(self, methodName):
        #TODO
        print("Stuff")
