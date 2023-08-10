import numpy as np
import matplotlib.pyplot as plt

def perform_complex_calculation(data):
    """
    Perform a complex scientific calculation on the input data.
    """
    return np.exp(np.sin(data) ** 2) / (np.log10(data + 1) + np.sqrt(np.cos(data) ** 3))

def analyze_results(result):
    """
    Analyze the results of the complex calculation.
    """
    mean_result = np.mean(result)
    max_result = np.max(result)
    min_result = np.min(result)
    std_result = np.std(result)
    return mean_result, max_result, min_result, std_result

def plot_histogram(result):
    """
    Display a histogram of the calculation results.
    """
    plt.hist(result, bins=100, color='skyblue')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Distribution of Complex Calculation Results')
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to generate data, perform calculation, analyze results, and visualize.
    """
    try:
        data = np.random.rand(1000000)
        result = perform_complex_calculation(data)
        mean_result, max_result, min_result, std_result = analyze_results(result)
        
        plot_histogram(result)
        
        print("Mean:", mean_result)
        print("Max:", max_result)
        print("Min:", min_result)
        print("Standard Deviation:", std_result)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
