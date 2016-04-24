from pymongo import MongoClient
from .configuration import Setting
from .configuration import Definitions
import io
import tarfile
import datetime


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

        c = io.BytesIO()
        cursor = self.__db[Setting.get_table_name()].find()
        out = tarfile.open(fileobj=c, mode='w')

        for item in cursor:
            out.add(Setting.get_local_storage() + item[Definitions.MongoDB.Features.get_string_feature_path()])
        out.close()
        return c

    def get_all_data(self):
        cursor = self.__db[Setting.get_table_name()].find()
        return [item for item in cursor]

    def get_meta_from_key(self, object_id):
        raise Exception("Have not implement exception")

    def is_key_exist(self, object_id):
        raise Exception("Have not implement exception")

    def drop_table(self):
        self.__db[Setting.get_table_name()].drop()

    # -----------------------------------------
    def set_distance_matrix(self, content):
        res = self.__db[Setting.get_table_tree_name()].insert(content)

        if res.inserted_id:
            return True

        return False

    def set_labeled_tree(self, content):
        res = self.__db[Setting.get_table_meta_name()].insert_one({
            Definitions.MongoDB.Meta.get_string_name(): Definitions.DataLabels.get_string_command_tree(),
            Definitions.MongoDB.Meta.get_string_value(): content,
            Definitions.MongoDB.Meta.get_string_last_update(): datetime.datetime.now()})

        if res.inserted_id:
            return True

        return False

    def set_row_index(self, content):
        res = self.__db[Setting.get_table_meta_name()].insert_one({
            Definitions.MongoDB.Meta.get_string_name(): Definitions.DataLabels.get_string_command_row_idx(),
            Definitions.MongoDB.Meta.get_string_value(): content,
            Definitions.MongoDB.Meta.get_string_last_update(): datetime.datetime.now()})

        if res.inserted_id:
            return True

        return False
