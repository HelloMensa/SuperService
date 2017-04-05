#!/usr/bin/env python
# -*- coding: utf-8 -*-


def __execSql(sql)
    con = sqlite3.connect("sdata.db") 
    cur = con.cursor() 
    
    cur.execute(sql) 
    
    cur.close() 
    con.close()
