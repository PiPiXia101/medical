import requests
from lxml import etree

cookies = {
    'ezproxy': 'BIRvL1ZM2632StN',
    '__utmc': '110063619',
    '_sdsat_MCID': '',
    'seen-cookie-message': 'yes',
    '__utma': '110063619.1138259926.1567673439.1567673439.1567732888.2',
    '__utmz': '110063619.1567732888.2.2.utmcsr=2447.net|utmccn=(referral)|utmcmd=referral|utmcct=/e/action/ShowInfo.php',
    '__utmt_6fc43dded90f3ff84bd3f7e59f616f6e': '1',
    '__utmt_9d8d89c5f608a8fcab351a62719dc606': '1',
    '__utmb': '110063619.4.10.1567732888',
    'LFR_SESSION_STATE_20159': '1567732913122',
    '__atuvc': '2%7C36',
    '__atuvs': '5d71b4b300ead8dc000',
}

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'Accept': 'text/html, */*; q=0.01',
    'Referer': 'https://www-cochranelibrary-com.rpa.skh.org.tw/cdsr/reviews',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}
for i in range(1,10):
    params = (
        ('p_l_id', '20759'),
        ('p_p_id', ['scolarissearchresultsportlet_WAR_scolarissearchresults',
                    'scolarissearchresultsportlet_WAR_scolarissearchresults']),
        ('p_p_lifecycle', ['0', '0']),
        ('p_t_lifecycle', '0'),
        ('p_p_state', ['normal', 'normal']),
        ('p_p_mode', ['view', 'view']),
        ('p_p_col_id', ['column-1', 'column-1']),
        ('p_p_col_pos', '0'),
        ('p_p_col_count', ['1', '1']),
        ('p_p_isolated', '1'),
        ('currentURL', '%2Fweb%2Fcochrane%2Fsearch'),
        ('min_year', ''),
        ('max_year', ''),
        ('custom_min_year', ''),
        ('custom_max_year', ''),
        ('searchBy', '6'),
        ('searchText', '*'),
        ('selectedType', 'review'),
        ('isWordVariations', ''),
        ('resultPerPage', '25'),
        ('searchType', 'basic'),
        ('orderBy', 'relevancy'),
        ('publishDateTo', ''),
        ('publishDateFrom', ''),
        ('publishYearTo', ''),
        ('publishYearFrom', ''),
        ('displayText', ''),
        ('forceTypeSelection', 'true'),
        ('cur', str(i)),
        ('pathname', '%2Fcdsr%2Freviews'),
    )

    response = requests.get('https://www-cochranelibrary-com.rpa.skh.org.tw/en/c/portal/render_portlet', headers=headers,params=params, cookies=cookies, verify=False)
    html = response.text
    parse_html = etree.HTML(html)
    tz_list = parse_html.xpath("//div[@class='search-results-item']")
    for tz in tz_list:
        num = tz.xpath("./div[@class='search-results-item-tools']/div/label/text()")
        title = tz.xpath("./div[@class='search-results-item-body']/h3[@class='result-title']/a/text()")
        content = tz.xpath(
            "./div[@class='search-results-item-body']/div[@class='search-result-authors']/div/text()")
        print(num, title, '\n')
