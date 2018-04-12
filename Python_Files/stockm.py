import os
import sys


class Stock:
    def __init__(self,company,symbol,com_type,):
        self._company = company
        self._symbol = symbol
        self._com_type = com_type
    def __call__(self):
        print('Stock {}  Company Type: {}'.format(self._company,self._com_type))



def main():
    pass


if __name__ =='__stockm__':
    print(__name__)
