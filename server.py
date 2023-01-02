from flask import Flask
server = Flask(__name__)

@server.route("/")
def index():

 return "Lavander Api Hoşgeldiniz"
 

@server.route("/haberler")
def indexx():

 return scrapheaal()

@server.route("/enyuksek")
def indexxx():

 return request(filter_start(),filter_end())


@server.route("/depremler")
def depremler():
    r = get("https://api.orhanaydogdu.com.tr/deprem/live.php?limit=100") # orhanaydogdu special thx 
    return json.loads(r.content)

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)
