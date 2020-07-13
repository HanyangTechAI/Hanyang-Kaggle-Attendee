import torch


class SubmittedApp:
    def __init__(self):
        pass

    def run(self, input_tensor: torch.Tensor) -> torch.Tensor:
        ''' Main run method for scoring system
        :param input_tensor: (torch.Tensor) [batchsize, channel(3), width, height]
        :return: (torch.Tensor) [batchsize, n_classes(10)]
        '''

        # You must write run method for predicting classes
        return input_tensor

    def metric(self, inferred_tensor: torch.Tensor, ground_truth: torch.Tensor) -> torch.Tensor:
        ''' Calculate accuracy
        example)
        inferred_tensor: [[0,0,1,0,0,0,0,0,0,0], [0,0,0,0,0,0,1,0,0,0]]
        ground_truth: [2, 5]
        return: 0.5

        because argmax inferred_tensor[0] is 2 and argmax inferred_tensor[1] is 6

        :param inferred_tensor: (torch.Tensor) [batch_size, n_classes(10)], inferred logits
        :param ground_truth: (torch.LongTensor) [batch_size], ground truth labels
                                each consisting LongTensor ranging from 0 to 9 (total 10 classes)
        :return: (torch.Tensor) metric score
        '''
        return torch.mean((inferred_tensor.argmax(dim=1) == ground_truth).float(), dim=-1)

