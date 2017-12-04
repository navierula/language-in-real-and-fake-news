def get_file_length(filename):
	with open(filename, 'r', encoding="ISO-8859-1") as f: 
		lines = f.readlines() 
		return len(lines)

fake_headlines_length = get_file_length('cleaned_data/fake_headlines.txt')
real_headlines_length = get_file_length('cleaned_data/real_headlines.txt')

print(fake_headlines_length, real_headlines_length)



