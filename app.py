# 1. Import Flask
from flask import Flask


yosimiteMonthlyAnnualVisitation = [
    {"YEAR": "2018", "JAN": "129432","FEB": "143321","MAR": "170681","APR": "278349","MAY": "385670","JUN": "543690","JUL": "504230","AUG": "441867","SEP": "524387","OCT": "360776","NOV": "215854","DEC": "311179","TOTAL": "4009436"},
    {"YEAR": "2017", "JAN": "120025","FEB": "119421","MAR": "166793","APR": "302553","MAY": "471844","JUN": "565702","JUL": "633351","AUG": "615892","SEP": "566279","OCT": "429827","NOV": "217927","DEC": "127276",,"TOTAL": "4336890"},
    {"YEAR": "2016", "JAN": "139780","FEB": "201601","MAR": "286990","APR": "305092","MAY": "457309","JUN": "703614","JUL": "780728","AUG": "692450","SEP": "598428","OCT": "483232","NOV": "218998","DEC": "160646",,"TOTAL": "5028868"},
    {"YEAR": "2015", "JAN": "128318","FEB": "135316","MAR": "194667","APR": "281328","MAY": "408121","JUN": "545231","JUL": "626009","AUG": "636936","SEP": "527402","OCT": "357223","NOV": "169425","DEC": "140241",,"TOTAL": "4150217"},
    {"YEAR": "2014", "JAN": "112133","FEB": "113403","MAR": "146750","APR": "242722","MAY": "333308","JUN": "496363","JUL": "623663","AUG": "654157","SEP": "467205","OCT": "354769","NOV": "203678","DEC": "134491",,"TOTAL": "3882642"},
    {"YEAR": "2013", "JAN": "103910","FEB": "114440","MAR": "165409","APR": "231178","MAY": "370422","JUN": "508941","JUL": "611538","AUG": "552137","SEP": "460855","OCT": "279526","NOV": "161356","DEC": "131479",,"TOTAL": "3691191"},
    {"YEAR": "2012", "JAN": "120496","FEB": "113341","MAR": "136687","APR": "243102","MAY": "356500","JUN": "528186","JUL": "623101","AUG": "660118","SEP": "482004","OCT": "322687","NOV": "141868","DEC": "125314",,"TOTAL": "3853404"},
    {"YEAR": "2011", "JAN": "100718","FEB": "93588","MAR": "100433","APR": "231372","MAY": "356588","JUN": "503741","JUL": "704553","AUG": "699749","SEP": "533502","OCT": "360449","NOV": "139079","DEC": "127621",,"TOTAL": "3951398"},
    {"YEAR": "2010", "JAN": "704553","FEB": "100379","MAR": "149651","APR": "224461","MAY": "382414","JUN": "521059","JUL": "643566","AUG": "659857","SEP": "520210","OCT": "356370","NOV": "148459","DEC": "127621",,"TOTAL": "3901408"},
    {"YEAR": "2009", "JAN": "101984","FEB": "78795","MAR": "132711","APR": "230828","MAY": "399683","JUN": "483382","JUL": "586591","AUG": "643300","SEP": "471530","OCT": "346826","NOV": "151297","DEC": "110545",,"TOTAL": "3737472"},
    {"YEAR": "2008", "JAN": "95124","FEB": "107729","MAR": "153735","APR": "199592","MAY": "361193","JUN": "473186","JUL": "539874","AUG": "543799","SEP": "416918","OCT": "295547","NOV": "146838","DEC": "97979",,"TOTAL": "3431514"},
]

# 2. Create an app
app = Flask(__name__)

# 3. Define static routes
@app.route("/")
def index():
    return "YOSIMTE 10-YEAR VISITATION DATA"


@app.route("/about")
def about():
    name = "Peleke"
    location = "Tien Shan"

    return f"My name is {name}, and I live in {location}."


@app.route("/contact")
def contact():
    email = "peleke@example.com"

    return f"Questions? Comments? Complaints? Shoot an email to {email}."


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
