import torch
import image_preprocess as PRE
from model_training import net
from LeNET_training import LeNet


def NumberOCR(image_dir, model):
    # Comment: 加载指定模型
    if model == 'LeNet':
        handwriting_net = LeNet()
        handwriting_net.load_state_dict(torch.load('model.pth')) # 请按照自己保存的神经网络变更模型名称
        handwriting_net.eval() # 设置模型为评估模式
    else:
        handwriting_net = net()
        handwriting_net.load_state_dict(torch.load('handwriting_reco_lr0p1to0p01.pth'))
        handwriting_net.eval()

    # Comment:  对输入的图片进行预处理
    img = PRE.image_preprocessing(image_dir, model)

    # Comment: 将预处理后的图片转换为模型的输入形状
    if model == 'LeNet':
        inputs = img.reshape(-1, 1, 28, 28)
    else:
        inputs = img.reshape(-1, 784)

    # Comment: 将inputs数据类型转换为 float
    inputs = torch.from_numpy(inputs)
    inputs = inputs.float()

    # Comment: 输入图片数据，进行推断得到预测结果
    predict = handwriting_net(inputs)
    print(predict)

    # Comment: 输出图片识别结果
    endstr = "The number in this picture is {}".format(torch.argmax(predict).detach().numpy())
    print(endstr)

    return endstr


# if __name__ == '__main__':
#     try:
#         res = NumberOCR('./image_archive/26.bmp', 'LeNet')
#     except Exception as e:
#         print(e)