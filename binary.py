def binary_search(sorted_array, target):
    """
    Performs a Binary Search on a sorted list of student scores 
    to find the target score efficiently.
    """
    low = 0
    high = len(sorted_array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if sorted_array[mid] == target:
            return mid

        elif sorted_array[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
            
    return -1

def main():

    sorted_scores = [60, 70, 80, 85, 95]
    target_score = 80
    
    print("=== CAMPUS FAST GRADE LOOKUP (BINARY SEARCH) ===")
    print(f"Sorted Scores: {sorted_scores}")
    print(f"Searching for score: {target_score}")
    
    result_index = binary_search(sorted_scores, target_score)
    
    if result_index != -1:
        print(f"Success! Score {target_score} found at index position: {result_index}")
    else:
        print(f"Score {target_score} not found in the records.")

if __name__ == "__main__":
    main()

