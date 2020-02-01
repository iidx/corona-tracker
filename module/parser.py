#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
from datetime import datetime
import requests
import config as conf


class CoronaTracker:
    data = ""

    def __init__(self):
        self.statistic = {}
        self.countries = {}

    def get_all_statistics(self):
        return self.statistic

    def get_country_statistics(self):
        return self.countries

    def parse(self):
        self.data = self._request_base_data()
        self._parser()

    def _parser(self):
        self.statistic = self._parse_statistics()
        if not self.data:
            return
        for re_str in [conf.china_regex, conf.global_regex]:
            china_flag = False
            if re_str == conf.china_regex:
                china_flag = True
            json_data = self._parse_json_from_data(re_str)
            if json_data is None:
                continue
            self._map_country_object(json_data, china_flag)

    def _parse_statistics(self):
        data = self._parse_json_from_data(conf.statistic_regex)
        dt_string = datetime.fromtimestamp(data["modifyTime"] / 1000)
        dt_string = dt_string.strftime("%Y-%m-%d %H:%M:%S")
        statistic = {
            "updated_at": dt_string,
            "confirmed": data["confirmedCount"],
            "suspected": data["suspectedCount"],
            "cured": data["curedCount"],
            "dead": data["deadCount"],
        }
        return statistic

    def _request_base_data(self):
        try:
            data = requests.get(conf.parse_url).text
        except:
            return None
        return data

    def _parse_json_from_data(self, parse_regex):
        try:
            parsed = re.search(parse_regex, self.data).group(1)
        except:
            return None
        return json.loads(parsed)

    def _get_country_name(self, chinese, china_flag):
        country = chinese.encode(conf.chinese_encode)
        if not isinstance(country, str):
            country = country.decode("utf-8")
        try:
            if china_flag:
                mapped_name = conf.nocn_country_map[country]
            else:
                mapped_name = conf.country_map[country]
        except:
            if china_flag:
                mapped_name = "China"
            else:
                mapped_name = "Other Countries"
        return mapped_name

    def _map_country_object(self, json_data, china_flag):
        for _json in json_data:
            country_obj = {
                "confirmed": _json["confirmedCount"],
                "suspected": _json["suspectedCount"],
                "cured": _json["curedCount"],
                "dead": _json["deadCount"],
            }
            country_name = self._get_country_name(
                chinese=_json["provinceName"], china_flag=china_flag
            )

            if not country_name in self.countries.keys():
                self.countries[country_name] = country_obj
            else:
                origin = self.countries[country_name]
                for key in origin.keys():
                    origin[key] += country_obj[key]
