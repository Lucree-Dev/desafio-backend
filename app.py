# -*- coding: utf-8 -*-
"""
Created on Sat Aug 02 01:18:51 2021
@author: Wilson Ricardo Pereira Silveira
"""

from config import app
from config import DEBUG, HOST, PORT

import digital_account.views


if __name__ == '__main__':
    if DEBUG:
        app.run(host=HOST, port=PORT, debug=True, threaded=True, use_reloader=False)

    else:
        app.run(host=HOST, port=PORT, threaded=True, use_reloader=False)