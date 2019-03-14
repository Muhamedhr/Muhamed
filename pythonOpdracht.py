from tkinter import *
from datetime import datetime
from DatabaseConnection import *
from Schoonmaakplan import *

dbc = DatabaseConnection('root', 'Muhammed123', 'werktijden', 'localhost')
			
class GUI_Start():
	def __init__(self):
		master = Tk()
		self.master = None
		self.switchFrame(SchoonmaakplanFrame)
		self.master.mainloop()
		
	def switchFrame(self, frameClass):
		newFrame = frameClass(self)
		if self.master is not None:
			self.master.destroy()
		self.master = newFrame
		self.master.grid()
		
class StartFrame(Frame):
	def __init__(self, master):
		super(StartFrame, self).__init__()
		
		self.welkomLabel = Label(text = "Maak een keuze")
		self.welkomLabel.grid(row = 1, column = 2)
		
		self.schoonMaakPlanButton = Button(text = "Schoonmaakplan", command = master.switchFrame(SchoonmaakplanFrame))
		self.schoonMaakPlanButton.grid(row = 2, column = 1)
		
		self.urenRegistratieButton = Button(text = "Uren registratie", command = master.switchFrame(UrenregistratieFrame))
		self.urenRegistratieButton.grid(row = 2, column = 3)
		
