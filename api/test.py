import pickle
import pandas as pd

if __name__ == '__main__':
    with open('../static/txt_file/1.txt', 'r', encoding='utf-8') as f:
        line = f.readlines()
    print(line)