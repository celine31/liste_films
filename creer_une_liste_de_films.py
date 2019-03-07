continuer='o'
films=[]
while continuer=='o':
	
	#Demander a l'utilisateur de rentrer des noms de films
	film_a_ajouter=raw_input('Entrez un nom de film : ')
	
	#ajouter ces films dans la liste
	#gerer les doublons
	if film_a_ajouter.lower() in [film[0].lower() for film in films]:
		print('{0} est deja existant dans la liste'.format(film_a_ajouter))
	else:
		note= (raw_input('entrez une note de 1 a 5 : '))
		films.append((film_a_ajouter,note))

	continuer=raw_input('voulez vous continuer? : o/n ')

#classer les films par ordre alphabetique
films.sort()
#afficher la liste
print(films)
print('script fini')