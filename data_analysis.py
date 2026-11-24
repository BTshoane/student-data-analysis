print("PROGRAM IS RUNNING")

import pandas as pd 

print("=== STUDENT DATA ANALYSIS SYSTEM ===")

try:
    # Load data 
    data = pd.read_excel("students.xlsx")

    print("\nLoaded Data:")
    print(data)

    # Clean data
    data = data.dropna()
    data["Marks"] = pd.to_numeric(data["Marks"], errors='coerce')
    data = data.dropna()

    #Calculations
    average = data["Marks"].mean()
    highest = data["Marks"].max()
    lowest = data["Marks"].min()

    #Pass rate
    passed = data[data["Marks"] >= 50]
    pass_rate = (len(passed) / len(data)) * 100

    print("\n=== RESULTS ====")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Pass Rate: {pass_rate:.2f}%")

    # Add performance categories
    def get_grade(mark) : 
        if mark >= 75:
            return "Distinction"
        elif mark >= 50:
            return "Pass"
        else:
            return "Fail"
        
    data["Grade"] = data["Marks"].apply(get_grade)

    print("\n=== STUDENT GRADES ===")
    print(data) 

    # Count categories
    grade_counts = data["Grade"].value_counts()

    print("\n=== GRADE SUMMARY ===") 
    print(grade_counts)

    # Save report
    with open("report.txt", "w") as file:
        file.write("STUDENT REPORT\n")
        file.write(f"Average: {average}\n")
        file.write(f"Highest: {highest}\n")
        file.write(f"Lowest: {lowest}\n")
        file.write(f"Pass Rate: {pass_rate}%\n")
        
    print("\nReport saved as report.txt")

except FileNotFoundError: 
    print("Error: students.xlsx file not found.")

import matplotlib.pyplot as plt 

# Create bar chart
plt.bar(data["Name"], data["Marks"])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Save graph as image FIRST
plt.savefig("marks_chart.png")

# THEN show it 
plt.show()




      


