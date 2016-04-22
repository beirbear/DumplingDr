from pymongo import MongoClient
from .configuration import Setting
from datetime import datetime


class MetaStorage(object):
    def __init__(self):
        self.__client = MongoClient(Setting.get_db_connection_string())
        self.__db = self.__client[Setting.get_database_name()]

    @property
    def total_keys(self):
        raise Exception("Have not implement exception")

    def set_meta_by_key(self, object_id, realization_features, realization_path, realization_label, created_by):
        res = self.__db[Setting.get_table_name()].insert_one({
            "id": object_id,
            "features": realization_features,
            "realizations": realization_path,
            "label": realization_label,
            "created_by": created_by,
            "created_time": datetime.now(),
            "last_updated": datetime.now(),
            "is_enable": True
        })

        if res.inserted_id:
            return True

        return False

    def count_records(self):
        return self.__db[Setting.get_table_name()].count()

    def get_all_features(self):
        cursor = self.__db[Setting.get_table_name()].find()
        out = {}
        for item in cursor:
            out[int(item['id'])] = item['features']
        return out
        # return [(item['id'], item['features']) for item in cursor]

    def get_all_data(self):
        cursor = self.__db[Setting.get_table_name()].find()
        return [item for item in cursor]

    def get_meta_from_key(self, object_id):
        raise Exception("Have not implement exception")

    def is_key_exist(self, object_id):
        raise Exception("Have not implement exception")

    def drop_table(self):
        self.__db[Setting.get_table_name()].drop()
