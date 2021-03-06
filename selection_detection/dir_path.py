# -*- coding: utf-8 -*-

from logging import getLogger
import os

logger = getLogger(__name__)

SRC_DIR_NAME = os.path.dirname(os.path.abspath(__file__))


def __join_and_makedirs(*keys):
    path_name = ''
    for key in keys:
        path_name = os.path.join(path_name, key)
    os.makedirs(path_name, exist_ok=True)
    print('define ' + path_name)
    return path_name


STORAGE_DIR_NAME = __join_and_makedirs(SRC_DIR_NAME, 'storage')
TASKS_DIR_NAME = __join_and_makedirs(SRC_DIR_NAME, 'tasks')
TESTS_DIR_NAME = __join_and_makedirs(SRC_DIR_NAME, 'tests')
CONFIG_DIR_NAME = __join_and_makedirs(SRC_DIR_NAME, 'config')
MODEL_DIR_NAME = __join_and_makedirs(SRC_DIR_NAME, 'model')
SANDBOX_DIR_NAME = __join_and_makedirs(SRC_DIR_NAME, 'sandbox')
CONTROLLERS_DIR_NAME = __join_and_makedirs(SRC_DIR_NAME, 'controllers')

# STORAGE
SAMPLE_IMG_DIR_NAME = __join_and_makedirs(STORAGE_DIR_NAME, 'sample_img')


def sample_img_path_name(num, status):
    return os.path.join(SAMPLE_IMG_DIR_NAME, str(num) + '-' + str(status) + '.png')


if __name__ == '__main__':
    pass
