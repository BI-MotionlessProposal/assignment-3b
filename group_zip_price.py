import csv
import glob, os
import pandas as p

def avg(l):
    if(len(l)<=0):
        return "not enough data"
    else:
        return sum(l, 0.0) / len(l)


def avgPerDates(file):
    rivers = {}
    sell_date1 = "1992"
    sell_date2 = "2016"
    rivers[sell_date1] = []

    rivers[sell_date2] = []
    with open(file, mode='rU') as f:
        reader = csv.reader(f, delimiter=',')  # dialect=csv.excel_tab?
        for n, row in enumerate(reader):
            if not n:
                # Skip header row (n = 0).
                continue
            if (sell_date1 in row[3]):
                price = row[2]
                price = int(str(price).replace(".", "").replace("-", ""))
                zip_code = row[1]
                sq = row[8]
                tuple = ((row[1], row[8]))
                if ("-" in str(sq)):
                    sq = 0
                if (sq != 0):
                    pr_sq = price / int(sq)
                    if (tuple not in rivers[sell_date1]):
                        rivers[sell_date1].append(pr_sq)
            if (sell_date2 in row[3]): #find dates for 2016
                price = row[2]
                price = int(str(price).replace(".", "").replace("-", ""))
                zip_code = row[1]
                sq = row[8]
                tuple = ((row[1], row[8]))
                if ("-" in str(sq)):
                    sq = 0
                if (sq != 0):
                    pr_sq = price / int(sq)
                    if (tuple not in rivers[sell_date2]):
                        rivers[sell_date2].append(pr_sq)
    #print("average price for",os.path.basename(file).split(".")[0]," 1992 : " ,avg(rivers["1992"]),' , '," 2016 : ", avg(rivers["2016"]))
    _1 = (avg(rivers["1992"]))
    _2 = (avg(rivers["2016"]))
    name =os.path.basename(file).split(".")[0]
    val = ({"zipcode":name},{"1992":_1},{"2016":_2})
    return  val


#avgPerDates('boliga_all.csv');
all_avg=[]
for file in os.listdir("./data"):

    if file.endswith(".csv"):
        all_avg.append(avgPerDates(os.path.join("./data", file)))
all_avg=p.DataFrame(all_avg)
print(all_avg.T)