class SchoonmaakplanFrame(Frame):
	def __init__(self, master):
		super(SchoonmaakplanFrame, self).__init__()
		
		#self.master = master
		
		self.infoLabel1 = Label(text = 'Vul van elke soort ruimte in hoeveel je er van hebt, wat de gemiddelde oppervlakte is van elke ruimte')
		self.infoLabel1.grid(column = 3, row = 0)
		
		self.infoLabel2 = Label(text = 'en hoe vaak dat soort oppervlak schoongemaakt moet worden per week')
		self.infoLabel2.grid(column = 3, row = 1)
		
		
		'''
		#hoe ik het eigenlijk wou doen...
		self.createRuimteLijn('Wc', 2)
		self.createRuimteLijn('OpenRuimte', 3)
		self.createRuimteLijn('Hal', 4)
		self.createRuimteLijn('Kantoor', 5)
		self.createRuimteLijn('Ramen', 6)
		self.createRuimteLijn('Trappenhuis', 7)
		self.createRuimteLijn('Tafel', 8)
		'''
		
		#=============================================================
		#wc
		self.wcLabel = Label(text = "Wc's: ")
		self.wcLabel.grid(column = 0, row = 2)
				
		self.aantalWcLabel = Label(text = 'Aantal: ')
		self.aantalWcLabel.grid(column = 1, row = 2)
					
		self.aantalWcInvoer = Entry()
		self.aantalWcInvoer.grid(column = 2, row = 2)
					
		self.gemOppWcLabel = Label(text = 'Gemiddeld oppervlak in m2: ')
		self.gemOppWcLabel.grid(column = 3, row = 2)
					
		self.gemOppWcInvoer = Entry()
		self.gemOppWcInvoer.grid(column = 4, row = 2)
		
		self.freqWcLabel = Label(text = 'Frequentie: ')
		self.freqWcLabel.grid(column = 5, row = 2)
					
		self.freqWcInvoer = Entry()
		self.freqWcInvoer.grid(column = 6, row = 2)
		
		#==============================================================
		#openruimte
		self.openRuimteLabel = Label(text = "Open Ruimte: ")
		self.openRuimteLabel.grid(column = 0, row = 3)
				
		self.aantalOpenRuimteLabel = Label(text = 'Aantal: ')
		self.aantalOpenRuimteLabel.grid(column = 1, row = 3)
					
		self.aantalOpenRuimteInvoer = Entry()
		self.aantalOpenRuimteInvoer.grid(column = 2, row = 3)
					
		self.gemOppOpenRuimteLabel = Label(text = 'Gemiddeld oppervlak in m2: ')
		self.gemOppOpenRuimteLabel.grid(column = 3, row = 3)
					
		self.gemOppOpenRuimteInvoer = Entry()
		self.gemOppOpenRuimteInvoer.grid(column = 4, row = 3)
					
		self.freqOpenRuimteLabel = Label(text = 'Frequentie: ')
		self.freqOpenRuimteLabel.grid(column = 5, row = 3)
					
		self.freqOpenRuimteInvoer = Entry()
		self.freqOpenRuimteInvoer.grid(column = 6, row = 3)
		
		#==============================================================
		#Hal
		self.halLabel = Label(text = "Hal: ")
		self.halLabel.grid(column = 0, row = 4)
				
		self.aantalHallenLabel = Label(text = 'Aantal: ')
		self.aantalHallenLabel.grid(column = 1, row = 4)
					
		self.aantalHallenInvoer = Entry()
		self.aantalHallenInvoer.grid(column = 2, row = 4)
					
		self.gemOppHallenLabel = Label(text = 'Gemiddeld oppervlak in m2: ')
		self.gemOppHallenLabel.grid(column = 3, row = 4)
					
		self.gemOppHallenInvoer = Entry()
		self.gemOppHallenInvoer.grid(column = 4, row = 4)
					
		self.freqHallenLabel = Label(text = 'Frequentie: ')
		self.freqHallenLabel.grid(column = 5, row = 4)
					
		self.freqHallenInvoer = Entry()
		self.freqHallenInvoer.grid(column = 6, row = 4)
		
		#==============================================================
		#kantoren
		self.kantorenLabel = Label(text = "Kantoren: ")
		self.kantorenLabel.grid(column = 0, row = 5)
				
		self.aantalKantorenLabel = Label(text = 'Aantal: ')
		self.aantalKantorenLabel.grid(column = 1, row = 5)
					
		self.aantalKantorenInvoer = Entry()
		self.aantalKantorenInvoer.grid(column = 2, row = 5)
					
		self.gemOppKantorenLabel = Label(text = 'Gemiddeld oppervlak in m2: ')
		self.gemOppKantorenLabel.grid(column = 3, row = 5)
					
		self.gemOppKantorenInvoer = Entry()
		self.gemOppKantorenInvoer.grid(column = 4, row = 5)
					
		self.freqKantorenLabel = Label(text = 'Frequentie: ')
		self.freqKantorenLabel.grid(column = 5, row = 5)
					
		self.freqKantorenInvoer = Entry()
		self.freqKantorenInvoer.grid(column = 6, row = 5)
		
		#==============================================================
		#ramen
		self.ramenLabel = Label(text = "Ramen: ")
		self.ramenLabel.grid(column = 0, row = 6)
				
		self.aantalRamenLabel = Label(text = 'Aantal: ')
		self.aantalRamenLabel.grid(column = 1, row = 6)
					
		self.aantalRamenInvoer = Entry()
		self.aantalRamenInvoer.grid(column = 2, row = 6)
					
		self.gemOppRamenLabel = Label(text = 'Gemiddeld oppervlak in m2: ')
		self.gemOppRamenLabel.grid(column = 3, row = 6)
					
		self.gemOppRamenInvoer = Entry()
		self.gemOppRamenInvoer.grid(column = 4, row = 6)
					
		self.freqRamenLabel = Label(text = 'Frequentie: ')
		self.freqRamenLabel.grid(column = 5, row = 6)
					
		self.freqRamenInvoer = Entry()
		self.freqRamenInvoer.grid(column = 6, row = 6)
		
		#==============================================================
		#trappenhuis
		self.trappenhuisLabel = Label(text = "Trappenhuis: ")
		self.trappenhuisLabel.grid(column = 0, row = 7)
				
		self.aantalTrappenhuizenLabel = Label(text = 'Aantal: ')
		self.aantalTrappenhuizenLabel.grid(column = 1, row = 7)
					
		self.aantalTrappenhuizenInvoer = Entry()
		self.aantalTrappenhuizenInvoer.grid(column = 2, row = 7)
					
		self.gemOppTrappenhuizenLabel = Label(text = 'Gemiddeld oppervlak m2: ')
		self.gemOppTrappenhuizenLabel.grid(column = 3, row = 7)
					
		self.gemOppTrappenhuizenInvoer = Entry()
		self.gemOppTrappenhuizenInvoer.grid(column = 4, row = 7)
					
		self.freqTrappenhuizenLabel = Label(text = 'Frequentie: ')
		self.freqTrappenhuizenLabel.grid(column = 5, row = 7)
					
		self.freqTrappenhuizenInvoer = Entry()
		self.freqTrappenhuizenInvoer.grid(column = 6, row = 7)
		
		#==============================================================
		#tafels
		self.tafelLabel = Label(text = "Tafels: ")
		self.tafelLabel.grid(column = 0, row = 8)
				
		self.aantalTafelsLabel = Label(text = 'Aantal: ')
		self.aantalTafelsLabel.grid(column = 1, row = 8)
					
		self.aantalTafelsInvoer = Entry()
		self.aantalTafelsInvoer.grid(column = 2, row = 8)
					
		self.gemOppTafelsLabel = Label(text = 'Gemiddeld oppervlak in m2: ')
		self.gemOppTafelsLabel.grid(column = 3, row = 8)
					
		self.gemOppTafelsInvoer = Entry()
		self.gemOppTafelsInvoer.grid(column = 4, row = 8)
					
		self.freqTafelsLabel = Label(text = 'Frequentie: ')
		self.freqTafelsLabel.grid(column = 5, row = 8)
					
		self.freqTafelsInvoer = Entry()
		self.freqTafelsInvoer.grid(column = 6, row = 8)
		#==============================================================
		
		self.eenSpatie = Label(text = ' ')
		self.eenSpatie.grid(column = 3, row = 9)
		
		self.terugKnop = Button(text = 'Terug')
		self.terugKnop.grid(column = 0, row = 10)
		
		self.calculateButton = Button(text = 'Calculate', command = self.calculateUren)
		self.calculateButton.grid(column = 3, row = 10)
		
		
		#per entry appart de data opvragen?, met id
	'''
	def createRuimteLijn(self, ruimtesoort, regel):
		#Alles in een lijn zetten ->	{ruimteSoort},	aantal: [aantal],	gemOpp: [gemOpp],	freq: [freq]
		
		self.ruimteSoortLabel = Label(text = f"{ruimtesoort}: ")
		self.ruimteSoortLabel.grid(column = 0, row = regel)
				
		self.aantalRuimteSoortLabel = Label(text = 'Aantal: ')
		self.aantalRuimteSoortLabel.grid(column = 1, row = regel)
					
		self.aantalRuimteSoortInvoer = Entry()
		self.aantalRuimteSoortInvoer.grid(column = 2, row = regel)
					
		self.gemOppRuimteSoortLabel = Label(text = 'Gemiddeld oppervlak: ')
		self.gemOppRuimteSoortLabel.grid(column = 3, row = regel)
					
		self.gemOppRuimteSoortInvoer = Entry()
		self.gemOppRuimteSoortInvoer.grid(column = 4, row = regel)
					
		self.freqRuimteSoortLabel = Label(text = 'Frequentie: ')
		self.freqRuimteSoortLabel.grid(column = 5, row = regel)
					
		self.freqRuimteSoortInvoer = Entry()
		self.freqRuimteSoortInvoer.grid(column = 6, row = regel)
	'''
	
	
	def calculateUren(self):
		#bereken de norm, aantal uren totaal voor die week
		#freq, soort, oppervlak per ruimte, verrichte handeling, tijdseenheid per m2
		aantal = (int(self.aantalHallenInvoer.get()) + 
				 int(self.aantalKantorenInvoer.get()) + 
				 int(self.aantalRamenInvoer.get()) + 
				 int(self.aantalOpenRuimteInvoer.get()) + 
				 int(self.aantalTafelsInvoer.get()) + 
				 int(self.aantalTrappenhuizenInvoer.get()) + 
				 int(self.aantalWcInvoer.get()))
				 
		gemOppervlak = int((int(self.gemOppHallenInvoer.get()) + 
						int(self.gemOppKantorenInvoer.get()) + 
						int(self.gemOppOpenRuimteInvoer.get()) + 
						int(self.gemOppRamenInvoer.get()) + 
						int(self.gemOppTafelsInvoer.get()) + 
						int(self.gemOppTrappenhuizenInvoer.get()) + 
						int(self.gemOppWcInvoer.get())) / 7)
						
		frequentie = int((int(self.freqHallenInvoer.get()) + 
					 int(self.freqKantorenInvoer.get()) + 
					 int(self.freqOpenRuimteInvoer.get()) + 
					 int(self.freqRamenInvoer.get()) + 
					 int(self.freqTafelsInvoer.get()) + 
					 int(self.freqTrappenhuizenInvoer.get()) + 
					 int(self.freqWcInvoer.get()))/7)
		
		#totaalOppervlak = gemOppervlak * aantal
		#totaleTijd = (totaalOppervlak * freq) * tijdPerVierkanteMeter
		
		totaleOppervlak = int(aantal) * int(gemOppervlak)
		totaleTijd = int((totaleOppervlak * int(frequentie)) * (5 / 60 / 60))
		#vijf seconden per m2

		totaleUrenLabel = Label(text = f'Geschatte hoeveelheid uren nodig deze week: {totaleTijd}')
		totaleUrenLabel.grid(row = 11, column = 3)
		
		aantalMedewerkersNodig = int((totaleTijd / 8) + 1)	#8 uur werken per medewerker (kun je instellen)
		
		aantalMedewerkersNodigLabel = Label(text = f'Geschatten hoeveelheid medewerkers nodig deze week: {aantalMedewerkersNodig}')
		aantalMedewerkersNodigLabel.grid(row = 12, column = 3)
		
		print(f'Geschatte hoeveelheid uren nodig deze week: {totaleTijd}')
		print(f'Geschatte hoeveelheid medewerkers nodig deze week DEZE WEEEEK: {aantalMedewerkersNodig}')
		print(gemOppervlak)
		print(aantal)
		print(frequentie)
		print(type(aantal))
		print(type(frequentie))
		print(type(gemOppervlak))
		return totaleTijd
		
		
