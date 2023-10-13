nouns,verbs,adjectives,randoms = [],[],[],[]
nounn,verbb,adjectivee,randd = ['noun1','noun2','noun3'],['verb1','verb2','verb3'], ['adj1','adj2','adj3'], ['rand1', 'rand2', 'rand3']
# verbb = ['verb1','verb2','verb3']
# adjectivee = ['adj1','adj2','adj3']
# randd = ['rand1', 'rand2', 'rand3']
lists = [nouns,verbs, adjectives, randoms]
for x in range(3):
    if x == 1:
        noun = input('Give me a place:>  ')
    elif x==2:
        noun = input("Give me a plural noun Ex:humans |> ")
    else:
        noun = input('Give me a location |> ')
    nouns.append(noun)
for x in range(3):
    verb = input('Give me a verb:>  ')
    verbs.append(verb)
for x in range(3):
    adjective = input('Give me a adjective:>  ')
    adjectives.append(adjective)
for x in range(3):
    random = input("pick any famous person|>  ") 
    randoms.append(random)

for count, x in enumerate(nouns):
    nounn[count]=x
for count, x in enumerate(verbs):
    verbb[count]=x
for count, x in enumerate(adjectives):
    adjectivee[count]=x
for count, x in enumerate(randoms):
    randd[count]=x


madlib = f"""
    Once upon a time in {nounn[0]}, three {adjectivee[0]} {nounn[1]} decided to {verbb[0]} to {nounn[2]}.\n
    Little did they know, their adventure would turn into a {adjectivee[1]} and {adjectivee[2]} escape.\n
    Along the way, they encountered {randd[0]}, and {randd[1]}.\n 
    Surprised, they asked {randd[1]} for advice on how to {verbb[1]} and were delighted when {randd[2]} shared a story.
"""
print(madlib)