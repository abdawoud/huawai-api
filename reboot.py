#!/usr/bin/env python2
#
# coding: utf-8
#

from huawei_api import HuaweiAPI
import logging
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reboot the router to get a fresh IP",
                                     epilog="This tool allows to reboot the"
                                     "router to get a new IP address")
    parser.add_argument("--ip",
                        help="Router's IP",
                        required=True)
    parser.add_argument("--logfile",
                        help="Filename to save logs",
                        required=False)
    parser.add_argument("--loglevel",
                        help="loglevel",
                        required=False,
                        choices=["DEBUG", "INFO", "WARN", "ERROR"],
                        default="INFO")

    args = parser.parse_args()

    logging.getLogger().setLevel(getattr(logging, args.loglevel))
    log = logging.getLogger("lteband")
    api = HuaweiAPI(host=args.ip, user="admin", passwd="P@s$_pVe/8!",
                    logfile=args.logfile)

    api.reboot()
