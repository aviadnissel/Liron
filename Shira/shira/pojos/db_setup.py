# -*- coding: utf-8 -*- 

# Run this class to create the DB.

from elixir import create_all

from shira.pojos.model import *

if __name__ == '__main__':
    create_all()
