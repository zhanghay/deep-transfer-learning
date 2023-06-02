import torch
import torch.nn as nn
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from DSAN import DSAN
from data_loader import load_testing_other
from tqdm import tqdm

nclass = 12
root_path = '/home/hangyuan/nx/code/Pacs/PACS/'
dir = 'art_painting'
batch_size = 2
kwargs = {'num_workers': 1, 'pin_memory': True}

# 创建DSAN模型并移动到CUDA设备
# model = DSAN(num_classes=nclass).cuda()

# 加载模型权重
# model.load_state_dict(torch.load('model_visda.pkl'))
model = torch.load('model_PACS_c2p.pkl')
# 定义数据转换和加载测试集
# transform = transforms.Compose([
#    transforms.ToTensor(),
#    # 其他必要的转换
# ])

# test_dataset = datasets.ImageFolder('test_data_folder', transform=transform)
# test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
test_loader = load_testing_other(root_path=root_path, dir=dir, kwargs=kwargs, batch_size=batch_size)


# 定义评估函数
def evaluate(model, test_loader):
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in tqdm(test_loader):
            images = images.cuda()
            labels = labels.cuda()

            # 前向传播
            outputs = model.predict(images)

            # 获取预测结果
            _, predicted = torch.max(outputs.data, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    return accuracy


if __name__ == '__main__':
    accuracy = evaluate(model, test_loader)
    print('Test Accuracy: {:.2f}%'.format(accuracy))
