


from flask import Flask, request,jsonify
import main
app = Flask(__name__)

@app.route('/connect_sql',methods=['POST'])
def connect_sql():
    if request.method == 'POST':
        user = request.json['user']
        password = request.json['password']
        host = request.json['host']

        input_dict = {"user":user,"password":password,"host":host}
    return input_dict

@app.route('/connect_sql/get_databases', methods = ['POST'])
def get_dbs():
    user,password,host = tuple(connect_sql().values())
    sql_connection = main.SQL_Connection(user = user,password = password, host = host)
    dbs = sql_connection.get_databases()
    return jsonify(dbs)

@app.route('/connect_sql/con_db', methods = ['POST'])
def connect_db():
    user, password,host = tuple(connect_sql().values())
    if request.method == 'POST':
        dbname = request.json['dbname']
        user = request.json['user']
        password = request.json['password']
        host = request.json['host']
        db_connection = main.DB_connection(user = user, password = password, host = host, dbname = dbname)
        output = db_connection.get_tables() 
        output_list = []
        for i in range(0,len(output)):
            output_list.append(output.iloc[i].values)
        return jsonify(output_list)
    

if __name__ == '__main__':
    app.run(debug =True)

