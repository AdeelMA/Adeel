# %% [markdown]
# # Jupyternotebook in VS code
# This is much better than other jupyternotebook 

# %%
print("Python ka chilla with baba Aammar")

# %%
Adeel = "My name is Adeel"
Adeel

# %%
x = "What is your name"
x

# %%
import numpy as np
x = np.array([1,2,3,4,5,6,77,8])
x

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
phool = pd.read_csv("Iris.csv")

# %%
import pandas as pd
import matplotlib.pyplot as plt
phool = pd.read_csv("Iris.csv")

plt.plot(phool.Id, phool["SepalLengthCm"], "r--")
plt.show


# %%
import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)

# %%



