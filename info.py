"""
All package info is here. By defaults, opens URL with the repo
"""

info = {
    "name": "new_package",
    "version": "1.0.0",
    "description": "Some describtion",
    "url": "https://github.com/an-dr",
    "author": "Andrei Gramakov",
    "author_email": "mail@agramakov.me",
    "install_requires": [line.rstrip('\n') for line in open("requirements.txt")],  # reading requirements.txt content
    "license": "MIT",

}

if __name__ == '__main__':
    import webbrowser

    webbrowser.open(info["url"])
