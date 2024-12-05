
def get_cats_info(path): #Function is to analys and convert data into good view
    try:
        cats_info = list()
        with open(path, "r", encoding="utf-8") as file:
            lines = [el.strip() for el in file.readlines()] #Removing whitespace chars from lines
            for line in lines:
                cats_info.append(line.split(',')) #spliting the data in strings and adding it to list
            keys = ['id', 'name', 'age'] #here we define keys for the dictionary
            cats_info = [dict(zip(keys, sublist)) for sublist in cats_info] # convert list of lists to a list of dictionaries
            print(cats_info)
            return cats_info
    except FileNotFoundError:
        print(f"File {path} is not found.")
    except OSError:
        print("File {path} has been corrupted or cannot be read.")
    except Exception as e:
        print(f"Unknown error: {e}")

#Check the function:
get_cats_info("TextFiles/cats_info.txt") #Valid input
get_cats_info("TextFiles/cats.txt") #Invalid input



