from pymongo import MongoClient
from .configuration import Setting
from .configuration import Definitions


class MetaStorage(object):
    def __init__(self):
        self.__client = MongoClient(Setting.get_db_connection_string())
        self.__db = self.__client[Setting.get_database_name()]

    @property
    def total_keys(self):
        raise Exception("Have not implement exception")

    def set_meta_by_key(self, _id, prev_id, f_path, r_path, created_by, is_labeled):
        res = self.__db[Setting.get_table_name()].insert_one(
              Definitions.MongoDB.Features.get_dict_record(_id, prev_id, f_path, r_path, created_by, is_labeled))

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
