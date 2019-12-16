import urllib.request
import lxml.html
class Node():
	def __init__(self, person, page):
		self.person = person
		self.connections = []
		self.page = page
	def add_connection(self,p_class, movie):

		self.connections.append([p_class, movie])
	def update_connections_via_web(self):
		print("working on " + self.person)
		print("Updating via web", end ="\n\n")
		for movie_pair in self.get_list_of_movie_pairs(self.page):
			actor_pair_list = self.get_list_of_actors(movie_pair[0])
			for actor_pair in actor_pair_list:
				if actor_pair[0] != self.person:
					self.add_connection(Node(actor_pair[0], actor_pair[1]), movie_pair[1])
	def get_actor_name(self, page):
		text = self.get_page_html(page)
		doc = lxml.html.document_fromstring(text)
		html = doc.xpath("//table[@id='name-overview-widget-layout']/tbody/tr/td/h1/span[1]")
		return(html[0].text)
	def get_list_of_movie_pairs(self, page):
		pages_list = []
		text = self.get_page_html(page)
		doc = lxml.html.document_fromstring(text)
		odds = doc.xpath("//div[@class='filmo-row odd']")
		evens = doc.xpath("//div[@class='filmo-row even']")
		actual_number = len(odds) + len(evens)
		for i in range(actual_number):
			try:
				individual_movie_html = doc.xpath("//div[@id='filmography']/div[2]//div[" + str(i + 1)  + "]/b/a")
				pages_list.append(['https://www.imdb.com' + str(individual_movie_html[0].attrib['href']), str(individual_movie_html[0].text)])
			except:
				pass
		return pages_list

	def get_list_of_actors(self, page):
		actor_pair_list = []
		text = self.get_page_html(page)
		doc = lxml.html.document_fromstring(text)
		see_more = doc.xpath("//div[@id='titleCast']/div[@class='see-more']/a")
		first_of_url = page[:37]
		if first_of_url[-1] != "/":
			first_of_url += "/"
		try:
			text_2 = self.get_page_html(first_of_url + see_more[0].attrib['href'])
		except:
			return []
		doc2 = lxml.html.document_fromstring(text_2)
		casts_odd = doc2.xpath("//tr[@class='odd']/td[2]/a")
		for item in casts_odd:
			actor_pair_list.append([item.text[1:-1], "http://imdb.com" + item.attrib['href']])
		casts_even = doc2.xpath("//tr[@class='even']/td[2]/a")
		for item in casts_even:
			actor_pair_list.append([item.text[1:-1], "http://imdb.com" + item.attrib['href']])
		return(actor_pair_list)
	def get_page_html(self, page):
		while True:
			try:
				fp = urllib.request.urlopen(page)
				break
			except:
				pass
		mybytes = fp.read()
		mystr = mybytes.decode("utf8")
		fp.close()
		return mystr
	def update_connections_via_dict(self, reference, final = False):
		print("working on " + self.person)
		print("Updating via already existing", end ="\n\n")
		for x in range(len(reference[self.person])):
			if reference[self.person][x][0].person != self.person:
				self.add_connection(reference[self.person][x][0], reference[self.person][x][1])






