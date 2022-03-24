import matplotlib.pyplot as plt

from prochazka import np

fig, ax = plt.subplots(figsize=(15, 8))

im = ax.scatter(np.krokyX, np.krokyY, s=100, c=list(range(len(np.krokyY))), cmap="viridis")
fig.colorbar(im)
ax.plot(np.krokyX, np.krokyY, ls="--", c="k")
ax.scatter(np.krokyX[0], np.krokyY[0], s=800, c="red", label="start", edgecolors="k")
ax.scatter(np.krokyX[-1], np.krokyY[-1], s=800, c="orange", label="konec", edgecolors="k")

ax.set_title("Náhodná procházka", fontsize=50)
ax.legend()


plt.show()

