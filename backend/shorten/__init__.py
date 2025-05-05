import os, uuid, json, pyodbc
import azure.functions as func

# — ODBC setup (execuat o singură dată la cold-start)
host     = os.getenv("SQL_HOST")
db       = os.getenv("SQL_DB")
user     = os.getenv("SQL_USER")
pwd      = os.getenv("SQL_PASSWORD")
port     = os.getenv("SQL_PORT", "1433")

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={host},{port};DATABASE={db};UID={user};PWD={pwd}"
)
cnxn   = pyodbc.connect(conn_str, autocommit=True)
cursor = cnxn.cursor()

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        orig = data.get("url")
        if not orig:
            return func.HttpResponse("Missing url", status_code=400)

        # 1) generează cod unic
        code = uuid.uuid4().hex[:6]

        # 2) salvează în baza de date
        cursor.execute(
            "INSERT INTO UrlMap (code, originalUrl) VALUES (?, ?);",
            code, orig
        )

        # 3) construiește link-ul scurt
        base  = req.url.rstrip("/shorten")
        short = f"{base}/{code}"
        return func.HttpResponse(
            json.dumps({ "shortUrl": short }),
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(f"Error: {e}", status_code=500)
