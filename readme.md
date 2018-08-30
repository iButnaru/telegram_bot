# Description

A telegram bot used to store items in an sqlite3 database.
Built using python 3.6.

Bot can be found at http://telegram.me/Conversationbot.

# Architecture

"bot_database.py" creates an SQLite database which will be later used to store messages. After creating the database, new items can be inserted or deleted from it. This requires the installation of the sqlite3 module.

"improved_bot.py" is able to receive a message, store it and to send it back. After storing, the messages can also be deleted.

# Installation

To run the project, first install `requests` package using pip:
 - `pip install requests`

Import project in pycharm and run "improved_bot.py"

# Actions

Sending a message to the bot will store the item in the database. Sending the same message will delete the item, if it already exists in the db.

Work in progress.

