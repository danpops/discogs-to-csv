# Discogs to CSV via Python

This is a simple Python script to generate a CSV of your entire Discogs collection. You must input your Discogs user token in order for it to work.

## Installation

**PYTHON 3**

Log into your Discogs account and generate a user token at https://www.discogs.com/settings/developers 

After you generate a token, input your token on line 9 of the script.

Next, install discogs_client via pip3

```bash
pip3 install discogs_client
```

Now you are ready to generate a CSV of your collection:

```bash
python3 discogs_collection_csv.py
```

A collection.csv file should appear in your folder. 

Happy collecting :)

## Usage

I use this script to access my Discogs .csv when I need an updated version immediately. 

Feel free to check out my collection on [Instagram](https://www.instagram.com/nowspinninglps) or [Discogs](https://www.discogs.com/user/nowspinninglps/collection?header=1)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

ALSO, will be converting this into a CLI for generating albums from collection to listen to. Should be up by April 2021.
