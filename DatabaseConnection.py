from mysql import connector
#from escpos.connections import getNetworkPrinter

class DatabaseConnection:
	def __init__(self, user, passwd, dtb, host):
		self.connection = connector.Connect(user = f'{user}', password = f'{passwd}' , database = f'{dtb}', host = f'{host}')
		
	def executeStatement(self, statement):
		self.cursor = self.connection.cursor()
		self.cursor.execute(statement)
		self.connection.commit()
		self.cursor.close()
		
	def printData(self, idInvoer, maandInvoer):
		#haal de data uit de database en zet die in een lijst die je kan uitprinten...
		self.id = self.idInvoer.get()
		self.maand = self.maandInvoer.get()
		
		self.getDataQuery = f'select * from id{self.id} where datum = 20{datetime.now().strftime("%y")}-{self.maand}-12'
		self.executeStatement(getDataQuery)
		
		self.records = statement.fetchall()
		
		for row in self.records:
			print(row)
			
		uitklokTijden = f'select tijdstip from medewerkers where id = {self.id} and message = "uit"'
		inklokTijden = f'select tijdstip from medewerkers where id = {self.id} and message = "in"'
		
		totaalGewerkt = uitklokTijden - inklokTijden
		#printer = getNetworkPrinter()(host = 'localhost', port = 9100)
		#printer.text(f'Medewerker {self.id}: \n', f'self.records\n', f'Totaal: {totaalGewerkt}')
		#printer.lf()
		#connection.close()