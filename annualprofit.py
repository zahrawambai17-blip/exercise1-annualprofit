import pandas as pd
import matplotlib.pyplot as plt

sales_profit = pd.read_csv( "company_sales_data.csv")


plt.figure(figsize=(10, 6))
plt.plot(sales_profit["month_number"], sales_profit["total_profit"], color = "tab:blue", linewidth = 3)
plt.title("Annual company profit")
plt.xlabel("Month Number")
plt.ylabel( "Total Profit")
plt.xticks(sales_profit["month_number"])
plt.ylim(100000, 500000)
plt.yticks([100000, 200000, 300000, 400000, 500000])                                
plt.tight_layout()
plt.show()                                
