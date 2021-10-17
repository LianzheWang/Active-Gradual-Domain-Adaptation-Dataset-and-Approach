import torch

def evaluate(model, dloader, device):
    """
    Evaluate the performance of "model" on the the given dataloader. 
    return acc & loss
    """
    num_correct = 0
    num_total = 0
    total_loss = 0
    with torch.no_grad():
        #for i, (x, y, idx) in enumerate(dloader):
        for i, (x, y) in enumerate(dloader):
            x = x.to(device)
            y = y.to(device)
            model.eval()
            yhat = model(x)
            total_loss += F.cross_entropy(yhat, y)
            num_correct += (yhat.argmax(dim=1) == y).sum().item()
            num_total += x.size(0)
        loss = total_loss / len(dloader)
        acc = num_correct / num_total
    return acc, loss

def evaluate_(model, dloader, device):
    """
    Evaluate the performance of "model" on the the given dataloader. 
    only acc is returned.
    """
    num_correct = 0
    num_total = 0
    with torch.no_grad():
        for i, (x, y) in enumerate(dloader):
            x = x.to(device)
            y = y.to(device)
            model.eval()
            yhat = model(x)
            num_correct += (yhat.argmax(dim=1) == y).sum().item()
            num_total += x.size(0)
        acc = num_correct / num_total
    return acc

def evaluate_per_class(model, dloader, device, num_classes = 10):
    """
    Evaluate the performance of "model" on the given dataloader.
    return: a list with per class accuracy.
    """
    num_correct = [0] * num_classes
    num_total = [0] * num_classes
    acc_list = [1] * num_classes
    with torch.no_grad():
        for i, (x, y) in enumerate(dloader):
            x = x.to(device)
            y = y.to(device)
            model.eval()
            yhat = model(x)

            for j in range(len(y)):
                num_correct[y[j]] += (yhat[j].argmax(dim=0) == y[j]).sum().item()
                num_total[y[j]] += 1
                
        for i in range(num_classes):
            if num_total[i] > 0:
                acc_list[i] = num_correct[i] / num_total[i]
    return acc_list

def binary_accuracy(a,b):
    """
    Calculate the binary acc.
    """
    return ((a.argmax(dim=1) == b).sum().item()) / a.size(0)