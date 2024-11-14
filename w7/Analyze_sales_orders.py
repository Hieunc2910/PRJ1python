# Data about sales in an e-commerce company (the e-commerce company has several shops) consists a sequence of lines, each line (represents an order) has the following information:
#             <CustomerID> <ProductID> <Price> <ShopID> <TimePoint>
# in which the customer <CustomerID> buys a product <ProductID> with price <Price> at the shop <ShopID> at the time-point <TimePoint>
# <CustomerID>: string of length from 3 to 10
# <ProductID>: string of length from 3 to 10
# <Price>: a positive integer from 1 to 1000
# <ShopID>: string of length from 3 to 10
# <TimePoint>: string representing time-point with the format HH:MM:SS (for example, 09:45:20 means the time-point 9 hour 45 minutes 20 seconds)
#
# Perform a sequence of queries of following types:
# ?total_number_orders: return the total number of orders
# ?total_revenue: return the total revenue the e-commerce company gets
# ?revenue_of_shop <ShopID>: return the total revenue the shop <ShopID> gets
# ?total_consume_of_customer_shop <CustomerID> <ShopID>: return the total revenue the shop <ShopID> sells products to customer <CustomerID>
# ?total_revenue_in_period <from_time> <to_time>: return the total revenue the e-commerce gets of the period from <from_time> to <to_time> (inclusive)
#
# Input
# The input consists of two blocks of data:
# The first block is the operational data, which is a sequence of lines (number of lines can be upto 100000), each line contains the information of a submission with above format
# The first block is terminated with a line containing the character #
# The second block is the query block, which is a sequence of lines (number of lines can be upto 100000), each line is a query described above
# The second block is terminated with a line containing the character #
#
# Output
# Write in each line, the result of the corresponding query
#PYTHON
import datetime
import sys
from collections import defaultdict
import bisect

class Order:
    def __init__(self, CustomerID, ProductID, Price, ShopID, TimePoint):
        self.CustomerID = CustomerID
        self.ProductID = ProductID
        self.Price = Price
        self.ShopID = ShopID
        self.TimePoint = TimePoint

orders = []
revenue_of_shop = defaultdict(int)
revenue_of_customer_shop = defaultdict(lambda: defaultdict(int))
total_revenue = 0
time_points = []

def process_order(line):
    global total_revenue
    parts = line.split()
    order = Order(parts[0], parts[1], int(parts[2]), parts[3], parts[4])
    orders.append(order)
    revenue_of_shop[order.ShopID] += order.Price
    total_revenue += order.Price
    revenue_of_customer_shop[order.CustomerID][order.ShopID] += order.Price
    time_points.append((datetime.datetime.strptime(order.TimePoint, "%H:%M:%S"), order.Price))

def get_total_number_orders():
    return len(orders)

def get_total_revenue():
    return total_revenue

def get_revenue_of_shop(shop_id):
    return revenue_of_shop[shop_id]

def get_total_consume_of_customer_shop(customer_id, shop_id):
    return revenue_of_customer_shop[customer_id][shop_id]

def get_total_revenue_in_period(from_time, to_time):
    from_time = datetime.datetime.strptime(from_time, "%H:%M:%S")
    to_time = datetime.datetime.strptime(to_time, "%H:%M:%S")
    start_index = bisect.bisect_left(time_points, (from_time,))
    end_index = bisect.bisect_right(time_points, (to_time,))
    return sum(price for time, price in time_points[start_index:end_index])

def main():
    input = sys.stdin.read
    data = input().splitlines()

    i = 0
    while data[i] != "#":
        process_order(data[i])
        i += 1
    i += 1

    while data[i] != "#":
        parts = data[i].split()
        query = parts[0]

        if query == "?total_number_orders":
            print(get_total_number_orders())
        elif query == "?total_revenue":
            print(get_total_revenue())
        elif query == "?revenue_of_shop":
            shop_id = parts[1]
            print(get_revenue_of_shop(shop_id))
        elif query == "?total_consume_of_customer_shop":
            customer_id = parts[1]
            shop_id = parts[2]
            print(get_total_consume_of_customer_shop(customer_id, shop_id))
        elif query == "?total_revenue_in_period":
            from_time = parts[1]
            to_time = parts[2]
            print(get_total_revenue_in_period(from_time, to_time))
        i += 1

if __name__ == "__main__":
    main()
