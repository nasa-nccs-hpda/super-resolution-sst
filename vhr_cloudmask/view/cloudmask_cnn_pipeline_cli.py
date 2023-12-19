import sys
import time
import logging
import argparse
from tensorflow_caney.model.pipelines.cnn_segmentation import \
    CNNSegmentation as CloudMaskPipeline


# -----------------------------------------------------------------------------
# main
#
# python cloudmask_pipeline_cli.py -c config.yaml -d config.csv -s preprocess
# -----------------------------------------------------------------------------
def main():

    # Process command-line args.
    desc = 'Use this application to perform CNN segmentation.'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-c',
                        '--config-file',
                        type=str,
                        required=False,
                        dest='config_file',
                        help='Path to the configuration file')

    parser.add_argument('-d',
                        '--data-csv',
                        type=str,
                        required=False,
                        dest='data_csv',
                        help='Path to the data configuration file')

    parser.add_argument('-s',
                        '--step',
                        type=str,
                        nargs='*',
                        required=True,
                        dest='pipeline_step',
                        help='Pipeline step to perform',
                        default=['preprocess', 'train', 'predict'],
                        choices=['preprocess', 'train', 'predict'])

    parser.add_argument('-m',
                        '--model-filename',
                        type=str,
                        required=False,
                        dest='model_filename',
                        help='Path to model file')

    parser.add_argument('-o',
                        '--output-dir',
                        type=str,
                        required=False,
                        dest='output_dir',
                        help='Path to output directory')

    args = parser.parse_args()

    # Setup timer to monitor script execution time
    timer = time.time()

    # Initialize pipeline object
    pipeline = CloudMaskPipeline(args.config_file, args.data_csv)

    # Regression CHM pipeline steps
    if "preprocess" in args.pipeline_step:
        pipeline.preprocess()
    if "train" in args.pipeline_step:
        pipeline.train()
    if "predict" in args.pipeline_step:
        pipeline.predict()

    logging.info(f'Took {(time.time()-timer)/60.0:.2f} min.')


# -----------------------------------------------------------------------------
# Invoke the main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())