import matplotlib.pyplot as plt

fig,ax = plt.subplots()

fruits = ['Apple', 'Banana', 'Cherry', 'Orange']
counts=[10, 15, 7, 12]
bar_labels = ['red', 'yellow', 'pink', 'orange']
bar_colors = ['tab:red', 'yellow', 'tab:pink', 'tab:orange']

ax.bar(fruits, counts, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit Supply by Kind and Type')
ax.legend(title='Fruit Types')

plt.savefig('fruit_supply.png',bbox_inches='tight')

cat=['bored','happy','bored','bored','happy','happy']
dog=['happy','happy','happy','bored','bored','bored']
actions=['combing','drinking','feeding','napping','playing','walking']

fig,ax = plt.subplots()
ax.plot(actions,dog,label='dog')
ax.plot(actions,cat,label='cat')
ax.legend()

plt.savefig('lines.png',bbox_inches='tight')