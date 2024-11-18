"""
CITIZEN
Given a DataBase about citizen, perform queries over this DataBase.
Input
The input consists of two blocks: the first block is the DataBase and the second block is the list of queries. Two blocks are separated by a line containing a character *.
1. The first block (DataBase about citizen) consists of lines (number of lines can be upto 100000), each line is the information about a person and is under the format:
                                   <code>  <dat_of_birth>  <fathher_code>   <mother_code>  <is_alive>  <region_code>
in which:
 <code>: the code of the person which is a string of length 7
 <date_of_birth>: the date of birth of the person and has the format YYYY-MM-DD (for example 1980-02-23), <date_of_birth> is before 3000-12-31
 <fathher_code> and <mother_code> is the code of father and mother: they are also strings of length 7. If the code is 0000000, then the current person does not has information about his father or mother
 <is_alive>: a character with two values: ‘Y’ means that the person is still alive, and ‘N’ means tat the current person is died.
 <region_code>: the code of the region where the person lives

2. The second block is the list of queries (number of queries can be upto 100000) over the DataBase which consists of following commands:
 NUMBER_PEOPLE: return the number of people (number of lines of the DataBase)
 NUMBER_PEOPLE_BORN_AT <date>: return the number of people having date-of-birth is equal to <date>
 MOST_ALIVE_ANCESTOR <code>: find the most ancestor (farthest in term of generation distance) of the given person <code>. Return the generation distance between the ancestor found and the given person
 NUMBER_PEOPLE_BORN_BETWEEN <from_date> <to_date>: compute the number of people having date-of-birth between <from_date> and <to_date> (<from_date> and <to_date> are under the form YYYY-MM-DD, <to_date> is before 3000-12-31)
 MAX_UNRELATED_PEOPLE: find a subset of people in which two any people of the subset do not have father/mother-children and the size of the subset is maximal. Return the size of the subset found.
The second block is terminated by a line containing ***.
Output
 Each line presents the result of the corresponding query (described above).

"""
import sys
from collections import defaultdict
from datetime import datetime

class Person:
    def __init__(self, code, date_of_birth, father_code, mother_code, is_alive, region_code):
        self.code = code
        self.date_of_birth = date_of_birth
        self.father_code = father_code
        self.mother_code = mother_code
        self.is_alive = is_alive
        self.region_code = region_code

database = []
person_map = {}
birth_date_count = defaultdict(int)

def parse_database():
    for line in sys.stdin:
        if line.strip() == "*":
            break
        parts = line.split()
        person = Person(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
        database.append(person)
        person_map[person.code] = person
        birth_date_count[person.date_of_birth] += 1

def count_people():
    return len(database)

def count_people_born_at(date):
    return birth_date_count[date]

def find_most_alive_ancestor(code):
    visited = set()
    current_code = code
    generation_distance = 0
    while current_code != "0000000" and current_code not in visited:
        visited.add(current_code)
        person = person_map[current_code]
        if person.father_code != "0000000" and person_map[person.father_code].is_alive == 'Y':
            current_code = person.father_code
        elif person.mother_code != "0000000" and person_map[person.mother_code].is_alive == 'Y':
            current_code = person.mother_code
        else:
            break
        generation_distance += 1
    return generation_distance

def count_people_born_between(from_date, to_date):
    from_date = datetime.strptime(from_date, "%Y-%m-%d")
    to_date = datetime.strptime(to_date, "%Y-%m-%d")
    return sum(1 for person in database if from_date <= datetime.strptime(person.date_of_birth, "%Y-%m-%d") <= to_date)

def max_unrelated_people():
    relations = defaultdict(set)
    all_codes = set()

    for person in database:
        all_codes.add(person.code)
        if person.father_code != "0000000":
            relations[person.code].add(person.father_code)
            relations[person.father_code].add(person.code)
        if person.mother_code != "0000000":
            relations[person.code].add(person.mother_code)
            relations[person.mother_code].add(person.code)

    unrelated_set = set()
    while all_codes:
        current = all_codes.pop()
        unrelated_set.add(current)
        to_remove = {current}
        if current in relations:
            to_remove.update(relations[current])
        for code in to_remove:
            all_codes.discard(code)
            if code in relations:
                for relative in relations[code]:
                    relations[relative].discard(code)
                del relations[code]

    return len(unrelated_set)

def process_queries():
    for line in sys.stdin:
        if line.strip() == "***":
            break
        parts = line.split()
        query = parts[0]
        if query == "NUMBER_PEOPLE":
            print(count_people())
        elif query == "NUMBER_PEOPLE_BORN_AT":
            date = parts[1]
            print(count_people_born_at(date))
        elif query == "MOST_ALIVE_ANCESTOR":
            code = parts[1]
            print(find_most_alive_ancestor(code))
        elif query == "NUMBER_PEOPLE_BORN_BETWEEN":
            from_date = parts[1]
            to_date = parts[2]
            print(count_people_born_between(from_date, to_date))
        elif query == "MAX_UNRELATED_PEOPLE":
            print(max_unrelated_people())

if __name__ == "__main__":
    parse_database()
    database.sort(key=lambda person: person.date_of_birth)
    process_queries()