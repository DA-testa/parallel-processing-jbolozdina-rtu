# python3



def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]

    for i in range(m):
        next_thread = min(threads)
        threads[next_thread[1]] = (next_thread[0] + data[i], next_thread[1])
        output.append((next_thread[1], next_thread[0]))

    return output



def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for i in range(m):
        print(result[i][0], result[i][1])



if __name__ == "__main__":
    main()
