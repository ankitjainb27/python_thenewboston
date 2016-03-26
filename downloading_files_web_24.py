from urllib import request

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=8&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"

def download_data(csv_url):
    response  = request.urlopen(csv_url)
    csv = response.read()
    csr_str = str(csv)
    # print(csr_str)
    lines = csr_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_data(goog_url)
