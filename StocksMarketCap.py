

file = open("StockMarketCaps.txt")
for lines in file:
    line_strip = lines.strip()
    line_split = lines.split(" ")
    #line_split[1] = line_split[1][0:len(line_split[1])]
    market_cap = int(line_split[1])
    if 300000000 <= market_cap < 2000000000:
        print(line_split[0] + " is a Small cap stock")
    elif 2000000000 <= market_cap < 10000000000:
        print(line_split[0] + " is a Mid cap stock")
    else:
        print(line_split[0] + " is a Large cap stock")
