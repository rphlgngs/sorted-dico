import os

class Iterator:

	def __init__(self, dico):
		self._myDico = dico
		self._index = -1
		self._max = len(self._myDico._cle_dico)

	def __iter__(self):
		return self

	def __next__(self):

		if self._index < self._max:
			self._index += 1
			return self._myDico._cle_dico[self._index]
		else:
			raise StopIteration



class SortedDico(dict):
	"""Classe permettant de créer un dictionnaire que l'on peut trier"""

	def __init__(self, **couple):
		"""Constructeur qui créer une liste contenant les clés et une autres
		contenant les valeurs. Si rien n'est passé en paramètre, on créer un
		dictionnaire vide."""

		self._cle_dico = []			#Liste contenant les clés du dictionnaire
		self._valeur_dico = []		#Liste contenant les valeurs du dictionnaire

		# Si au moins une clé avec sa valeur respective sont données, on les ajoutes dans les listes grâce à une boucle "for"
		if len(couple) > 0:
			self._sorted_dico = couple

			for cle, valeur in self._sorted_dico.items():
				self._cle_dico.append(cle)
				self._valeur_dico.append(valeur)
		# Sinon on créer juste un dictionnaire vide
		elif len(couple) == 0:
			self._sorted_dico = {}

	def __getitem__(self, cle):
		""" Fonction qui permet de renvoyer la valeur correpondant à la clé envoyée en paramètre """
		for i in range(len(self._cle_dico)):
			if self._cle_dico[i] == cle:
				return self._valeur_dico[i]

	def __setitem__(self, cle, valeur):
		""" Fonction qui permet d'assigner une nouvelle valeur à une clé ou de créer un nouveau couple """
		if not cle in self._cle_dico:
			self._cle_dico.append(cle)
			self._valeur_dico.append(valeur)
		else:
			for i in range(len(self._cle_dico)):
				if self._cle_dico[i] == cle:
					self._valeur_dico[i] = valeur

		self._sorted_dico[cle] = valeur

	def __delitem__(self, cle):
		""" Fonction qui permet de supprimer un élément """
		for i in range(len(self._cle_dico)):
			if self._cle_dico[i] == cle:
				del self._valeur_dico[i]

		self._cle_dico.remove(cle)
		del self._sorted_dico[cle]

	def __contains__(self, cle):
		""" Fonction qui permet de vérifier si la clé donnée est dans le dictionnaire """
		if cle in self._cle_dico:
			return True
		else:
			return False

	def __len__(self):
		""" Fonction qui renvoie la taille du dictionnaire """
		return len(self._cle_dico)

	def __str__(self):
		""" Fonction qui permet d'afficher le contenu du dictionnaire avec un print """
		txt = "{"
		for i in range(len(self._cle_dico)):
			if i == len(self._cle_dico) - 1:
				txt += "\"{}\": {}".format(self._cle_dico[i], self._valeur_dico[i])
			else:
				txt += "\"{}\": {}, ".format(self._cle_dico[i], self._valeur_dico[i])

		return txt + "}"

	def __iter__(self):
		return Iterator(self)

	def sort(self, key=None, reverse=False):
		""" Fonction pour trier le dictionnaire selon la clé donnée en paramètre """
		temp_dico = []
		temp_dico = sorted(self._sorted_dico.items(), key=key, reverse=reverse)

		self._cle_dico.clear()
		self._valeur_dico.clear()

		for cle, valeur in temp_dico:
			self._cle_dico.append(cle)
			self._valeur_dico.append(valeur)

		del temp_dico

	def keys(self):
		""" Fonction renvoyant la liste des clés """
		return self._cle_dico

	def values(self):
		""" Fonction renvoyant la liste des valeurs """
		return self._valeur_dico

	def items(self):
		""" Fonction renvoyant le couple (clé, valeur) """
		temp_items = []
		for i in range(len(self._cle_dico)):
			temp_items.append((self._cle_dico[i], self._valeur_dico[i]))

		return temp_items


mon_dic = {"f": 11, "b": 2, "z": 1, "x": 44}
mon_dico = SortedDico(**mon_dic)

for cle in mon_dico:
	print(cle)

os.system("pause")