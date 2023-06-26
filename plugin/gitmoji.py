import json
from urllib import request

import os
import webbrowser

from flox import Flox, ICON_BROWSER, ICON_COPY
from flox.clipboard import Clipboard

ICON_FOLDER = "./Icons"

class Gitmoji(Flox, Clipboard):
   
    def find_file_with_emoji_code(self, emoji_code):  
        found_file = None   
        for root, dirs, files in os.walk(ICON_FOLDER):
            for file_name in files:
                if emoji_code in file_name:
                     found_file = os.path.join(ICON_FOLDER, file_name)
                     break
            return found_file
  
    def emoji_to_code(self, emoji):
        code = []
        for char in emoji:
            char_code = '{:X}'.format(ord(char)).lower()
            code.append(char_code)
        
        emoji_code = "-".join(code)
        return emoji_code
    
    def match(self, query, name, description):
        if query == '':
            return True
        q = query.lower()
        
        if q in name.lower():
            return True
        if q in description.lower():
            return True
            
    def results(self, query):

        with request.urlopen("https://gitmoji.dev/api/gitmojis") as response:
            status_code = response.getcode()
            if status_code == 200:
                data = response.read().decode('utf-8') 
                emoji_data = json.loads(data)

        for gitmoji in emoji_data['gitmojis']:
            if self.match(query, gitmoji['name'], gitmoji['description']):
                emoji_code = self.emoji_to_code(gitmoji['emoji']) 
                icon = self.find_file_with_emoji_code(emoji_code)        
                self.add_item(
                    title=gitmoji['name'],
                    subtitle=gitmoji['description'],
                    icon=icon,
                    context=[gitmoji['emoji']],
                    method = self.copy_emoji,
                    parameters=[gitmoji['emoji']]
                ) 
        
        return self._results
    
    def context_menu(self, data):
        emoji = data[0]

        self.add_item(
            title="Copy",
            subtitle="Copy emoji to clipboard",
            icon=ICON_COPY,
            method=self.copy_emoji,
            parameters=[emoji],
        )
        self.add_item(
            title='Open Gitmoji.dev',
            subtitle='Opens Gitmoji.dev',
            icon=ICON_BROWSER,
            method=self.open_url,
            parameters=[f'https://gitmoji.dev/']
        )

    def open_url(self, url):
        webbrowser.open(url)
    
    def copy_emoji(self, emoji):
        self.put(emoji)
                          
    def query(self, query):
        self.results(query)