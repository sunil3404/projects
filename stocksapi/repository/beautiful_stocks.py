from bs4 import BeautifulSoup as bs
from matplotlib.pyplot import table
import requests
import json, uuid

class Economic_Times:
    def __init__(self, url: str) -> None:
        self.url = url

def _get_stock_title(soup_obj):
    return soup_obj.find("title").get_text()

def _get_names(name_detail):
    name = name_detail.find("span", class_="name").get_text().strip()
    if "/" in name:
        return name.replace(" / ", "/").lower()
    else:
        return "_".join(name.split(" ")).lower()

def _get_values(value_details):
    values = value_details.find("span", class_="nowrap").get_text().strip()
    values = values.replace("\n", "").replace(" ", "")
    return values

def _get_stock_details(soup_obj):
    stocks = {}
    stock_detail = soup_obj.find("div", class_="company-ratios").find_all("li")
    for each in stock_detail:
        name = _get_names(each)
        value = _get_values(each)
        stocks[name] = value
    return stocks

def _get_analysis(comments):
    content = []
    for comment in comments:
        content.append(comment.get_text())
    return content
    
def _get_stock_analysis(soup_obj):
    analysis = {}
    pros = soup_obj.find("div", class_="pros").find_all("li")
    cons = soup_obj.find("div", class_="cons").find_all("li")
    analysis["pros"] = _get_analysis(pros)
    analysis["cons"] = _get_analysis(cons) 
    return analysis

def _get_peer_comparison(soup_obj):
    comparison = soup_obj.find("table", class_="data-table text-nowrap striped").find("tbody")
    table_headers = comparison.find_all("tr")
    for header in table_headers:
        pass

'''
Get stock details of all the tables
'''
def _get_table_results(soup_obj, table_name):
    theaders = soup_obj.find("section", id=f"{table_name}").find("table", class_="data-table").find("thead").find_all("th")[1:]
    values = soup_obj.find("section", id=f"{table_name}").find("table", class_="data-table").find("tbody").find_all("tr")[:11]
    quarter_results = {}
    try:
        for item in theaders:
            for value in values:
                if item not in quarter_results.keys():
                    item = item.get_text().strip()
                    quarter_results[item] = {}
                row_name = value.find("td").get_text().strip()
                row_value = [each.get_text() for each in value.find("td").find_next_siblings()]
                quarter_results[item][row_name] = row_value
        return quarter_results
    except AttributeError as ae:
        print(item, ae)
                  
def raw_content(url : str):
    response = requests.get(url)
    soup = bs(response.content, "html.parser")
    return soup

def get_content(soup : str, company_id: int):
    stock_response = {}
    try:
        # stock_response['stock_uuid'] = uuid.uuid4()
        stock_response['company_id'] = company_id
        stock_response['stock_title'] = _get_stock_title(soup)
        stock_response['stock_details'] = _get_stock_details(soup)
        stock_response['analysis'] = _get_stock_analysis(soup)
        # stock_response['peer_comparison'] = _get_table_results(soup, "peers")
        # stock_response['quaterly_results'] = _get_table_results(soup, "quarters")
        # stock_response['profit_loss'] = _get_table_results(soup, "profit-loss")
        # stock_response['balance_sheet'] = _get_table_results(soup, "balance-sheet")
        # stock_response['cash_flows'] = _get_table_results(soup, "cash-flow")
        # stock_response['ratios'] = _get_table_results(soup, "ratios")
        # stock_response['shareholding'] = _get_table_results(soup, "shareholding")
        return stock_response
    except Exception as ex:
        print(ex)