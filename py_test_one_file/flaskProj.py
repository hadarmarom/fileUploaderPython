from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import sqlite3
from flask_cors.core import LOG
app = Flask(__name__)
CORS(app)

con = sqlite3.connect('file.db')

# ---------------line to delete the rows------------
# cur = con.cursor()
# files = []
# for row in cur.execute("SELECT * FROM files"):
#     # print(row) # print(row[0], row[1])
#     cur.execute("DELETE FROM files WHERE name = 'fileName'")
#     currFile = {
#         'name': row[0],
#         'fileSrc': row[1]
#     }
#     files.append(currFile)
# con.commit()
# con.close()
# ---------------line to delete the rows------------

@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        con = sqlite3.connect('file.db')
        cur = con.cursor()
        if request.method == 'GET':
            files = [] 
            for row in cur.execute("SELECT * FROM files"):
                currFile = {
                    'name': row[0],
                    'fileSrc': row[1]
                }
                files.append(currFile)
            con.commit()
            return json.dumps(files)
        if request.method == 'POST':
            post_data = request.data # result in bytes
            post_data_str = post_data.decode("utf-8") # result is string
            startIndex = post_data_str.index('","fileSrc') 
            fileName = post_data_str[9:startIndex]
            updateStertIdx = startIndex+13
            fileSrc = post_data_str[updateStertIdx:-2]
            cur.execute(
                "INSERT INTO files (name, fileSrc) VALUES(?, ?)", (fileName, fileSrc))
            con.commit()
            results = {'processed': 'true'}
            return jsonify(results)
        return ("not Post not Get")
    except:
        print("except!!!")
        return ("except")

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5000, threaded=True)