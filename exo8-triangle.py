from pyDatalog.pyDatalog import create_terms, load, ask, assert_fact, clear


clear()


create_terms('X, triangle, nbCote, coteEgaux2, coteEgaux3, angleDroit, triangleRectangle, triangleIsocelle, triangleEquilateral, quelquonque,')

load("""
""")

triangle(X) <= nbCote(X, Y) & (Y==3)
triangleRectangle(X) <= triangle(X) & angleDroit(X)
triangleIsocelle(X) <= triangle(X) & coteEgaux(X, Y)  & (Y==2)
triangleEquilateral(X) <= triangle(X) & coteEgaux(X, Y)  & (Y==3)


+nbCote('polygone1', 3)
+angleDroit('polygone1')

+triangle('polygone2')
+coteEgaux('polygone2' 2)

+triangle('polygone3')
+coteEgaux('polygone3', 3)


query = 'yellow(X)'
answers = ask(query).answers
print(answers)

print(ask('frog(X)'))