class UrenregistratieFrame(Frame):
	def __init__(self,master):
		super(UrenregistratieFrame, self).__init__()
		
		self.master = master
		
	def showInklokFrame(self):
		self.inklokPage.tkraise()
		dbc.executeStatement(f"""insert into GUI_LOG values('INKLOK button pressed',
																	'{datetime.now().strftime('%y-%m-%d')}',
																	'{datetime.now().strftime('%H:%M:%S')}')""")
				
	def showMenuFrame(self):
		self.menuPage.tkraise()
		dbc.executeStatement(f"""insert into GUI_LOG values('MENU button pressed',
																	'{datetime.now().strftime('%y-%m-%d')}',
																	'{datetime.now().strftime('%H:%M:%S')}')""")
				
	def showUitklokFrame(self):
		self.uitklokPage.tkraise()
		dbc.executeStatement(f"""insert into GUI_LOG values('UITKLOK button pressed',
																	'{datetime.now().strftime('%y-%m-%d')}',
																	'{datetime.now().strftime('%H:%M:%S')}')""")
																	
		startLabel = Label(self.master, text = 'Werktijd Registratie', font = ('Calibri', 40))
		startLabel.pack()
			
		inklokButton = Button(self.master, text='Inklokken',command = showInklokFrame)
		inklokButton.pack()
		
		menuButton = Button(self.master, text='Menu', command = showMenuFrame)
		menuButton.pack()
		
		uitklokButton = Button(self.master, text='Uitklokken',command = showUitklokFrame)
		uitklokButton.pack()


