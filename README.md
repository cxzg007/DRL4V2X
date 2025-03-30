# DRL4V2X
首先将资源分配问题建模为一个图，其中每条 V2V 链路被视为图中的一个节点。这种建模方法允许利用GNN来学习每个节点的低维特征，通过聚合邻居节点的信息，提取出能够代表链路特征的嵌入
向量。在此基础上，本文采用DRL进行频谱分配
