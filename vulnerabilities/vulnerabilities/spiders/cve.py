import scrapy
import os
from os.path import dirname

# import csv # for writing to csv
# import json  # for writing to json

import sqlite3


# download the latest CVE data locally to save time of processing
current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, "source-EXPLOIT-DB.html")


class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    start_urls = ["http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]
    # start_urls = [f"file://{url}"]

    def parse(self, response):
        # connect to the database
        connection = sqlite3.connect("vuln.db")
        table = "CREATE TABLE vulns (exploit TEXT, cve TEXT)"
        cursor = connection.cursor()
        connection.execute(table)
        connection.commit()

        for child in response.xpath("//table"):
            if len(child.xpath("tr")) > 100:
                table = child
                break
        count = 0

        # data = {}
        # json_file = open("vulnerabilities.json", "w")

        # csv_file = open("vulnerabilities.csv", "w")
        # writer = csv.writer(csv_file)
        # writer.writerow(["CVE", "Exploit-DB"])

        for row in table.xpath("//tr"):
            if count > 100:
                break
            try:
                exploit_id = row.xpath("td//text()")[0].extract()
                cve_id = row.xpath("td//text()")[2].extract()
                cursor.execute("INSERT INTO vulns VALUES (?, ?)", (exploit_id, cve_id))
                connection.commit()

                # data[exploit_id] = cve_id

                # writer.writerow([cve_id, exploit_id])
                count += 1
                # print(row.xpath("td//text()")[0].extract())
            except IndexError:
                pass
        # csv_file.close()

        # json.dump(data, json_file)
        # json_file.close()
