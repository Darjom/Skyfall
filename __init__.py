from flask import render_template
from os.path import dirname
from sys import path

path.insert(0, dirname(__file__))

from flask import Flask

app = Flask(__name__, template_folder='_templates', static_folder='assets')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Import all urls file
import dashboards.urls
import auth.urls

from _keenthemes.views import SystemView
from _keenthemes.settings import settings

app.register_error_handler(404, SystemView.as_view('Not Found Error', template_name='pages/' + settings.KT_THEME + '/system/error.html', status=404))
app.register_error_handler(500, SystemView.as_view('System Error', template_name='pages/' + settings.KT_THEME + '/system/error.html', status=500))