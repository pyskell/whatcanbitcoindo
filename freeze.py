#!/usr/bin/env python3

from flask_frozen import Freezer
from app import app

app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_DESTINATION_IGNORE'] = ['CNAME']
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()