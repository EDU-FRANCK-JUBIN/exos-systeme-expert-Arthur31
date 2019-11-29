from pyDatalog.pyDatalog import create_terms, load, ask, assert_fact
create_terms('X, croakes, eatFlies, green, frog, sings, chirps, yellow, canary')

load("""
""")

frog(X) <= croakes(X) & eatFlies(X)
canary(X) <= sings(X) & chirps(X)
green(X) <= frog(X)
yellow(X) <= canary(X)



assert_fact('croakes','fritz' )
assert_fact('eatFlies','fritz' )

+sings('titi')
+chirps('titi')

+frog('Toto')
# assert_fact('sings','Jean' )
# assert_fact('chirps','Jean' )

query = 'yellow(X)'
answers = ask(query).answers
print(answers)

print(ask('frog(X)'))



print(ask("frog('fritz')"))

