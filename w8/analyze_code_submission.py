"""Data about submission of a programming contest consists a sequence of lines, each line has the following information:
                                                      <UserID> <ProblemID> <TimePoint> <Status> <Point>
in which the user <UserID> submits his/her code to solve the problem <ProblemID> at time-point <TimePoint>, and gets status <Status> and point <Point>
<UserID>: string of length from 3 to 10
<ProblemID>: string under the format Pxy where x, y are digits 0,1,...,9 (for example P03, P10)
<TimePoint>: string representing time-point with the format HH:MM:SS (for example, 09:45:20 means the time-point 9 hour 45 minutes 20 seconds)
<Status>: string with two cases (ERR, OK)
<Point>: integer from {0, 1, 2, ..., 10}

A user can submit the code for solving each problem several time. The point that the user gets for a problem is the maximal point among the submissions for that problem.

Perform a sequence of queries of following types:
?total_number_submissions: return the number of submissions of the contest
?number_error_submision: return the number of submissions having status ERR
?number_error_submision_of_user <UserID>: return the number of submission having status ERR of user <UserID>
?total_point_of_user <UserID>: return the total point of user <UserID>
?number_submission_period <from_time_point> <to_time_point>: return the number of submissions in the period from <from_time_point> to <to_time_point> (inclusive)

Input
The input consists of two blocks of data:
The first block is the operational data, which is a sequence of lines (number of lines can be up to 100000), each line contains the information of a submission with above format .The first block is terminated with a line containing the character #
The second block is the query block, which is a sequence of lines (number of lines can be up to 100000), each line is a query described above. The second block is terminated with a line containing the character #

Output
Write in each line, the result of the corresponding query
"""

import sys
from collections import defaultdict
from datetime import datetime
import bisect

class Submission:
    def __init__(self, user_id, problem_id, time_point, status, point):
        self.user_id = user_id
        self.problem_id = problem_id
        self.time_point = datetime.strptime(time_point, "%H:%M:%S")
        self.status = status
        self.point = point

submissions = []
user_error_count = defaultdict(int)
user_problem_max_points = defaultdict(lambda: defaultdict(int))
submission_times = []

def parse_submissions():
    for line in sys.stdin:
        if line.strip() == "#":
            break
        parts = line.split()
        submission = Submission(parts[0], parts[1], parts[2], parts[3], int(parts[4]))
        submissions.append(submission)
        submission_times.append(submission.time_point)
        if submission.status == "ERR":
            user_error_count[submission.user_id] += 1
        elif submission.status == "OK":
            user_problem_max_points[submission.user_id][submission.problem_id] = max(
                user_problem_max_points[submission.user_id][submission.problem_id], submission.point)
    submission_times.sort()

def total_number_submissions():
    return len(submissions)

def number_error_submissions():
    return sum(1 for s in submissions if s.status == "ERR")

def number_error_submissions_of_user(user_id):
    return user_error_count[user_id]

def total_point_of_user(user_id):
    return sum(points for points in user_problem_max_points[user_id].values())

def number_submission_period(from_time, to_time):
    from_time = datetime.strptime(from_time, "%H:%M:%S")
    to_time = datetime.strptime(to_time, "%H:%M:%S")
    start_idx = bisect.bisect_left(submission_times, from_time)
    end_idx = bisect.bisect_right(submission_times, to_time)
    return end_idx - start_idx

def process_queries():
    for line in sys.stdin:
        if line.strip() == "#":
            break
        parts = line.split()
        query = parts[0]
        if query == "?total_number_submissions":
            print(total_number_submissions())
        elif query == "?number_error_submision":
            print(number_error_submissions())
        elif query == "?number_error_submision_of_user":
            user_id = parts[1]
            print(number_error_submissions_of_user(user_id))
        elif query == "?total_point_of_user":
            user_id = parts[1]
            print(total_point_of_user(user_id))
        elif query == "?number_submission_period":
            from_time = parts[1]
            to_time = parts[2]
            print(number_submission_period(from_time, to_time))

if __name__ == "__main__":
    parse_submissions()
    process_queries()
