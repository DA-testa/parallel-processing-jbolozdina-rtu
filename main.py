# python3



def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    threads.sort()

    for i in range(m):
        ti = data[i]
        start_time, thread_idx = threads[0]
        output.append((thread_idx, start_time))
        threads[0] = (start_time+ti, thread_idx)
        for j in range(0, n//2):
            left_child = 2*j + 1
            right_child = 2*j + 2
            min_child = left_child
            if right_child < n and threads[right_child][0] < threads[left_child][0]:
                min_child = right_child
            if threads[min_child][0] < threads[j][0]:
                threads[j], threads[min_child] = threads[min_child], threads[j]
            else:
                break
                
    return output



def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread_idx, start_time in result:
        print(thread_idx, start_time)



if __name__ == "__main__":
    main()