class InklokFrame(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.master.tkraise()

		self.inklokLabel = Label(text='Vul je medewerkersnummer in', font = ('Calibri', 40))
		self.inklokLabel.pack(expand=True)
		
		self.inklokInvoer = Entry()
		self.inklokInvoer.pack(expand=True)	
		
		self.confirmInklok = Button(text = 'Bevestig', command = self.ingeklokt)
		self.confirmInklok.pack(expand=True)
		
		self.aantalMedewerkers = 24
		
		#self.ID = uitklokInvoer.get()
		
	def ingeklokt(self):
		#ga naar de bevestigd pagina
		try:
			int(self.inklokInvoer.get())
			if(int(self.inklokInvoer.get()) not in range(1, self.aantalMedewerkers)):
				raise ValueError
				
			dbc.executeStatement(f"""insert into GUI_LOG values('medewerker {self.inklokInvoer.get()} ingeklokt',
																		'{datetime.now().strftime('%y-%m-%d %H:%M:%S')}',
																		'{datetime.now().strftime('%y-%m-%d %H:%M:%S')}')""")
																		
			dbc.executeStatement(f"""insert into id{self.inklokInvoer.get()} values('medewerker {self.inklokInvoer.get()} ingeklokt',
																		'{datetime.now().strftime('%y-%m-%d %H:%M:%S')}',
																		'{datetime.now().strftime('%y-%m-%d')}')""")
																			
			
		except ValueError:
			print('ERROR: vul je medewerkersnummer in')
			dbc.executeStatement(f"""insert into GUI_LOG values('medewerker {self.inklokInvoer.get()} ingeklokt', 
																	'{datetime.now().strftime('%y-%m-%d')}', 
																	'{datetime.now().strftime('%y-%m-%d %H:%M:%S')}')""")
			try:
				self.errorLabel.destroy()
				self.errorLabel = Label(text = 'Vul je medewerkersnummer in!', fg = 'Red')
				self.errorLabel.pack()
			except:
				self.errorLabel = Label(text = 'Vul je medewerkersnummer in!', fg = 'Red')
				self.errorLabel.pack()
		
			
class GetListFrame(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.master = master
		self.master.tkraise()
		
		self.getListLabel = Label(text='Vul je medewerkersnummer in', font = ('Calibri', 40))
		self.getListLabel.pack(expand=True)
		
		self.idInvoer = Entry()
		self.idInvoer.pack(expand=True)
		
		self.maandLabel = Label(text='Vul de gewenste maand in', font = ('Calibri', 40))
		self.maandLabel.pack(expand=True)
		
		self.maandInvoer = Entry()
		self.maandInvoer.pack(expand=True)
		
		#je hebt nu medewerkersnummer en maand, dat is genoeg (denk ik) om de hele lijst uit de database te halen en te printen
		printData(idInvoer, maandInvoer) 
			
		#nu nog naar de printer sturen en printen...
		
		self.bevestigKnop = Button(text = 'print!', command = getData)
		self.bevestigKnop.pack()
			
class BevestigKlokFrame(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.master = master
		self.master.tkraise()

		self.klokmessage = klokmessage
		#je pakt de message van de laatste toegevoegde aan de database (in of uit) en voegt daar het id aan toe en dan heb je je message
		#haal de laatste regel maar uit de database nu...
		messageDataQuery = f'select message from medewerkers order by id desc limit 1'
		idDataQuery = f'select id from medewerkers order by id desc limit 1'
		
		self.bevestigKlokLabel = Label(text = '{messageDataQuery}klokken van medewerker {idDataQuery} bevestigd!')
		self.bevestigKlokLabel.pack()
		
	def gaTerug(self, lastDtbMessage):
		if(lastDtbMessage == 'in'):
			dbc.executeStatement(f"""insert into GUI_LOG values('TERUG button pressed at bevestigklok',
																	'{datetime.now().strftime('%y-%m-%d')}',
																	'{datetime.now().strftime('%H:%M:%S')}')""")
			tkraise(InklokFrame)
			
		else:
			dbc.executeStatement(f"""insert into GUI_LOG values('TERUG button pressed at bevestigklok',
																	'{datetime.now().strftime('%y-%m-%d')}',
																	'{datetime.now().strftime('%H:%M:%S')}')""")
			tkraise(UitklokFrame)
		
		
		#self.terugKnop = Button(text = 'terug', command = gaTerug)
		#self.terugKnop.pack()


class UitklokFrame(Frame):
	
	def __init__(self,master):
		super().__init__(master)
		self.master = master
		self.master.tkraise()

		self.uitklokLabel = Label(text='Vul je medewerkersnummer in', font = ('Calibri', 40))
		self.uitklokLabel.pack(expand=True)
		
		self.uitklokInvoer = Entry()
		self.uitklokInvoer.pack(expand=True)
		
		self.confirmUitklok = Button(text = 'Bevestig', command = self.uitgeklokt)
		self.confirmUitklok.pack(expand=True)
		
		self.aantalMedewerkers = 24
		#self.ID = uitklokInvoer.get()
		
	def uitgeklokt(self):
		#ga naar de bevestigd pagina
		try:
			int(self.uitklokInvoer.get())
			if(int(self.uitklokInvoer.get()) not in range(1, self.aantalMedewerkers)):
				raise ValueError
				
			dbc.executeStatement(f"""insert into GUI_LOG values('medewerker {self.uitklokInvoer.get()} uitgeklokt',
																		'{datetime.now().strftime('%y-%m-%d %H:%M:%S')}',
																		'{datetime.now().strftime('%y-%m-%d %H:%M:%S')}')""")
																		
			dbc.executeStatement(f"""insert into id{self.uitklokInvoer.get()} values('medewerker {self.uitklokInvoer.get()} uitgeklokt',
																		'{datetime.now().strftime('%y-%m-%d %H:%M:%S')}',
																		'{datetime.now().strftime('%y-%m-%d')}')""")
																			
			
		except ValueError:
			print('ERROR: vul je medewerkersnummer in')
			dbc.executeStatement(f"""insert into GUI_LOG values('medewerker {self.uitklokInvoer.get()} uitgeklokt', 
																	'{datetime.now().strftime('%y-%m-%d')}', 
																	'{datetime.now().strftime('%y-%m-%d %H:%M:%S')}')""")
			try:
				self.errorLabel.destroy()
				self.errorLabel = Label(text = 'Vul je medewerkersnummer in!', fg = 'Red')
				self.errorLabel.pack()
			except:
				self.errorLabel = Label(text = 'Vul je medewerkersnummer in!', fg = 'Red')
				self.errorLabel.pack()
		
#gui = GUI_Start()		

root = Tk()
gui = UitklokFrame(root)
root.mainloop()

