
import psycopg2
import psycopg2.extras

con = psycopg2.connect(
    dbname = 'dvdrental', user = 'postgres',
    password = 'supinf123', host = 'localhost')
cur = con.cursor()

# cur.execute('CREATE TABLE student(id serial primary key, name varchar);')

# cur.execute('select * from customer;')
# result = cur.fetchone()
# print(result[0])

# getting all the table names in a data base
cur.execute("""
SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'
       """)
for table in cur.fetchall():
    print(table[0])

# con.commit()

# getting the colum names of a table
cur.execute("""
        select * from information_schema.columns
        where table_schema = 'public'
        and table_name = 'customer'
""")
cols = []
for  i in cur.fetchall():
    cols.append(i[3])
print(cols)

# getting the output as dataframe format
import pandas as pd
def astable(result):
    cols = range(len(result[0]))
    output = pd.DataFrame(columns = cols)

    for j in range(len(result)):
        output.loc[j] = result[j]
    return output


cur.execute("""
        select * from customer
        limit(5)
        """)
result = cur.fetchall()
# for i in result:
#     print(i)

for j in range(len(result)):
    df.loc[j] = result[j]

astable(result)

def astable(result,cols):
    output = pd.DataFrame(columns = cols)
    for j in range(len(result)):
        output.loc[j] = result[j]
    return output

cur.execute("""
    select actor.first_name, actor.last_name from actor
    limit(6)
    """)
astable(cur.fetchall(), cols = ['firstname', 'lastname'])


# closing the connection
cur.close()
con.close()
