import torch

class SubmittedApp:
    def __init__(self):
        pass

    def run(input_tensor: torch.Tensor) -> torch.Tensor:
        """Main Run Method for scoring system
        :param input_tensor: (torch.Tensor) [batchsize, n_classes(3)]
        :return: (torch.Tensor) [batchsize, logit(3)]
        """
        return input_tensor

    def metric(self, inferred_tensor: torch.Tensor, ground_truth: torch.Tensor) -> torch.Tensor:
        """Classification Accuracy
        example)
        inferred_tensor: [[0,0,1], [0,1,0]]
        ground_truth: [3, 1]
        return: 0.5
        :param inferred_tensor: (torch.Tensor) [batch_size, n_classes(3)], inferred logits
        :param ground_truth:  (torch.LongTensor) [batch_size], ground truth labels
                                each consisting LongTensor ranging from 0 to 2
        :return: (torch.Tensor) metric 점수
        """

        inferred_tensor = torch.argmax(inferred_tensor, dim=-1)
        acc = torch.mean((inferred_tensor == ground_truth).to(torch.float), dim=-1)
        return acc
