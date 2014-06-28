# -*- coding: utf-8 -*- 

# Run this class to create the DB.

from liron.models import *

if __name__ == '__main__':
    from liron.models import Base
    Base.metadata.create_all(engine)
