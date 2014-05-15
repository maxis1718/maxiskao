# -*- coding: UTF-8 -*-

# system
from flask import Flask, render_template, request, redirect, url_for
import os
import util

app = Flask(__name__)

pages = ['profile', 'projects', 'publications', 'cv', 'about']

meta = {}
meta['Keywords'] = ['NTHU,清華大學,自然語言,NLP,Maxis,Kao,高定慧']
meta['Description'] = "Maxis Kao's personal website."
meta['Date'] = '2014-02-26'
meta['Author'] = 'Maxis Kao'


def current(target):
	selected = dict([(p, '' if p != target else 'selected' ) for p in pages])
	triangle = dict([(p, 'hide' if p != target else '' ) for p in pages])
	return (selected, triangle)



@app.route('/')
@app.route('/<section>')
@app.route('/<section>/')
def show(section='profile'):
	selected, triangle = current(section)
	if section == 'projects':
		projects = util.build_projects(projects_xml='static/projects.xml', people_xml='static/people.xml')
		return render_template(section+'.tpl', meta=meta, selected=selected, triangle=triangle, projects=projects)
	if section not in pages: 
		return redirect(url_for('show'))
	else:
		return render_template(section+'.tpl', meta=meta, selected=selected, triangle=triangle)

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=5000)
