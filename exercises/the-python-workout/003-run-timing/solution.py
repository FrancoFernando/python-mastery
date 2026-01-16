def run_timing():

    total_time, runs = 0, 0

    # walrus operator replace while True followed by if not data_point check
    while data_point := input("Enter 10 km run time (minutes):"):

        total_time += float(data_point)
        runs += 1

    average = total_time / runs
    print(f"Average of {average}, over {runs} runs")

run_timing()

