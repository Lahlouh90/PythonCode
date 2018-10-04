def afficher(*values, sep=' ', fin='\n'):
      values=list(values)
      for i, parametre in enumerate(values):
          values[i]=str(parametre)

      chaine = sep.join(values)
      chaine += fin

      print(chaine, end='')



afficher('abd', 33, [4], sep=" ")

