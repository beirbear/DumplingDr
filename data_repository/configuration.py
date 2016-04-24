import datetime


class Setting(object):
    # REST Setting
    __com_addr = '10.0.10.248'
    __com_port = 8080

    # Mongodb Setting
    __db_connection_string = 'mongodb://localhost:27017/'
    __db_name = 'meta_stream'
    __table_name = 'meta_data'
    __table_tree_name = 'meta_tree'
    __table_meta_name = 'meta_tree_score'
    __dynamic_token = 'None'
    __db_storage = ''

    @staticmethod
    def read_configuration_from_file():
        with open('configuration.json', 'rt') as rt:
            s_from_file = eval(rt.read())
            if 'rest_addr' in s_from_file and \
               'rest_port' in s_from_file and \
               'mongodb_setting' in s_from_file and \
               'token' in s_from_file:
                if 'connection_string' in s_from_file['mongodb_setting'] and \
                   'db_name' in s_from_file['mongodb_setting'] and \
                   'db_features' in s_from_file['mongodb_setting'] and \
                   'db_tree' in s_from_file['mongodb_setting'] and \
                   'db_meta' in s_from_file['mongodb_setting'] and \
                   'db_storage' in s_from_file['mongodb_setting']:

                    # Assign setting from file
                    try:
                        Setting.__com_addr = s_from_file['rest_addr']
                        Setting.__com_port = int(s_from_file['rest_port'])
                        Setting.__dynamic_token = s_from_file['token']
                        Setting.__db_connection_string = s_from_file['mongodb_setting']['connection_string']
                        Setting.__db_name = s_from_file['mongodb_setting']['db_name']
                        Setting.__table_name = s_from_file['mongodb_setting']['db_features']
                        Setting.__table_tree_name = s_from_file['mongodb_setting']['db_tree']
                        Setting.__table_meta_name = s_from_file['mongodb_setting']['db_meta']
                        Setting.__db_storage = s_from_file['mongodb_setting']['db_storage']

                    except Exception as e:
                        raise Exception("Error: " + e)
                else:
                    raise Exception("There are something wrong in setting in mongodb_setting in configuration.json")
            else:
                raise Exception("There are something wrong in parameter names in configuration.json");

    @staticmethod
    def get_com_addr():
        return Setting.__com_addr

    @staticmethod
    def get_com_port():
        return Setting.__com_port

    @staticmethod
    def get_database_name():
        return Setting.__db_name

    @staticmethod
    def get_string_table_feature():
        return Setting.__table_name

    @staticmethod
    def get_string_table_meta_name():
        return Setting.__table_meta_name

    @staticmethod
    def get_string_table_linkage_matrix():
        return Setting.__table_tree_name

    @staticmethod
    def get_db_connection_string():
        return Setting.__db_connection_string

    @staticmethod
    def get_token():
        return Setting.__dynamic_token

    @staticmethod
    def get_local_storage():
        return Setting.__db_storage


class Definitions(object):

    class Rest(object):

        @staticmethod
        def get_string_service_path():
            return 'dataRepository'

        @staticmethod
        def get_string_dump_features():
            return 'get_features'

        @staticmethod
        def get_string_count_features():
            return 'count'

        @staticmethod
        def get_string_req_command():
            return 'command'

        @staticmethod
        def get_string_request_token():
            return 'token'

        @staticmethod
        def get_string_id():
            return 'id'

        @staticmethod
        def get_string_realization():
            return 'realizations'

        @staticmethod
        def get_string_label():
            return 'label'

        @staticmethod
        def get_string_maker():
            return 'created_by'

    class DataLabels(object):

        @staticmethod
        def get_string_service_path():
            return 'dataLabels'

        @staticmethod
        def get_string_command():
            return 'command'

        @staticmethod
        def get_string_command_linkakge_m():
            return 'linkage_matrix'

        @staticmethod
        def get_string_command_tree():
            return 'labeled_tree'

        @staticmethod
        def get_string_command_row_idx():
            return 'row_index'

        @staticmethod
        def get_string_command_dump_meta():
            return 'meta_all'

    class Feature(object):

        @staticmethod
        def get_feature_name(_id):
            return str(_id) + '.p.zip'

        @staticmethod
        def get_string_feature():
            return 'features'

        @staticmethod
        def get_string_parameter():
            return 'parameters'

        @staticmethod
        def get_string_mapper_time():
            return 'time for mapper (s)'

    class MongoDB(object):

        class Features(object):
            @staticmethod
            def get_string_id():
                return 'id'

            @staticmethod
            def get_string_previous_id():
                return '_id'

            @staticmethod
            def get_string_feature_path():
                return 'feature_path'

            @staticmethod
            def get_string_realization_path():
                return 'realization_path'

            @staticmethod
            def get_string_created_by():
                return 'created_by'

            @staticmethod
            def get_string_created_date():
                return 'created_date'

            @staticmethod
            def get_string_is_labeled():
                return 'is_labeled'

            @staticmethod
            def get_string_is_enabled():
                return 'is_enabled'

            @staticmethod
            def get_dict_record(_id, prev_id, feature_path, realization_path, created_by, is_labeled):
                return {
                    Definitions.MongoDB.Features.get_string_id(): _id,
                    Definitions.MongoDB.Features.get_string_previous_id(): prev_id,
                    Definitions.MongoDB.Features.get_string_feature_path(): feature_path,
                    Definitions.MongoDB.Features.get_string_realization_path(): realization_path,
                    Definitions.MongoDB.Features.get_string_created_by(): created_by,
                    Definitions.MongoDB.Features.get_string_created_date(): datetime.datetime.now(),
                    Definitions.MongoDB.Features.get_string_is_labeled(): is_labeled,
                    Definitions.MongoDB.Features.get_string_is_enabled(): True
                }

        class LinkageMatrix(object):

            @staticmethod
            def get_string_left_child():
                return 'left_child'

            @staticmethod
            def get_string_right_child():
                return 'right_child'

            @staticmethod
            def get_string_proximity():
                return 'proximity'

            @staticmethod
            def get_string_num_of_nodes():
                return 'members_num'

        class Meta(object):
            @staticmethod
            def get_string_name():
                return 'name'

            @staticmethod
            def get_string_value():
                return 'value'

            @staticmethod
            def get_string_last_update():
                return 'last_update'
