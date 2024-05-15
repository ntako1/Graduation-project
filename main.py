from read_from_arduino import read_from_arduino
from insert_into_db import insert_into_db

while True:
    data = read_from_arduino()
    if data is not None:
        insert_into_db(data)
