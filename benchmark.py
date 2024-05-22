import time

def measure_processing_speed():
    start_time = time.time()
    
    # Perform a large number of additions
    iterations = 1000000
    for _ in range(iterations):
        _ = 1 + 1
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    processing_speed = iterations / elapsed_time  # Operations per second
    return processing_speed

def main():
    processing_speed = measure_processing_speed()
    print("Processing speed:", processing_speed, "operations per second")

if __name__ == "__main__":
    main()