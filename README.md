# Anki poker generator

The script in this repository generates an Anki deck from a set of poker charts. This lets you more
easily and durably memorize the charts, compared to just eyeballing them periodically.

## Note on data

When I used this script, I was specifically using the charts from the Upswing Poker Lab. The data is
not mine to redistribute in this format, so the data variables are empty. You'll have to re-enter
the data yourself from your preferred source.

## How to use

First, enter the poker charts into the script, in the variables `rfi_actions`, `vs_limp_actions`,
`vs_rfi_actions`, and `vs_3bet_actions`. You can use the spreadsheet at
https://docs.google.com/spreadsheets/d/1Of-2F6szvJ63IA_tvc96i6petg1cvrEGfRyY_a5zhCQ/edit#gid=0 to
enter these charts quickly, since the spreadsheet lets you check them by eye.

```
$ virtualenv -p /usr/bin/python3 env
$ source env/bin/activate
$ pip install genanki
$ python generate_deck.py /tmp/poker_hands.apkg
```

The last command should print "Deck written to /tmp/poker_hands.apkg". You can then import the deck
into Anki from that file.