class Ajilchin:
    def __init__(self, f_name, l_name, id, gender, age, worked_year, still_working, salary, role):
        self.f_name = f_name
        self.l_name = l_name
        self.id = id
        self.gender = gender
        self.age = age
        self.worked_year = worked_year
        self.still_working = still_working
        self.salary = salary
        self.role = role
        
    def __str__(self):
        return f"{self.f_name} ийн {self.l_name} нь {self.worked_year} жил ажилласан. (Ажиллаж байгаа эсэх: {self.still_working} Нас: {self.age} Хүйс: {self.gender} Цалин: {self.salary} Албан тушаал: {self.role})"

def read_workers_from_file(filename):
    workers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            workers.append(Ajilchin(*data))
    return workers

def main():
    filename = 'UbA.txt'
    workers = read_workers_from_file(filename)
    filter(workers)
    
def filter(workers):
    result = workers
    while True:
        i = 0
        for worker in result:
            i += 1
            print(f"{i}. {vars(worker)}\n")

        filter_value = input("Enter your filter to search ('exit' to finish or 'save' to save): ")
        if filter_value.lower() == 'exit':
            break
        elif filter_value.lower() == 'save':
            with open('darkhanB.txt', 'w', encoding='utf-8') as f:
                for worker in result:
                    f.write(str(worker) + '\n')
            print("Amjilttai")
            break

        new_result = []
        for worker in result:
            if filter_value.lower() in [str(value).lower() for value in vars(worker).values()]:
                new_result.append(worker)

        result = new_result

    return result

if __name__ == "__main__":
    main()
