from elixir import setup_all, cleanup_all, session, metadata

metadata.bind = "sqlite:///liron.sqlite"
metadata.bind.echo = True

from liron.pojos.persons import *
from liron.pojos.seminar import *

setup_all()