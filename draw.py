import networkx as nx
import matplotlib.pyplot as plt


#意见领袖可视化


G = nx.Graph()

with open('/home/ljx/Ljx/PeopleWeb/ToupleGDD _Final/test_data/Wiki-2.txt', 'r') as file:
    for line in file:
        u, v = map(int, line.strip().split())
        G.add_edge(u, v)

# 创建一个与节点数相同的颜色列表
node_colors = ['blue'] * G.number_of_nodes()
node_sizes = [0.1] * G.number_of_nodes()

all_degrees = dict(nx.degree(G))
degree = [(stu_value, stu_key) for stu_key, stu_value in all_degrees.items()]
degree=sorted(degree,reverse=True)[:10]
for i in degree:
    print('index:',i[1],'count:',i[0])


#模型输出的一组节点
# result=[142, 72, 564, 984, 114]

result=[408, 699, 2013, 2374, 286]
# 将节点 2 和节点 3 的颜色设置为红色
for i in result:
    node_colors[i] = 'red'
    node_sizes[i] = 50


# 绘制图形
# pos = nx.spring_layout(G)  # 选择布局
nx.draw(G,  node_color=node_colors, node_size=node_sizes,width=0.2)

# 显示图形

plt.savefig("graph01.pdf")
plt.show()