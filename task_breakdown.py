# -*- coding: utf-8 -*-
"""Task Breakdown

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sKidm82CYMbvfl7IHKMg98kTW3zFWqW0
"""

import matplotlib.pyplot as plt

# Data for Vendor Coordination Tasks
tasks = ['Engaged with Vendors', 'Designed Labels', 'Assured Quality', 'Managed Timelines', 'Assessed New Vendors', 'Consistency Checks']
timelines = [20, 15, 25, 15, 10, 15]

# Create the chart
plt.figure(figsize=(10, 6))
plt.barh(tasks, timelines, color='skyblue', edgecolor='black')
plt.title('Vendor Coordination Task Breakdown', fontsize=14)
plt.xlabel('Percentage Time Allocated (%)', fontsize=12)
plt.ylabel('Tasks', fontsize=12)
plt.tight_layout()

# Display the chart
plt.show()