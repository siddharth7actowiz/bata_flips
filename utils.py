import json
import gzip
import os
                                                                               

def read_html(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print("Error read_html:", e)

def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Error read_json:", e)
        return {}

def read_gzip(path):
    try:
        with gzip.open(path, "rt", encoding="utf-8") as f:
            for line in f:
                yield json.loads(line)
    except Exception as e:
        print("Error read_gzip:", e)




def load_files(data_dir, start, end):
    
    for file in files[start:end]:
        path = os.path.join(data_dir, file)
        try:
            with gzip.open(path, "rt", encoding="utf-8",errors="replace") as f: #decompress
                yield json.load(f)

        except Exception as e:
            print("Error in func:", load_files.__name__, e)                                                         
