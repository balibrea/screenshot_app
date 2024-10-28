#  app_screenshoot.py
#  
#  Copyright 2024 Yosel de Jesús Balibrea Lastre <yosel@auger.org.ar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#  
#  This is a simple program to take screen shots from server side
#  It is intended for the Coihueco LIDAR camera as a tool to check
#  If cover is closed in the right way.
#  



from flask import Flask, render_template, send_file, request  
import mss  
import os

app = Flask(__name__)

screenshot_path = 'static/screenshot.png'
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def index():
    """if request.args.get('refresh'):
        take_screenshot()
    return render_template('index.html', image=screenshot_path)
    """
    take_screenshot()
    image_path = os.path.join(app.static_folder, 'screenshot.png')
    return render_template('index.html')

def take_screenshot():
    with mss.mss() as sct:
        # Capture the screen  
        sct.shot(output=screenshot_path)

@app.route('/download')
def download():
    #return send_file(screenshot_path, as_attachment=True)
    return send_file(os.path.join(app.static_folder, 'screenshot.png'), as_attachment=True)

if __name__ == '__main__':
    # Ensure the static directory exists  
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(host='0.0.0.0', port=5000, debug=True)
