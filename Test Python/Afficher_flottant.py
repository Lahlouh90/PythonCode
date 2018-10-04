def afficher_flottant(flottant):

   if type(flottant) is not float:
       raise TypeError("Le parametre attentu doit étres un flottant")
   flottant=str(flottant)
   partie_entier, partie_flottante= flottant.split(".")
   return print(",".join([partie_entier, partie_flottante[:3]]))

afficher_flottant(3.0)