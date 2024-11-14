# The data about bank transactions consists of a sequence of transactions: the information of each transaction has the following format:
#                                                                     <from_account>   <to_account>   <money>   <time_point>   <atm>
# In which:
# •	<from_account>: the account from which money is transferred (which is a string of length from 6 to 20 )
# •	<to_account>: the account which receives money in the transaction (which is a string of length from 6 to 20)
# •	<money>: amount of money transferred in the transaction (which is an integer from 1 to 10000)
# •	<time_point>: the time point at which the transaction is performed, it is a string under the format HH:MM:SS  (hour: minute: second)
# •	<atm>: the code of the ATM where the transaction is taken (a string of length from 3 to 10)
# Example: T00112233445 T001234002 2000 08:36:25 BIDV (at the ATM BIDV, account T00112233445 transfers 2000$ to account T001234002 at time point 08:36:25 (08 hour, 36 minutes, 25 seconds)
# A transaction cycle of length k starting from account a1 is defined to be a sequence of distinct account a1, a2, …, ak  in which there are transactions from account a1 to a2, from a2 to a3, …, from ak to a1.
# Write a program that process the following queries:
# ?number_transactions: compute the total number of transactions of the data
# ?total_money_transaction: compute the total amount of money of transactions
# ?list_sorted_accounts: compute the sequence of bank accounts (including sending and receiving accounts) appearing in the transaction (sorted in an increasing (alphabetical) order)
# ?total_money_transaction_from <account>: compute the total amount of money transferred from the account <account>
# ?inspect_cycle <account> k : return 1 if there is a transaction cycle of length k, starting from <account>, and return 0, otherwise
# Input (stdin)
# The input consists of 2 blocks of information: the data block and the query block
# •	The data block consists of lines:
# o	Each line contains the information about a transaction described above
# o	The data is terminated by a line containing #
# •	The query block consists of lines:
# o	Each line is a query described above
# o	The query block is terminated by a line containing #
#
# Output (stdout)
# •	Print to stdout (in each line) the result of each query described above
import sys
from collections import defaultdict

class Transaction:
    def __init__(self, from_account, to_account, money, time_point, atm):
        self.from_account = from_account
        self.to_account = to_account
        self.money = money
        self.time_point = time_point
        self.atm = atm

transactions = []
money_from_account = defaultdict(int)
accounts = set()
adj_list = defaultdict(list)

def process_transaction(line):
    parts = line.split()
    transaction = Transaction(parts[0], parts[1], int(parts[2]), parts[3], parts[4])
    transactions.append(transaction)
    money_from_account[transaction.from_account] += transaction.money
    accounts.add(transaction.from_account)
    accounts.add(transaction.to_account)
    adj_list[transaction.from_account].append(transaction.to_account)

def dfs(start_account, current_account, k, depth, visited):
    if depth == k:
        return current_account == start_account
    visited.add(current_account)
    for neighbor in adj_list[current_account]:
        if neighbor == start_account and depth + 1 == k:
            return True
        if neighbor not in visited:
            if dfs(start_account, neighbor, k, depth + 1, visited):
                return True
    visited.remove(current_account)
    return False

def inspect_cycle(account, k):
    visited = set()
    return dfs(account, account, k, 0, visited)

def main():
    input = sys.stdin.read
    data = input().splitlines()

    i = 0
    while data[i] != "#":
        process_transaction(data[i])
        i += 1
    i += 1

    while data[i] != "#":
        parts = data[i].split()
        query = parts[0]

        if query == "?number_transactions":
            print(len(transactions))
        elif query == "?total_money_transaction":
            total_money = sum(transaction.money for transaction in transactions)
            print(total_money)
        elif query == "?list_sorted_accounts":
            sorted_accounts = sorted(accounts)
            print(" ".join(sorted_accounts))
        elif query == "?total_money_transaction_from":
            account = parts[1]
            print(money_from_account[account])
        elif query == "?inspect_cycle":
            account = parts[1]
            k = int(parts[2])
            print(1 if inspect_cycle(account, k) else 0)
        i += 1

if __name__ == "__main__":
    main()