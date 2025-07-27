import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = r'c:\Users\gosc\Desktop\stolik\wyniki_230725\power_vs_position_mwcnt1_1_23072025.csv'

data = pd.read_csv(file)
df = pd.DataFrame(data)

P = df['Power [W]']
z = df['Position [mm]']

plt.plot(z, P, color='chocolate')
plt.xlabel('Pozycja [mm]')
plt.ylabel('Moc [W]')
plt.xlim(10,30)
plt.grid(linestyle='--')
plt.savefig('szkiełko.png')
plt.show()