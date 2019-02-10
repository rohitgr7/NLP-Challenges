import re


F_WORDS = [
    'impure', 'forest', 'abducted', 'marries', 'purity', 'listen', 'earth', 'furrow', 'goddess', 'brother-in-law',
    'queen', 'woman', 'female', 'women', 'baroness', 'dedication', 'self-sacrifice', 'women3', 'wifely', 'womanly',
    'virtues', 'miss', 'daughter', 'she', 'her', 'lady', 'madam', 'milady', 'sister', 'mother', 'parents', 'mom',
    'girl', 'hun', 'bride', 'child', 'children', 'adolescent', 'husband', 'couple', 'marriage', 'clothes', 'chastity',
    'pregnant', 'gives', 'birth', 'wonb', 'born', 'wearing', 'sweets', 'dear', 'little'
]

M_WORDS = [
    'businessman', 'co-founder', 'corporation', 'technology', 'engineering', 'slays', 'intemperate', 'washerman',
    'berating', 'wayward', 'kill', 'buried', 'ruin', 'settle', 'exile', 'secretary', 'foreign', 'verses', 'lord',
    'bestial', 'attack', 'wife', 'broke', 'explosion', 'gunpowder', 'cruelty', 'stabbed', 'englishman', 'earl',
    'worthy', 'horseback', 'soldiers', 'guard', 'orders', 'tortuous', 'betraying', 'marquis', 'he', 'his', 'him',
    'male', 'sir', 'monsieur', 'captain', 'brother', 'boy', 'han', 'man', 'courage', 'battle', 'hardships', 'poet',
    'challenge', 'revenge', 'handsome', 'one', 'valiant', 'intelligent', 'united', 'avatar', 'god', 'science', 'wives',
    'refuge', 'unjust', 'world', 'sons', 'sages', 'son', 'king', 'crowned', 'side', 'trust', 'take', 'people', 'refuge',
    'arms', 'slander', 'rule', 'protection', 'hermits', 'shelter', 'religious', 'figures'
]

NOT_PREV = ['her', 'women', 'him', 'gunpowder',
            'one', 'earth', 'marries', 'take', 'he']


def predict(name, maps):
    mappings = maps[name]
    cm, cf = 0, 0

    for w in M_WORDS:
        if w in mappings:
            cm += mappings[w]

    for w in F_WORDS:
        if w in mappings:
            cf += mappings[w]

    print('Male' if cm > cf else 'Female')


def update_maps(txt, name, maps):
    for i, w in enumerate(txt):
        if w.lower() in (M_WORDS + F_WORDS):
            mappings = maps[name]

            if w.lower() in mappings:
                mappings[w.lower()] += 1
            else:
                mappings[w.lower()] = 1

            if i < len(txt) - 1 and txt[i + 1] == name and w.lower() not in NOT_PREV:
                mappings[w.lower()] += 100


# Inputs
N = int(input())
names = [input() for _ in range(N)]
unames = set(names)
counts = dict()
maps = dict()

for x in unames:
    counts[x] = -1
    maps[x] = dict()

# Preprocess corpus
corp = open('corpus.txt', 'r').read().split('\n')
for txt in corp:
    txt = re.sub(r'[(|)|\[|\]|,|.]', '', txt).split()

    for name in unames:
        if counts[name] == -1:
            if name in txt:
                counts[name] = 0

        if counts[name] > -1:
            counts[name] += 1
            if counts[name] < 5 and len(txt) != 0:
                update_maps(txt, name, maps)
            else:
                counts[name] = -1

# Predictions
for name in names:
    predict(name, maps)
