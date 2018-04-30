import requests
import pygal

url = 'https://api.github.com/search/repositories?q=language:javascript&sort=forks'
r = requests.get(url)
print('Status code', r.status_code)

response_dict = r.json()
print(response_dict['total_count'])

repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict = {
	    'value': repo_dict['forks_count'],
	    'xlink': repo_dict['html_url'],
	}
	plot_dicts.append(plot_dict)

chart = pygal.Bar(x_label_rotation=45)
chart.title = 'Most-Forked Javascript Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('js_repo.svg')

