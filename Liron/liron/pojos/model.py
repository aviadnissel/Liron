from elixir import setup_all, session, metadata

metadata.bind = "sqlite:///shira.sqlite"
metadata.bind.echo = True

from shira.pojos.persons import *
from shira.pojos.seminar import *

setup_all()