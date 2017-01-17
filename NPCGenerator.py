import random
import sys
import getopt

def main(argv):
	genNPC()	
	
def genNPC():
	if(random.randint(1,100) > 60):
		print('Name: 		'+str(names(True)))
		print('Gender:	 	'+'Male')
		
	else: 
		print('Name: 		'+str(names(False)))
		print('Gender:	 	'+'Female')
	

	print('Age: 		'+str(age()))
	print('Height:	 	'+str(height()))
	print('Hair: 		'+str(haircolor()))
	print('Problems:	'+str(problems()))
	print('Job Motivation:	'+str(jobmot()))
	print('Quirk:		'+str(quirks()))
	
	
def names(male):#Lost p54
	mannames = [ 'Aamir', 'Ayub', 'Binyamin', 'Efraim','Ibrahim','Ilyas', 'Ismail','Jibril','Jumanah','Kazi','Lut','Matta','Mohammed','Mubarak','Mustafa','Nazir','Rahim','Reza','Sharif','Taimur','Usman','Yakub','Yusuf','Zakariya','Zubair','Aiguo','Bohai','Chao','Dai','Dawei','Duyi','Fa','Fu','Gui','Hong','Jianyu','Kang','Li','Niu','Peng','Quan','Ru','Shen','Shi','Song','Tao','Xue','Yi','Yuan','Zian','Adam','Albert','Alfred','Allan','Archibald','Arthur','Basil','Charles','Colin','Donald','Douglas','Edgar','Edmund','Edward','George','Harold','Henry','Ian','James','John','Lewis','Oliver','Philip','Richard','William','Amrit','Ashok','Chand','Dinesh','Gobind','Harinder','Jagdish','Johar','Kurien','Lakshman','Madhav','Mahinder','Mohal','Narinder','Nikhil','Omrao','Prasad','Pratap','Ranjit','Sanjay','Shankar','Thakur','Vijay','Vipul','Yash','Akira','Daisuke','Fukashi','Goro','Hiro','Hiroya','Hotaka','Katsu','Katsuto','Keishuu','Kyuuto','Mikiya','Mitsunobu','Mitsuru','Naruhiko','Nobu','Shigeo','Shigeto','Shou','Shuji','Takaharu','Teruaki','Tetsushi','Tsukasa','Yasuharu','Adesegun','Akintola','Amabere','Arikawe','Asagwara','Chidubem','Chinedu','Chiwetei','Damilola','Esangbedo','Ezenwoye','Folarin','Genechi','Idowu','Kelechi','Ketanndu','Melubari','Nkanta','Obafemi','Olatunde','Olumide','Tombari','Udofia','Uyoata','Uzochi','Aleksandr','Andrei','Arkady','Boris','Dmitri','Dominik','Grigory','Igor','Ilya','Ivan','Kiril','Konstantin','Leonid','Nikolai','Oleg','Pavel','Petr','Sergei','Stepan','Valentin','Vasily','Viktor','Yakov','Yegor','Yuri','Alejandro','Alonso','Amelio','Armando','Bernardo','Carlos','Cesar','Diego','Emilio','Estevan','Felipe','Francisco','Guillermo','Javier','Jose','Juan','Julio','Luis','Pedro','Raul','Ricardo','Salvador','Santiago','Valeriano','Vicente']
	femnames = [ 'Aisha',  'Alimah','Badia','Bisharah','Chanda','Daliya','Fatimah','Ghania','Halah','Kaylah','Khayrah','Layla','Mina','Munisa','Mysha','Naimah','Nissa','Nura','Parveen','Rana','Shalha','Suhira','Tahirah','Yasmin','Zulehka','Biyu','Changying','Daiyu','Huidai','Huiliang','Jia','Jingfei','Lan','Liling','Liu','Meili','Niu','Peizhi','Qiao','Qing','Ruolan','Shu','Suyin','Ting','Xia','Xiaowen','Xiulan','Ya','Ying','Zhilan','Abigail','Anne','Beatrice','Blanche','Catherine','Charlotte','Claire','Eleanor','Elizabeth','Emily','Emma','Georgia','Harriet','Joan','Judy','Julia','Lucy','Lydia','Margaret','Mary','Molly','Nora','Rosie','Sarah','Victoria','Amala','Asha','Chandra','Devika','Esha','Gita','Indira','Indrani','Jaya','Jayanti','Kiri','Lalita','Malati','Mira','Mohana','Neela','Nita','Rajani','Sarala','Sarika','Sheela','Sunita','Trishna','Usha','Vasanta','Aemi','Airi','Ako','Ayu','Chikaze','Eriko','Hina','Kaori','Keiko','Kyouka','Mayumi','Miho','Namiko','Natsu','Nobuko','Rei','Ririsa','Sakimi','Shihoko','Shika','Tsukiko','Tsuzune','Yoriko','Yorimi','Yoshiko','Abike','Adesuwa','Adunola','Anguli','Arewa','Asari','Bisola','Chioma','Eduwa','Emilohi','Fehintola','Folasade','Mahparah','Minika','Nkolika','Nkoyo','Nuanae','Obioma','Olafemi','Shanumi','Sominabo','Suliat','Tariere','Temedire','Yemisi','Aleksandra','Anastasia','Anja','Catarina','Devora','Dima','Ekaterina','Eva','Irina','Karolina','Katlina','Kira','Ludmilla','Mara','Nadezdha','Nastassia','Natalya','Oksana','Olena','Olga','Sofia','Svetlana','Tatyana','Vilma','Yelena','Adalina','Aleta','Ana','Ascencion','Beatriz','Carmela','Celia','Dolores','Elena','Emelina','Felipa','Inez','Isabel','Jacinta','Lucia','Lupe','Maria','Marta','Nina','Paloma','Rafaela','Soledad','Teresa','Valencia','Zenaida']
	surnames = [ 'Abdel','Awad','Dahhak','Essa','Hanna','Harbi','Hassan','Isa','Kasim','Katib','Khalil','Malik','Mansoor','Mazin','Musa','Najeeb','Namari','Naser','Rahman','Rasheed','Saleh','Salim','Shadi','Sulaiman','Tabari','Bai','Cao','Chen','Cui','Ding','Du','Fang','Fu','Guo','Han','Hao','Huang','Lei','Li','Liang','Liu','Long','Song','Tan','Tang','Wang','Wu','Xing','Yang','Zhang','Barker','Brown','Butler','Carter','Chapman','Collins','Cook','Davies','Gray','Green','Harris','Jackson','Jones','Lloyd','Miller','Roberts','Smith','Taylor','Thomas','Turner','Watson','White','Williams','Wood','Young','Achari','Banerjee','Bhatnagar','Bose','Chauhan','Chopra','Das','Dutta','Gupta','Johar','Kapoor','Mahajan','Malhotra','Mehra','Nehru','Patil','Rao','Saxena','Sharma','Sharma','Singh','Trivedi','Venkatesan','Verma','Yadav','Abe','Arakaki','Endo','Fujiwara','Goto','Ito','Kikuchi','Kinjo','Kobayashi','Koga','Komatsu','Maeda','Nakamura','Narita','Ochi','Oshiro','Saito','Sakamoto','Sato','Suzuki','Takahashi','Tanaka','Watanabe','Yamamoto','Yamasaki','Adegboye','Adeniyi','Adeyeku','Adunola','Agbaje','Akpan','Akpehi','Aliki','Asuni','Babangida','Ekim','Ezeiruaku','Fabiola','Fasola','Nwokolo','Nzeocha','Ojo','Okonkwo','Okoye','Olaniyan','Olawale','Olumese','Onajobi','Soyinka','Yamusa','Abelev','Bobrikov','Chemerkin','Gogunov','Gurov','Iltchenko','Kavelin','Komarov','Korovin','Kurnikov','Lebedev','Litvak','Mekhdiev','Muraviov','Nikitin','Ortov','Peshkov','Romasko','Shvedov','Sikorski','Stolypin','Turov','Volokh','Zaitsev','Zhukov','Arellano','Arispana','Borrego','Carderas','Carranzo','Cordova','Enciso','Espejo','Gavilan','Guerra','Guillen','Huertas','Illan','Jurado','Moretta','Motolinia','Pancorbo','Paredes','Quesada','Roma','Rubiera','Santoro','Torrillas','Vera','Vivero']
	if male: 
		return mannames[random.randint(0, 199)]+ ' ' +surnames[random.randint(0,199)]
	else: 
		return femnames[random.randint(0, 199)]+ ' ' +surnames[random.randint(0,199)]


