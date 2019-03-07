continuer='o'
films=[]
while continuer=='o':
	
	#Demander a l'utilisateur de rentrer des noms de films
	film=raw_input('Entrez un nom de film : ')

	#ajouter ces films dans la liste
	#gerer les doublons
	if film.lower() in [film.lower() for film in films]:
		print('le film est deja existant dans la liste')
	else:
		films.append(film)

	continuer=raw_input('voulez vous continuer? : o/n ')

#classer les films par ordre alphabetique
films.sort()
#afficher la liste
print(films)
print('script fini')