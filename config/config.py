#!/usr/bin/env python
#-*- coding: utf-8 -*-

parse_url = "https://3g.dxy.cn/newh5/view/pneumonia"

statistic_regex = r"window\.getStatisticsService = (.+?)\}catch\(e\)\{\}"
global_regex = r"window\.getListByCountryTypeService2 \= (.+?)\}catch\(e\)\{\}"
china_regex = r"window\.getAreaStat \= (.+?)\}catch\(e\)\{\}"

chinese_encode = "ISO-8859-1"

nocn_country_map = {
    "香港": "Hong Kong",
    "台湾": "Taiwan",
}

country_map = {
    "泰国": "Thailand",
    "日本": "Japan",
    "新加坡": "Singapore",
    "韩国": "South Korea",
    "澳大利亚": "Australia",
    "马来西亚": "Malaysia",
    "美国": "US",
    "法国": "France",
    "德国": "Germany",
    "阿联酋": "Arab Emirates",
    "加拿大": "Canada",
    "越南": "Vietnam",
    "意大利": "Italy",
    "英国": "UK",
    "俄罗斯": "Russia",
    "芬兰": "Finland",
    "西班牙": "Spain",
    "瑞典": "Sweden",
    "印度": "India",
    "斯里兰卡": "Sri Lanka",
    "柬埔寨": "Cambodia",
    "尼泊尔": "Nepal",
}
