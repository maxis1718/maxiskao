from xml.etree import ElementTree
import os

file_path = os.path.dirname(__file__)
abs_file_path = os.path.abspath(file_path)

def build_people(people_xml='people.xml'):
	try:
		root = ElementTree.parse(people_xml).getroot()
	except Exception,e: print str(e)

	PEOPLE = {}
	for people in root:
		name = people.find('name').text
		nick = people.find('nick').text
		link  = '' if people.find('link') is None else people.find('link').text
		PEOPLE[nick.lower()] = {'name': name, 'link':link}
	return PEOPLE

def build_projects(projects_xml='projects.xml', people_xml='people.xml'):

	people_xml = os.path.join(file_path, people_xml)
	projects_xml = os.path.join(file_path, projects_xml)

	PEOPLE = build_people(people_xml)

	root = ElementTree.parse(projects_xml).getroot()
	
	PORJECTS = []

	for project in root:

		P = {}
		P['name'] = '' if project.find('name') is None else project.find('name').text
		P['link'] = '' if project.find('link') is None else project.find('link').text
		P['logo'] = '' if project.find('logo') is None else project.find('logo').text
		P['time'] = '' if project.find('time') is None else project.find('time').text
		P['note'] = '' if project.find('note') is None else project.find('note').text
		# detail
		detail = [] if project.find('detail') is None else project.find('detail')
		detail_html = []
		for p in detail:
			detail_html.append('<p>')
			for e in p:
				text = e.text.strip()
				if e.tag == 'text': html = text
				elif e.tag == 'highlight': html = '<b>' + text + '</b>'
				elif e.tag == 'link': html = '<a ' + ' '.join(['href="'+e.attrib['to']+'"', "target=_blank", '>']) + text + '</a>'
				else: html = text
				detail_html.append(html)
			detail_html.append('</p>')
		P['detail'] = ' '.join(detail_html)

		## enhanced team-member generation
		

		P['team'] = []
		for member in list(project.find('team')):
			m = PEOPLE[member.attrib['nick']]
			P['team'].append( { 'link': m['link'], 'name':m['name'], 'delimiter':'' } )

		P['team'][-1]['delimiter'] = ''

		if len(P['team']) > 1: P['team'][-2]['delimiter'] = 'and'

		if len(P['team']) > 2:
			for i in range(len(P['team'][:-2])):
				P['team'][i]['delimiter'] = ','

		PORJECTS.append(P)

	return PORJECTS
