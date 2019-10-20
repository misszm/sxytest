# -*- coding: utf-8 -*-
# from django.db import connections, connection  # Django框架有连接方式
from psycopg2.pool import ThreadedConnectionPool 

from public_code import dbname, user, password, host, port

# for row in rows:
#
# pgpool.putconn(conn)
pgpool = ThreadedConnectionPool(1, 5, dbname=dbname, user=user, host=host, password=password, port=port)


def conn_exe(*sp):
	conn = pgpool.getconn()
	cursor = conn.cursor()
	cursor.execute(*sp)
	conn.commit()
	pgpool.putconn(conn)
	return cursor


def fetchone_sql(*sp):
	cursor = conn_exe(*sp)
	# desc = cursor.description
	fetchone = cursor.fetchone()[0]
	cursor.close()
	return fetchone


def fetchall_sql(*sp):
	cursor = conn_exe(*sp)
	fetchall = cursor.fetchall()
	cursor.close()
	return fetchall


def insert_sql(*sp):
	cursor = conn_exe(*sp)
	cursor.close()


# def fetchall_by_columns(sql, columns, db='default'):
# 	cursor = connections[db].cursor()
# 	cursor.execute(sql)
# 	object_list = [dict(zip(columns, row)) for row in cursor.fetchall()]
# 	cursor.close()
# 	return object_list
def get_black_addr():
	black_sql = "select black_email, black_level from " + "email_black"
	# black_addr = {row[0]: row[1] for row in fetchall_sql(black_sql)}
	return {row[0]: row[1] for row in fetchall_sql(black_sql)}
