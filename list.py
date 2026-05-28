my_list = [1, 2, 3, "hello"]
print(my_list[0])  # 1
my_list.append(4)
my_list[1] = 10
my_list.remove("hello")

#Tuple
my_tuple = (1, 2, 3, "hello")
print(my_tuple[0])  # 1

#dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"])  # Alice
my_dict["age"] = 31

#set
my_set = {1, 2, 3, "hello"}
print(1 in my_set)  # True
my_set.add(4)   
my_set.remove("hello")
