from scrapy import cmdline

cmdline.execute("scrapy crawl basic -o item.csv".split())
