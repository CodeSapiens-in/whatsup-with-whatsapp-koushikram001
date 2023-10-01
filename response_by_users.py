import matplotlib.pyplot as plt

# Read data from the text file
with open('name_count.txt', 'r',encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

# Extract names and counts from the file
names = []
counts = []
for line in lines:
    name, count = line.strip().split(': ')
    names.append(name)
    counts.append(int(count))

# Create a bar chart
plt.figure(figsize=(10, 8))
plt.barh(names, counts, color='skyblue')
plt.xlabel('Count')
plt.title('Name Counts')
plt.gca().invert_yaxis()  # Invert the y-axis to display the names from top to bottom
plt.tight_layout()

# Show the chart
plt.show()

