import pickle
import node

with open("./web.pickle", 'rb+') as f:
	reference_dict = pickle.load(f)
def make_iter(prev_iter, total_list, looking_for_name, already_expanded, reference_dict):
	# prev iter in the form [str, [act_obj, num], [...], str, [...]]
	new_iter = []	
	for item in prev_iter:
		if type(item) != str:
			if item[0].person not in already_expanded:
				if item[0].person in reference_dict:
					item[0].update_connections_via_dict(reference_dict)
				else:
					item[0].update_connections_via_web()
					reference_dict[item[0].person] = item[0].connections
					with open('./web.pickle', "wb+") as handle:
						pickle.dump(reference_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
				already_expanded.append(item[0].person)
				new_iter.append(item[0].person)
				for item2 in item[0].connections:
					new_iter.append([item2[0], item[1] + 1])
					if item2[0].person == looking_for_name:
						print("Match Found!")
						if item2[0].person in reference_dict:
							item2[0].update_connections_via_dict(reference_dict)
						else:
							item2[0].update_connections_via_web()
							reference_dict[item2[0].person] = item2[0].connections
							with open('./web.pickle', "wb+") as handle:
								pickle.dump(reference_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
						for item3 in  new_iter:
							total_list.append(item3)
						return(total_list, reference_dict)
	for item in new_iter:
		total_list.append(item)
	return(make_iter(new_iter, total_list, looking_for_name, already_expanded, reference_dict))

def make_movie_path(lis, current_path):
	current_num = lis[-1][1]
	current_name = lis[-1][0].person
	for x in range(len(lis)):
		index = len(lis)-x-1
		if type(lis[index]) == str:
			name = lis[index]
			break
	for x in range(len(lis)):
		if type(lis[x]) != str:
			if lis[x][0].person == name and lis[x][1] == current_num-1:
				stopping_point = x
				break
	updated_list = lis[:x+1]
	for item in updated_list[-1][0].connections:
		if item[0].person == current_name:
			movie = item[1]
	current_path.append([name, current_name, movie])
	if len(updated_list) == 1:
		return(current_path)
	else:
		return(make_movie_path(updated_list, current_path))
def find_x(start_person, looking_for_name, reference_dict):
	if start_person.person == looking_for_name:
		return([start_person.person, 0])
	else:
		total = [[start_person, 0], start_person.person]
		start = [[start_person, 0], start_person.person]
		data_list, reference_dict = make_iter(start, total, looking_for_name, [], reference_dict)
	path = make_movie_path(data_list, [])
	for item in path:
		print(item[1], end=" was in ")
		print(item[0], end=" in the movie ")
		print(item[2], end = ", ")
	print("number is ", end=" ")
	print(len(path))
	return(reference_dict)

def main():
	person = input("Who do you want to find? ")
	
	bacon = node.Node("Kevin Bacon", "https://www.imdb.com/name/nm0000102/")
	new_reference_dict = find_x(bacon, person, reference_dict)


main()

