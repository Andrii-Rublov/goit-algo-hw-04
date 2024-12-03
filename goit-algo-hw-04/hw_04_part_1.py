from lief import corrupted


# the function is to calculate total and average salary

def total_salary(path):
    try:
        salary = list()
        with open(path, "r", encoding="utf-8") as salary_bill:
            lines = [el.strip() for el in salary_bill.readlines()] #Removing whitespace chars from lines
            for line in lines:
                salary.append(line.split(',')[1]) #take out salary amounts (string format) from file and add them to list
                salary = [int(x) for x in salary] #converting string format to integers
                total = sum(salary) #calculating total amount of the salary
                average = int(total / len(salary)) #calculating average amount of the salary
            print(f"Total amount of salary: {total}, Average salary: {average}")
            return total, average
    except FileNotFoundError:
        print(f"File {path} is not found.")
    except OSError:
        print("File {path} has been corrupted or cannot be read.")
    # not sure if needed to add here one more exception
    #except Exception as e:
        #print(f"Unknown error: {e}")


#Check the function:
total_salary("TextFiles/salary_file.txt") #Valid input
total_salary("salary.txt") #Invalid input

