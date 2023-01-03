from dataclasses import dataclass, field

@dataclass
class CaptionArguments:
    """
    自定义的一些参数
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune from.
    """
    max_seq_length: int = field(metadata={"help": "输入最大长度"})
    train_caption_file: str = field(metadata={"help": "训练集"})
    train_image_file: str = field(metadata={"help": "训练集"})
    test_caption_file: str = field(metadata={"help": "测试集"})
    test_image_file: str = field(metadata={"help": "测试集"})
    model_name_or_path: str = field(metadata={"help": "预训练权重路径"})
    freeze_encoder: bool = field(metadata={"help": "是否将encoder的权重冻结，仅对decoder进行finetune"})

