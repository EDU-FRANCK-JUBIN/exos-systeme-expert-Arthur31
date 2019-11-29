from pyDatalog.pyDatalog import create_terms, load, ask, assert_fact, clear

clear()


create_terms('X, g001, g002, g003, g004, g005, g006, g007, g008, g009, g010, g011, g012, g013, g014, g015, g016, g017, g018, g019, g020, g021, g022, g023, p01, p02, p03, p04, p05, p06, p07, p08')


load("""
""")

p01(X) <= g001(X) & g002(X) & g003(X) & g004(X)
p02(X) <= g001(X) & g002(X) & g005(X) & g006(X)
p03(X) <= g007(X) & g008(X)
p04(X) <= g009(X) & g010(X) & g011(X) & g012(X)
p05(X) <= g013(X) & g014(X) & g015(X) & g016(X)
p06(X) <= g010(X) & g015(X) & g016(X) & g017(X) & g018(X) & g019(X)
p07(X) <= g010(X) & g019(X) & g020(X) & g021(X)
p08(X) <= g001(X) & g010(X) & g019(X) & g022(X) & g023(X)

+g001("zzz")
+g002("zzz")
+g003("zzz")
+g004("zzz")
+g005("zzz")
+g006("zzz")
+g007("zzz")
+g008("zzz")
+g009("zzz")
+g010("zzz")
+g011("zzz")
+g012("zzz")
+g013("zzz")
+g014("zzz")
+g015("zzz")
+g016("zzz")
+g017("zzz")
+g018("zzz")
+g019("zzz")
+g020("zzz")
+g021("zzz")
+g022("zzz")
+g023("zzz")


+g001('Jean')
+g007('Jean')
+g008('Jean')

print(ask("p03('Jean')"))

query = "p03(X)"
answers = ask(query).answers
print(answers)





# +g001("Paupière rouge")
# +g002("Paupière enflée")
# +g003("Douleur oculaire et démangeaisons")
# +g004("La saleté oculaire est collante et dépend des cils")
# +g005("Ressentir une gêne et des douleurs oculaires")
# +g006("Douleur quand on presse")
# +g007("Bosse sur les paupières dans quelques semaines")
# +g008("Indolore lorsqu'il est pressé")
# +g009("Il y a un peu de poussière dans l'oeil")
# +g010("Yeux rouges")
# +g011("Les yeux sont un peu irritants et douloureux")
# +g012("Maux de gorge et fièvre")
# +g013("Yeux qui piquent")
# +g014("Yeux enflés et douloureux")
# +g015("Yeux larmoyants")
# +g016("Les yeux brillent")
# +g017("Les yeux brillent")
# +g018("Douleur oculaire")
# +g019("Vision diminuée")
# +g020("Sensation de douleur légère à sévère")
# +g021("Yeux sales")
# +g022("Douleur intense")
# +g023("Yeux enflés difficiles à ouvrir")




# assert_fact(p01, "Blépharite")
# assert_fact(p02, "Orgelet de prévention ")
# assert_fact(p03, "Chalazion")
# assert_fact(p04, "Conjonctiviste viral")
# assert_fact(p05, "Conjonctiviste en allergie")
# assert_fact(p06, "Kératite")
# assert_fact(p07, "Ulcère cornéen")
# assert_fact(p08, "Endophtalmie")




# assert_fact(p01, "Blépharite", "Elle est causée par des allergies à la poussière, à la fumée, à des produits chimiques et à des bactéries staphylococciques, alpha streptocoques ou bêta-hémolytiques ', - Compression de sels physiologiques \ n-Fourniture d'antibiotiques', '- favorise la propreté de la zone autour des yeux et les mains si vous voulez toucher les yeux.")
# assert_fact(p02, "Orgelet de prévention ", "Causée par une inflammation superative des glandes des paupières ',' - Compressez à l'eau tiède \ r \ n-Donnez une pommade antibiotique \ r \ n-Donnez des antibiotiques systémiques \ r \ n-Donnez une protection anti-douleur ',' - Conservez la propreté de la zone environnante \ r \ n les yeux et les mains si vous voulez toucher les yeux. \ r \ n- Évitez les facteurs qui provoquent des allergies.")
# assert_fact(p03, "Chalazion", "Causée par une inflammation chronique de la granulomatose des glandes de Meibomian bloquées ',' étant donné une incision ',' - maintenir nettoyer la zone autour des yeux et des mains quand ils veulent toucher les yeux.")
# assert_fact(p04, "Conjonctiviste viral", "Inflammation de la conjonctive causée par le virus ',' -Avec l'administration d'antibiotiques systomatiques et \ r \ n ',' -Le maintien de l'état corporel (propreté) - Le contact avec les personnes atteintes d'une maladie des yeux")
# assert_fact(p05, "Conjonctiviste en allergie", "Causée par la conjonctive en raison de réactions allergiques à des non-infections ',' -En fournissant anti-allergique topique et systématique. ',' - gardez la zone autour des yeux et des mains propre lorsque vous souhaitez toucher les yeux. \ r \ n-Évitez les facteurs allergiques.")
# assert_fact(p06, "Kératite", "Causé en raison d'une inflammation de la cornée ',' En fournissant des déchirures artificielles, des antibiotiques et des cycloplégiques. ',' -En interdisant l'utilisation de lentilles de contact \ r \ n ou en assurant la procédure d'installation \ r \ n et le retrait des lentilles de contact selon les règles en vigueur. \ r \ n- Utiliser une protection oculaire tout en continuant \ r \ n fonctionne principalement en ce qui concerne \ r \ n avec les rayons UV.")
# assert_fact(p07, "Ulcère cornéen", "Il s'agit d'une infection résultant d'une infection bactérienne pathogène à gram négatif de la cornée ',' étant donné des antibiotiques cycloplégiques et topiques et sous-conjonctivaux. ',' - Utilisez des protections oculaires. \ r \ n-Évitez les lentilles de contact.")
# assert_fact(p08, "Endophtalmie", "Causée pour cause d'infection après un traumatisme ou une intervention chirurgicale, ou endogène en raison d'une sepsie ',' Dans l'hospitalisation \ antibiotiques systémiques (perfusion / injection) \ gouttes Antibiotica \ anti-douleur ',' Maintenir la propreté la zone autour des yeux et des mains quand ils veulent toucher les yeux")