import json
import cattr
import os
import webbrowser

from dataclasses import dataclass
from typing import List

from flox import Flox
from flox.clipboard import Clipboard

ICONS_FOLDER= r"./Icons"
CLIPBOARD_ICON = r"./Images/clipboard_icon.png"
GITMOJI_JSON_FILE = r"./data/gitmojis.json"

@dataclass
class Gitmoji:
    emoji: str = ""
    entity: str = ""
    code: str = ""
    description: str = ""
    name: str = ""
    example: str = ""

class GitmojiLoader(Flox, Clipboard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with open(GITMOJI_JSON_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            converter = cattr.Converter()
            self.gitmojis = [converter.structure(item, Gitmoji) for item in data]

    def results(self, query):
        for gitmoji in self.gitmojis:
            comparable_items = self._get_gitmoji_comparable_item(gitmoji)
            if any(self.match(query, str(item)) for item in comparable_items):
                self.add_item(
                    title=self._get_gitmoji_title(gitmoji),
                    subtitle=self._get_gitmoji_subtitle(gitmoji),
                    icon=self._get_gitmoji_icon(gitmoji),
                    context=[gitmoji.emoji],
                    method=self.copy_to_clipboard,
                    parameters=[gitmoji.emoji],
                )
        return self._results

    def _get_gitmoji_comparable_item(self, gitmoji:Gitmoji) -> List[str]:
        return [gitmoji.name, gitmoji.description, gitmoji.emoji]
    
    def _get_gitmoji_title(self, gitmoji:Gitmoji) -> str:
        return f"[{gitmoji.name}] {gitmoji.description}"
    
    def _get_gitmoji_subtitle(self, gitmoji:Gitmoji) -> str:
        return f"{gitmoji.example}"

    def _get_gitmoji_icon(self, gitmoji:Gitmoji) -> str:
        found_file = None
        for root, dirs, files in os.walk(ICONS_FOLDER):
            for file_name in files:
                emoji_code = self.emoji_to_code(gitmoji.emoji)
                if emoji_code in file_name:
                    found_file = os.path.join(ICONS_FOLDER, file_name)
                    break
            return found_file
        
    def emoji_to_code(self, emoji: str) -> str:
        code = []
        for char in emoji:
            char_code = "{:X}".format(ord(char)).lower()
            code.append(char_code)

        emoji_code = "-".join(code)
        return emoji_code

    def match(self, query: str, item: str):
        if query == "":
            return True
        q = query.lower()

        if q in item.lower():
            return True

    def context_menu(self, emoji: str):
        self.add_item(
            title="Copy Emoji",
            subtitle="Copy emoji to clipboard",
            icon=CLIPBOARD_ICON,
            method=self.copy_to_clipboard,
            parameters=[emoji],
        )
        self.add_item(
            title="Open Gitmoji.dev",
            subtitle="Opens Gitmoji.dev",
            method=self.open_url,
            parameters=["https://gitmoji.dev/"],
        )

    def open_url(self, url: str):
        webbrowser.open(url)

    def copy_to_clipboard(self, item: str):
        self.put(item)

    def query(self, query: str):
        self.results(query)
