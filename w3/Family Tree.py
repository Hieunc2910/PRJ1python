#
# Given a family tree represented by child-parent (c,p) relations in which c is a child of p. Perform queries about the family tree:
# descendants <name>: return number of descendants of the given <name>
# generation <name>: return the number of generations of the descendants of the given <name>
#
# Note that: the total number of people in the family is less than or equal to 10
# 4
# Input
# Contains two blocks. The first block contains information about child-parent, including lines (terminated by a line containing ***), each line contains: <child> <parent> where <child> is a string represented the name of the child and <parent> is a string represented the name of the parent. The second block contains lines (terminated by a line containing ***), each line contains two string <cmd> and <param> where <cmd> is the command (which can be descendants or generation) and <param> is the given name of the person participating in the  query.
# Output
# Each line is the result of a corresponding query.
# Example
# Input
# Peter Newman
# Michael Thomas
# John David
# Paul Mark
# Stephan Mark
# Pierre Thomas
# Mark Newman
# Bill David
# David Newman
# Thomas Mark
# ***
# descendants Newman
# descendants Mark
# descendants David
# generation Mark
# ***
# Output
# 10
# 5
# 2
# 2
#PYTHON
import sys
from collections import defaultdict

# Read input
input_text = sys.stdin.read().splitlines()

# Split input into two blocks
relations = []
queries = []
reading_relations = True

for line in input_text:
    if line == "***":
        reading_relations = False
        continue
    if reading_relations:
        relations.append(line)
    else:
        queries.append(line)

# Build the family tree
family = defaultdict(list)
for relation in relations:
    child, parent = relation.split()
    family[parent].append(child)

# Function to count descendants
def count_descendants(name):
    count = 0
    for child in family[name]:
        count += 1 + count_descendants(child)
    return count

# Function to count generations
def count_generations(name):
    max_generation = 0
    for child in family[name]:
        max_generation = max(max_generation, 1 + count_generations(child))
    return max_generation

results = []
for query in queries:
    if query == "***":
        break
    if query.strip():
        parts = query.split()
        if len(parts) == 2:
            cmd, param = parts
            if cmd == "descendants":
                results.append(count_descendants(param))
            elif cmd == "generation":
                results.append(count_generations(param))

for result in results:
    print(result)
