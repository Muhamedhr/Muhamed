class Oppervlak:
	def __init__(self, aantal, gemOppervlak, freqentie, schoonmaakManier):
		self.aantal = aantal
		self.gemOppervlak = gemOppervlak
		self.frequentie = freqentie
		
		self.schoonmaakManier = schoonmaakManier	#deze staat vast
		
	def calculateNorm(self, aantal, gemOppervlak, freqentie, schoonmaakManier):
		#bereken de norm, aantal uren totaal voor die week
		
		tijdPerVierkanteMeter = SchoonmaakManier.tijdPerVierkanteMeter
		
		totaalOppervlak = gemOppervlak * aantal
		totaleTijd = (totaalOppervlak * freq) * tijdPerVierkanteMeter
		print('Geschatte hoeveelheid uren nodig deze week: ' + totaleTijd)
		return totaleTijd
		
#===============================================================================
#soorten oppervlaktes om schoon te maken

class Wc(Oppervlak):
	def __init__(self):
		self.schoonmaakManier = Dweilen()
		
class OpenRuimte(Oppervlak):
	def __init__(self):
		self.schoonmaakManier = Boenen()
	
class Hal(Oppervlak):
	def __init__(self):
		self.schoonmaakManier = Dweilen()
	
class Lokaal(Oppervlak):
	def __init__(self):
		self.schoonmaakManier = Dweilen()
	
class Kantoor(Oppervlak):
	def __init__(self):
		self.schoonmaakManier = Stofzuigen()
		
class Ramen(Oppervlak):
	def __init__(self):
		self.schoonmaakManier = CleanWindow()
		
class Trappenhuis(Oppervlak):
	def __init__(self):
		self.schoonmaakManier = Dweilen()
		
class Tafel(Oppervlak):
	def __init__(self):
		self.schoonmaakManier = CleanTable()
		
#===============================================================================================
#manieren van schoonmaken (gebruik je bij een specifiek oppervlak)
		
class SchoonmaakManier:
	def __init__(self, tijdPerVierkanteMeter):
		self.tijdPerVierkanteMeter = tijdPerVierkanteMeter
		
class Stofzuigen(SchoonmaakManier):
	def __init__(self):
		tijdPerVierkanteMeter = (1/4)
		
class Dweilen(SchoonmaakManier):
	def __init__(self):
		tijdPerVierkanteMeter = (1/4)
		
class Boenen(SchoonmaakManier):
	def __init__(self):
		tijdPerVierkanteMeter = (1/20)
		
class CleanWindow(SchoonmaakManier):
	def __init__(self):
		tijdPerVierkanteMeter = (5/8)
		
class Vegen(SchoonmaakManier):
	def __init__(self):
		tijdPerVierkanteMeter = (1/30)
		
class CleanTable(SchoonmaakManier):
	def __init__(self):
		tijdPerVierkanteMeter = (36/100)