def age(): 
	return random.randint(1,70)+15

def height(): 
	randy = random.randint(1,80)
	if randy < 10:
		return 'Very Short'
	elif randy < 30:
		return 'Short'
	elif randy < 50:
		return 'Average'
	elif randy < 70: 
		return 'Tall'
	else: 
		return 'Very Tall'

def haircolor(): 
	randy = random.randint(1,80)
	if randy < 20:
		return 'White'
	elif randy < 40:
		return 'Brown'
	elif randy < 60:
		return 'Black'
	elif randy < 80: 
		return 'Blonde'
	else: 
		return 'Red'
		
def problems():
	prob = ["Grudge against local authorities", "Has a secret kept from their family.", "Chronic illness", "Enmity of a local psychic", "Has enemies at work", "Owes loan sharks", "Th reatened with loss of spouse, sibling, or child", "Close relative in trouble with the law", "Drug or behavioral addict", "Blackmailed by enemy"]
	return prob[random.randint(0,9)]
	
def jobmot(): 
	jobmot = ["Greed, because nothing else they can do pays better","Idealistic about the job","Sense of social duty","Force of habit takes them through the day","Seeks to please another","Feels inadequate as anything else","Family tradition","Religious obligation or vow","Nothing better to do, and they need the money","Theyre quitting at the first good opportunity","Its a stepping stone to better things","Spite against an enemy discomfited by the work"]
	return jobmot[random.randint(0,11)]
	
def quirks():
	quirk = ["Bald","Terrible taste in clothing","Very thin","Powerful build","Bad eyesight, wears spectacles","Carries work tools constantly","Long hair","Bearded, if male. Ankle-length hair if female.","Scars all over hands","Missing digits or an car","Smells like their work","Repeats himself constantly","Talks about tabloid articles","Booming voice","Vocal dislike of off worlders","Always snuffling","Missing teeth","Fastidiously neat","Wears religious emblems","Speaks as little as possible"]
	return quirk[random.randint(0,19)]
	
	
if __name__ == "__main__":
	main(sys.argv[1:])