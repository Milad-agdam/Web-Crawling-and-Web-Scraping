import pandas as pd


def adding_exel(file_name):
	# df = pd.read_excel('{}.xlsx'.format(file_name))
	# cities = list(df['city'])
	# post_codes = list(df['post_codes'])
	# print(len(cities))
	# print(len(post_codes))
	# return cities, post_codes
	city = input('Enter your city name: ').title()
	post_code = input('Enter your post code name: ').lower()
	print(f'{city} {post_code}')
	return city, post_code

