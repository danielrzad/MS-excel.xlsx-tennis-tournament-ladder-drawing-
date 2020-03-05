import requests
from bs4 import BeautifulSoup

URL = (
    "https://portal.pzt.pl/TournamentAcceptanceList.aspx?CategoryID=10&"
    "Male=&TournamentID=20596A85-0C43-4713-B577-FFCF9E68A958"
)
TAG_NAME = "td"
QUERY = {"class": "r"}
response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, "html.parser")
search_result = soup.find_all(TAG_NAME)

lp_list = [f"{i}." for i in range(1, 65)]
to_parse = ['1.', 'CHM1838401', 'Chmielewski', 'Jakub', '2010-08-27', 'Niezrzeszony', '1', '2.', 'GAJ1839129', 'GAJDA', 'KSAWERY', '2010-01-21', 'RKT Return Radom', 'mazowieckie', '3.', 'KOW1938339', 'Kowalik', 'Wojciech', '2010-05-28', 'KS Nadwiślan Kraków', 'małopolskie', '4']
data = []
# for c, v in enumerate(search_result):
# 	if len(v.text.strip()) >= 1:
# 		to_parse.append(v.text.strip())
to_parse.append('out_of_range_error_fix')
#print(to_parse)
for c, v in enumerate(to_parse):
	append_to_data = []

	if v in lp_list:
		name = ' '.join([str(to_parse[c+2]), str(to_parse[c+3])])
		append_to_data.append(name.title())
		if to_parse[c+7].isdigit():
			print(to_parse[c+7])
			print('ELOOO')
			append_to_data.append(to_parse[c+7])
		if to_parse[c+6].isdigit():
			print(to_parse[c+6])
			print('ELOOO')
			append_to_data.append(to_parse[c+6])	
	if len(append_to_data) >= 1:
		data.append(append_to_data)

#print(data)

# 	# if len(element.text.strip()) > 2:
# 	# 	data.append(element.text.strip())
# idx_to_delete = []
# print(data)


