#dicts.py

d = {"port":5432, "engine":"postgres", "host":"127.0.0.1", "odbc":"psycopg2"}

#print(d["port"], d["engine"])

print(d)

#d["engine"] = "PostgreSql"
#d["host"] = "localhost"
# d[12] = 34
# d["23"] = "abc"
# print(d)

# del d[12]
# del d["23"]

print(d.items())