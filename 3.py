# A class to represent a job
class Job:
    def __init__(self, id, dead, profit):
        self.id = id  # Job Id
        self.dead = dead  # Deadline of job
        self.profit = profit  # Profit if job is over before or on deadline

# Returns maximum profit from jobs
def print_job_scheduling(arr, n):
    # Sort jobs based on their profits in descending order
    arr.sort(key=lambda x: x.profit, reverse=True)

    # Initialize result array and slots array
    result = [-1] * n
    slot = [False] * n

    # Iterate over each job
    for i in range(n):
        # Find a free slot for this job (start from the last possible slot)
        for j in range(min(n, arr[i].dead) - 1, -1, -1):
            if not slot[j]:
                result[j] = i
                slot[j] = True
                break

    # Print the job ids that are scheduled
    print("Following is the maximum profit sequence of jobs:")
    for i in range(n):
        if slot[i]:
            print(arr[result[i]].id, end=" ")


# Driver code
if __name__ == "__main__":
    # JobId, Deadline, Profit
    arr = [
        Job('a', 2, 100),
        Job('b', 1, 19),
        Job('c', 2, 27),
        Job('d', 1, 25),
        Job('e', 3, 15)
    ]

    n = len(arr)
    print_job_scheduling(arr, n)
