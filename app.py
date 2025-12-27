from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=VHTPF79;"
    "DATABASE=PXK20250612;"
    "UID=sa;"
    "PWD=12345678"
)

@app.route("/getdata")
def get_data():
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("SELECT TOP 10 * FROM SanPham")
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append({
            "MaSP": row[0],
            "TenSP": row[1],
            "SoLuong": row[2]
        })

    conn.close()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
