# python3



def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]

    for i in range(m):
        ti = data[i]
        start_time, thread_idx = threads[0]
        output.append((thread_idx, start_time))
        threads[0] = (start_time+ti, thread_idx)
        j = 0
        while True:
            left_child = 2*j + 1
            right_child = 2*j + 2
            if left_child >= n:
                break
            min_child = left_child
            if right_child < n and threads[right_child][0] < threads[left_child][0]:
                min_child = right_child
            if threads[min_child][0] < threads[j][0]:
                threads[j], threads[min_child] = threads[min_child], threads[j]
                j = min_child
            else:
                break

    return output


    def print_grid(grid):
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                print(i, j)
                print(grid[i][j])


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    
    # for thread_idx, start_time in result:
    #     print(thread_idx, start_time)
    print_grid(n, m, result)



if __name__ == "__main__":
    main()
