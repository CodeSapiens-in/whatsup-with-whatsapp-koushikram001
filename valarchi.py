import matplotlib.pyplot as plt
from datetime import datetime

# Initialize variables
timestamps = []
users = set()
active_users = []

# Read the chat log from the '_chat.txt' file
with open('_chat.txt', 'r', encoding='utf-8') as file:
    chat_log = file.readlines()

# Parse the chat log
for line in chat_log:
    parts = line.split('] ')
    if len(parts) >= 2:
        timestamp_str = parts[0][1:]
        username = parts[1].split(':')[0]
        
        try:
            timestamp = datetime.strptime(timestamp_str, "%d/%m/%y, %I:%M:%S %p")
            
            # Append data to lists
            timestamps.append(timestamp)
            users.add(username)
        except ValueError:
            # Skip lines with incorrect date format
            pass

# Create a list of all unique timestamps
unique_timestamps = sorted(set(timestamps))

# Fill in the gaps in the active_users list
for timestamp in unique_timestamps:
    active_users.append(len([t for t in timestamps if t <= timestamp]))

# Create the graph
plt.figure(figsize=(10, 5))
plt.plot(unique_timestamps, active_users, marker='o', linestyle='-')
plt.xlabel('Time')
plt.ylabel('Active responses')
plt.title('Active Users Over Time')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the graph
plt.show()
