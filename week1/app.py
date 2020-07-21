import torch

class SubmittedApp:
    def __init__(self):
        pass

    def run(input_tensor: torch.Tensor) -> torch.Tensor:
        """Main Run Method for scoring system
        :param input_tensor: (torch.Tensor) [batchsize, height(1)]
        :return: (torch.Tensor) [batchsize, weight(1)]
        """
        return input_tensor

    def metric(self, inferred_tensor: torch.Tensor, ground_truth: torch.Tensor) -> torch.Tensor:
        """Mean Square Error
        l(y, y') = (y - y')^2        
        :param inferred_tensor: (torch.Tensor) [batch_size, weight(1)], inferred value
        :param ground_truth:  (torch.FloatTensor) [batch_size, weight(1)], ground truth value
        :return: (torch.Tensor) metric 점수
        """

        return torch.mean((inferred_tensor - ground_truth)**2)

