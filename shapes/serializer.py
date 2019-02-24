import pickle
import os


class Serializer:
    """our class to work with write/read data"""
    def __init__(self, dir_path, shapes):
        if not os.path.exists(dir_path):
            raise Exception('Path does not exist')
        if not os.path.isdir(dir_path):
            raise Exception('Path is not dir')
        self.dir_path = dir_path
        self.shapes = shapes

    def store(self):
        """this is our function to store date in files"""
        for idx, shape in enumerate(self.shapes):
            file_name = self.generate_file_name(shape, idx)
            serialized_shape = pickle.dumps(shape)
            full_path = os.path.join(self.dir_path, file_name)
            with open(full_path, 'wb') as f:
                f.write(serialized_shape)

    def generate_file_name(self, shape, idx):
        class_name = type(shape).__name__
        file_name = f'{class_name}_{idx}.pickle'
        return file_name

    def restore(self):
        """this is our function to restore date in files"""
        result = []
        for file_name in os.listdir(self.dir_path):
            full_path = os.path.join(self.dir_path, file_name)
            if not os.path.isfile(full_path):
                continue
            with open(full_path, 'rb') as f:
                shape_bytes = f.read()
            shape = pickle.loads(shape_bytes)
            result.append(shape)
            print(result)
        return result
