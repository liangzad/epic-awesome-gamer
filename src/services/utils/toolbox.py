# -*- coding: utf-8 -*-
# Time       : 2022/1/16 0:27
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import sys
from typing import List, Union, Dict

from loguru import logger


class ToolBox:
    """可移植的工具箱"""

    @staticmethod
    def transfer_cookies(
        api_cookies: Union[List[Dict[str, str]], str]
    ) -> Union[str, List[Dict[str, str]]]:
        """
        ctx_cookies --> request_cookies
        request_cookies --> ctx_cookies

        :param api_cookies: api.get_cookies() or cookie_body
        :return:
        """
        if isinstance(api_cookies, str):
            return [
                {"name": i.split("=")[0], "value": i.split("=")[1]} for i in api_cookies.split("; ")
            ]
        return "; ".join([f"{i['name']}={i['value']}" for i in api_cookies])


def init_log(**sink_path):
    """初始化 loguru 日志信息"""
    event_logger_format = (
        "<g>{time:YYYY-MM-DD HH:mm:ss}</g> | "
        "<lvl>{level}</lvl> - "
        # "<c><u>{name}</u></c> | "
        "{message}"
    )
    logger.remove()
    logger.add(
        sink=sys.stdout, colorize=True, level="DEBUG", format=event_logger_format, diagnose=False
    )
    if sink_path.get("error"):
        logger.add(
            sink=sink_path.get("error"),
            level="ERROR",
            rotation="1 week",
            encoding="utf8",
            diagnose=False,
        )
    if sink_path.get("runtime"):
        logger.add(
            sink=sink_path.get("runtime"),
            level="DEBUG",
            rotation="20 MB",
            retention="20 days",
            encoding="utf8",
            diagnose=False,
        )
    return logger