import torch


class SubmittedApp:
    def __init__(self):
        pass

    def run(input_tensor: torch.Tensor) -> torch.Tensor:
        """Main Run Method for scoring system
        :param input_tensor: (torch.Tensor)
            [batchsize, channel(3), width, height]
        :return: (torch.Tensor)
            [batchsize, channel(3), width, height]
        """
        return input_tensor

    def metric(self, inferred_tensor: torch.Tensor, ground_truth: torch.Tensor) -> torch.Tensor:
        """Metric Method for students to test on
        :param inferred_tensor: (torch.Tensor)
            문제 출제자들은 inferred_tensor shape 을 작성해줄것
        :param ground_truth:  (torch.Tensor)
            문제 출제자들은 output_tensor shape 을 작성해줄것
        :return: (torch.Tensor) metric 점수
        """
        # 출제자들은 메트릭을 작성해주시기 바랍니다
        raise NotImplementedError
