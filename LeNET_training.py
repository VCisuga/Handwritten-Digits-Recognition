# author: baiCai
# 导包
import time
import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
import torchvision.transforms as transforms
from torchvision.models import AlexNet


# 创建模型
class LeNet(nn.Module):
    def __init__(self):
        super(LeNet,self).__init__()
        # Comment:  # 定义模型的特征提取层
        self.features = nn.Sequential(
            nn.Conv2d(in_channels=1,out_channels=6,kernel_size=(5,5),stride=1,padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2,stride=2), # 输出是: 5 * 5 * 6
            nn.Conv2d(in_channels=6,out_channels=16,kernel_size=(5,5),stride=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2,stride=2), # 输出是: 5 * 5 * 16
        )
        self.classifier = nn.Sequential(
            # FC1层：输入为5*5*16=400
            nn.Linear(in_features=400, out_features=120),
            nn.ReLU(),# 输出是: 120 * 1
            nn.Linear(in_features=120, out_features=84),
            nn.ReLU(),# 输出是: 84 * 1
            nn.Linear(in_features=84, out_features=10)# 输出是: 10 * 1
        )

    def forward(self,x):
        # 定义了：前向传播函数
        x = self.features(x) # 将输入张量x通过特征提取层，得到特征表示
        x = torch.flatten(x,1)
        result = self.classifier(x)
        return result


if __name__ == '__main__':
    # Comment: 下载MNIST数据集
    train_dataset = MNIST(root='./data/',train=True,transform=transforms.ToTensor(),download=True)
    test_dataset = MNIST(root='./data/',train=False,transform=transforms.ToTensor())
    # Comment: 分批次加载数据，每批32个数据
    batch_size = 32
    train_loader = DataLoader(dataset=train_dataset,batch_size=batch_size,shuffle=True)
    test_loader = DataLoader(dataset=test_dataset,batch_size=batch_size,shuffle=False)
    # start time
    start_time = time.time()
    # Comment: 初始化一个神经网络模型
    model = LeNet()
    
    # Comment: 定义损失函数
    loss_func = nn.CrossEntropyLoss()
    loss_list = [] # 存储损失值
    # Comment: 定义优化器
    SGD = optim.SGD(params=model.parameters(),lr=0.001,momentum=0.9)
    # Comment: 定义学习率
    LR = 10

    for i in range(LR):
        loss_temp = 0 # Comment: 损失值
        # Comment: j-迭代次数，batch_data、batch_label-批量的，每批32个数据
        for j,(batch_data,batch_label) in enumerate(train_loader):
            # Comment: 梯度清空
            SGD.zero_grad()
            # Comment: 训练模型
            prediction = model(batch_data)
            # Comment: 计算损失值
            loss = loss_func(prediction,batch_label)
            loss_temp += loss
            # Comment: 先使用loss.backward()计算梯度，然后使用SGD.step()等更新模型参数。
            loss.backward()
            # Comment: 根据计算出的梯度，更新模型的参数
            SGD.step()
            if (j + 1) % 200 == 0:
                print('第%d次训练，第%d批次，损失值: %.3f' % (i + 1, j + 1, loss_temp / 200))
                loss_temp = 0
    # end_time
    end_time = time.time()
    print('训练花了: %d s' % int((end_time-start_time)))

    correct = 0
    # Comment: 初始化正确计数器为0
    for batch_data,batch_label in test_loader:
        prediction = model(batch_data)
        # Comment: 使用torch.max函数获取预测结果中的最大值及其对应的索引
        predicted = torch.max(prediction.data, 1)[1]
        # Comment: 将预测结果与真实标签进行比较，得出当前预测正确的样本数
        correct += (predicted == batch_label).sum()
    print('准确率: %.2f %%' % (100 * correct / 10000))

    # Comment: 取名并保存权重模型
    model_name = input('> ')
    torch.save(model.state_dict(), './' + model_name + '.pth')
