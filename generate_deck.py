import sys
import genanki


model = genanki.Model(
    1725376822,
    'Poker hand',
    fields=[
        {'name': 'Position'},
        {'name': 'Situation'},
        {'name': 'Hand'},
        {'name': 'Action'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': """
You have {{Hand}} {{Position}}. {{Situation}}.

<br><br><br>

<img id="img1" src="" height="225" width="150" style="outline-style: solid">&nbsp;&nbsp;&nbsp;&nbsp;
<img id="img2" src="" height="225" width="150" style="outline-style: solid">

<script>

var card_mapping = {
    'A': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
};

// Anki renders the front and back of a card independently. To avoid the suits
// changing when you click "show answer", we use the current time to generate
// the suits rather than generating a random number. The suits rotate every 10
// minutes.
var today = new Date();
var current_time = Math.floor(today.getTime() / (1000 * 60 * 10));
var card1_int = card_mapping["{{Hand}}".charAt(0)];
var card2_int = card_mapping["{{Hand}}".charAt(1)];
var rand = (current_time + card1_int * 13 + card2_int) % 12;

var suit1_index = rand % 4;
var suit1 = all_suits[suit1_index];

all_suits.splice(suit1_index, 1);
var suit2 = all_suits[Math.floor(rand / 4)];

if ("{{Hand}}".endsWith("s"))
  suit2 = suit1;

var card1 = "{{Hand}}".charAt(0);
if (card1 == 'A')
  card1 = 'ace';
if (card1 == 'K')
  card1 = 'king';
if (card1 == 'Q')
  card1 = 'queen';
if (card1 == 'J')
  card1 = 'jack';
if (card1 == 'T')
  card1 = '10';

var card2 = "{{Hand}}".charAt(1);
if (card2 == 'A')
  card2 = 'ace';
if (card2 == 'K')
  card2 = 'king';
if (card2 == 'Q')
  card2 = 'queen';
if (card2 == 'J')
  card2 = 'jack';
if (card2 == 'T')
  card2 = '10';

document.getElementById("img1").src = 'https://raw.githubusercontent.com/hayeah/playing-cards-assets/master/png/' + card1 + '_of_' + suit1 + '.png';
document.getElementById("img2").src = 'https://raw.githubusercontent.com/hayeah/playing-cards-assets/master/png/' + card2 + '_of_' + suit2 + '.png';
</script>
""",
            'afmt': '{{FrontSide}}<hr id="answer">You should {{Action}}.',
        },
    ])


deck = genanki.Deck(
    1396380199,
    'Poker hands')


# Each of these lists of actions has a format like this:
#
# rfi_actions = [
#     ('in the small blind', [
#         ('The hand has folded around to you', [
#             'r,r,r,r,r,r,r,r,r,r,r,r,r',
#             'r,r,r,r,r,r,r,r,r,r,r,r,r',
#             'r,r,r,r,r,r,r,r,r,r,r,r,r',
#             'r,r,r,r,r,r,r,r,r,r,r,rf,rf',
#             'r,r,r,r,r,r,r,r,r,r,rf,rf,rf',
#             'r,r,r,r,r,r,r,r,r,r,rf,rf,rf',
#             'r,r,r,r,r,r,r,r,r,r,r,rf,rf',
#             'r,r,rf,rf,rf,rf,r,r,r,r,r,r,rf',
#             'r,r,rf,rf,rf,rf,rf,r,r,r,r,r,r',
#             'r,rf,rf,rf,rf,rf,rf,rf,r,r,r,r,r',
#             'r,rf,rf,f,f,f,f,f,rf,rf,r,r,r',
#             'r,rf,rf,f,f,f,f,f,f,f,rf,r,r',
#             'r,rf,rf,f,f,f,f,f,f,f,f,f,r',
#         ]),
#         ...
#     ]),
#     ...
# ]
#
# That is, it's a list of positions, each of which has a list of situations, each of which is
# associated with a chart of actions. The actions form a poker chart, with the usual format (A -> 2
# from left to right and top to bottom, pairs on the diagonal starting with AA in the top left,
# suited hands above the diagonal, offsuit hands below). The possible actions are:
#
# - r (raise)
# - rf (raise or fold)
# - rcf (raise, call, or fold)
# - rc (raise or call)
# - c (call)
# - cf (call or fold)
# - f (fold)
#
# You can use the spreadsheet linked in the README to enter these charts more quickly than by hand.

# Whether you should open the pot, or raise first in (RFI)
rfi_actions = [
    ('in the small blind', [
        ('The hand has folded around to you', [
            # TODO
        ]),
    ]),
    ('on the button', [
        ('The hand has folded around to you', [
            # TODO
        ]),
    ]),
    ('in the cutoff', [
        ('The hand has folded around to you', [
            # TODO
        ]),
    ]),
    ('in the hijack', [
        ('The hand has folded around to you', [
            # TODO
        ]),
    ]),
    ('in the lojack', [
        ('The hand has folded around to you', [
            # TODO
        ]),
    ]),
    ('under the gun + 2', [
        ('The hand has folded around to you', [
            # TODO
        ]),
    ]),
    ('under the gun + 1', [
        ('The hand has folded around to you', [
            # TODO
        ]),
    ]),
    ('under the gun', [
        ('You are first to act', [
            # TODO
        ]),
    ]),
]

# What you should do facing one or more limpers
vs_limp_actions = [
    ('in the big blind', [
        ('At least one player has limped in', [
            # TODO
        ]),
    ]),
    ('in the small blind', [
        ('At least one player has limped in', [
            # TODO
        ]),
    ]),
    ('on the button', [
        ('At least one player has limped in', [
            # TODO
        ]),
    ]),
    ('in the cutoff', [
        ('At least one player has limped in', [
            # TODO
        ]),
    ]),
    ('in the hijack', [
        ('At least one player has limped in', [
            # TODO
        ]),
    ]),
    ('in the lojack', [
        ('At least one player has limped in', [
            # TODO
        ]),
    ]),
    ('under the gun + 2', [
        ('At least one player has limped in', [
            # TODO
        ]),
    ]),
    ('under the gun + 1', [
        ('The player under the gun has limped in', [
            # TODO
        ]),
    ]),
]

# What you should do if someone already RFI
vs_rfi_actions = [
    ('in the big blind', [
        ('The small blind has raised', [
            # TODO
        ]),
        ('The player on the button has raised', [
            # TODO
        ]),
        ('The player in the cutoff has raised', [
            # TODO
        ]),
        ('The player in the hijack has raised', [
            # TODO
        ]),
        ('The player in the lojack has raised', [
            # TODO
        ]),
        ('The player under the gun + 2 has raised', [
            # TODO
        ]),
        ('The player under the gun + 1 has raised', [
            # TODO
        ]),
        ('The player under the gun has raised', [
            # TODO
        ]),
    ]),
    ('in the small blind', [
        ('The player on the button has raised', [
            # TODO
        ]),
        ('The player in the cutoff has raised', [
            # TODO
        ]),
        ('The player in the hijack has raised', [
            # TODO
        ]),
        ('The player in the lojack has raised', [
            # TODO
        ]),
        ('The player under the gun + 2 has raised', [
            # TODO
        ]),
        ('The player under the gun + 1 has raised', [
            # TODO
        ]),
        ('The player under the gun has raised', [
            # TODO
        ]),
    ]),
    ('on the button', [
        ('The player in the cutoff has raised', [
            # TODO
        ]),
        ('The player in the hijack has raised', [
            # TODO
        ]),
        ('The player in the lojack has raised', [
            # TODO
        ]),
        ('The player under the gun + 2 has raised', [
            # TODO
        ]),
        ('The player under the gun + 1 has raised', [
            # TODO
        ]),
        ('The player under the gun has raised', [
            # TODO
        ]),
    ]),
    ('in the cutoff', [
        ('The player in the hijack has raised', [
            # TODO
        ]),
        ('The player in the lojack has raised', [
            # TODO
        ]),
        ('The player under the gun + 2 has raised', [
            # TODO
        ]),
        ('The player under the gun + 1 has raised', [
            # TODO
        ]),
        ('The player under the gun has raised', [
            # TODO
        ]),
    ]),
    ('in the hijack', [
        ('The player in the lojack has raised', [
            # TODO
        ]),
        ('The player under the gun + 2 has raised', [
            # TODO
        ]),
        ('The player under the gun + 1 has raised', [
            # TODO
        ]),
        ('The player under the gun has raised', [
            # TODO
        ]),
    ]),
    ('in the lojack', [
        ('The player under the gun + 2 has raised', [
            # TODO
        ]),
        ('The player under the gun + 1 has raised', [
            # TODO
        ]),
        ('The player under the gun has raised', [
            # TODO
        ]),
    ]),
    ('under the gun + 2', [
        ('The player under the gun + 1 has raised', [
            # TODO
        ]),
        ('The player under the gun has raised', [
            # TODO
        ]),
    ]),
    ('under the gun + 1', [
        ('The player under the gun has raised', [
            # TODO
        ]),
    ]),
]

# What to do if you RFI and someone 3-bet
vs_3bet_actions = [
    ('in the small blind', [
        ('You opened with a raise, and the player in the big blind 3-bet', [
            # TODO
        ]),
    ]),
    ('on the button', [
        ('You opened with a raise, and the player in the big blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the small blind 3-bet', [
            # TODO
        ]),
    ]),
    ('in the cutoff', [
        ('You opened with a raise, and the player in the big blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the small blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player on the button 3-bet', [
            # TODO
        ]),
    ]),
    ('in the hijack', [
        ('You opened with a raise, and the player in the big blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the small blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player on the button 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the cutoff 3-bet', [
            # TODO
        ]),
    ]),
    ('in the lojack', [
        ('You opened with a raise, and the player in the big blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the small blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player on the button 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the cutoff 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the hijack 3-bet', [
            # TODO
        ]),
    ]),
    ('under the gun + 2', [
        ('You opened with a raise, and the player in the big blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the small blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player on the button 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the cutoff 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the hijack 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the lojack 3-bet', [
            # TODO
        ]),
    ]),
    ('under the gun + 1', [
        ('You opened with a raise, and the player in the big blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the small blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player on the button 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the cutoff 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the hijack 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the lojack 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player under the gun + 2 3-bet', [
            # TODO
        ]),
    ]),
    ('under the gun', [
        ('You opened with a raise, and the player in the big blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the small blind 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player on the button 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the cutoff 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the hijack 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player in the lojack 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player under the gun + 2 3-bet', [
            # TODO
        ]),
        ('You opened with a raise, and the player under the gun + 1 3-bet', [
            # TODO
        ]),
    ]),
]


def is_hand_in_rfi_range(position, row, col):
    rfi_action = [a for p, a in rfi_actions if p == position]
    if len(rfi_action) == 0:
        raise Exception('Position not found: ' + position)
    if len(rfi_action) != 1:
        raise Exception('Position \'' + position + '\' found multiple times')
    actions = rfi_action[0][0][1]
    action = actions[row].split(',')[col]
    return action != 'f'


def get_hand(row, col):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    card1 = cards[min(row, col)]
    card2 = cards[max(row, col)]
    if row == col:
        return card1 + card2
    return card1 + card2 + ('s' if col > row else 'o')


def convert_action_to_human_readable(action):
    if action == 'r':
        return 'raise'
    if action == 'rf':
        return 'raise or fold'
    if action == 'rcf':
        return 'raise, call, or fold'
    if action == 'rc':
        return 'raise or call'
    if action == 'c':
        return 'call'
    if action == 'cf':
        return 'call or fold'
    if action == 'f':
        return 'fold'
    raise Exception('Unrecognized action: ' + action)


def create_note(position, situation, hand, action, tag):
    return genanki.Note(
        model=model,
        fields=[position, situation, hand, convert_action_to_human_readable(action)],
        tags=[tag])


for tag, actions_list, should_include in [
        ('RFI', rfi_actions, lambda pos, r, c: True),
        ('vs_limp', vs_limp_actions, lambda pos, r, c: True),
        ('vs_RFI', vs_rfi_actions, lambda pos, r, c: True),
        # Note that we use is_hand_in_rfi_range as the should_include function here. This is because
        # the vs_3bet_actions are the actions we take after our RFI is 3-bet, so if the hand is not
        # in our RFI range, we shouldn't get to that point.
        ('vs_3bet', vs_3bet_actions, is_hand_in_rfi_range)]:
    for position, situations in actions_list:
        for situation, all_actions in situations:
            if len(all_actions) != 13:
                raise Exception('Wrong number of rows')
            actions = [list(actions_row.split(',')) for actions_row in all_actions]
            for row, actions_row in enumerate(actions):
                if len(actions_row) != 13:
                    raise Exception('Wrong number of columns' + str(a))
                for col, action in enumerate(actions_row):
                    if should_include(position, row, col):
                        note = create_note(position, situation, get_hand(row, col), action, tag)
                        deck.add_note(note)

filename = sys.argv[1]
genanki.Package(deck).write_to_file(filename)
print('Deck written to ' + filename)
