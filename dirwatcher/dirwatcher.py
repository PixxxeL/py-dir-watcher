# -*- coding: utf-8 -*-
'''
Use module: https://pypi.python.org/pypi/dirsync/2.1
'''
import sys
from time import sleep
from dirsync import sync
import logging


def sync_one(src, dst):
    logger = logging.getLogger('dir-syncer')
    logger.addHandler( logging.NullHandler() )
    while True:
        sync(src, dst, 'sync', purge=True, logger=logger)
        sleep(1)

def main():
    sync_one(sys.args[1], sys.args[2])

if __name__ == '__main__':
    main()
