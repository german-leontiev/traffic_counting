import os
from typing import Any

import argparse

from utilities.getter import *
from modules import CountingPipeline

parser = argparse.ArgumentParser(description='Perform Counting vehicles')
parser.add_argument('--weight', type=str, default=None, help='checkpoint of yolo')
parser.add_argument('--input_path', type=str, help='path to video to inference')
parser.add_argument('--output_path', type=str, help='path to save inferences video')
parser.add_argument('--gpus', type=str, default='0', help='number of GPU')
parser.add_argument('--debug', action='store_true', help='save detection at')
parser.add_argument('--mapping', default=None, help='Specify a class mapping if using pretrained')


def main(args: Any, model_params: object) -> None:
    """
    Function for run main pipeline
    Args:
        args: input parameters (weight, input_path, output_path, gpus, debug, mapping)
        model_params: class Config with yolo parameters (see configs.yaml)
    Returns: None
    """
    if os.path.isdir(args.input_path):
        if not os.path.exists(args.output_path):
            os.makedirs(args.output_path)

    cam_config = Config(os.path.join('configs', 'cam_configs.yaml'))
    pipeline = CountingPipeline(args, model_params, cam_config)
    pipeline.run()


if __name__ == '__main__':
    argum = parser.parse_args()
    config = Config(os.path.join('configs', 'configs.yaml'))

    main(argum, config)
