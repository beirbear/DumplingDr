

class Setting(object):
    # REST Setting
    __com_addr = '130.238.29.141'
    __com_port = 8080

    # Mongodb Setting
    __db_connection_string = 'mongodb://130.238.29.141:27017/'
    __db_name = 'meta_stream'
    __table_name = 'meta_data'
    __table_tree_name = 'meta_tree'
    __table_tree_score_name = 'meta_tree_score'
    __dynamic_token = 'None'

    @staticmethod
    def read_configuration_from_file():
        with open('configuration.json','rt') as rt:
            s_from_file = eval(rt.read())
            if 'rest_addr' in s_from_file and \
               'rest_report' in s_from_file and \
               'mongodb_setting' in s_from_file and \
               'token' in s_from_file:
                if 'connection_string' in s_from_file['mongodb_setting'] and \
                   'db_name' in s_from_file['mongodb_setting'] and \
                   'db_features' in s_from_file['mongodb_setting'] and \
                   'db_tree' in s_from_file['mongodb_setting'] and \
                   'db_tree_score' in s_from_file['mongodb_setting']:

                    # Assign setting from file
                    try:
                        Setting.__com_addr = s_from_file['rest_addr']
                        Setting.__com_port = int(s_from_file['rest_port'])
                        Setting.__dynamic_token = s_from_file['token']
                        Setting.__db_connection_string = s_from_file['mongodb_setting']['connection_string']
                        Setting.__db_name = s_from_file['mongodb_setting']['db_name']
                        Setting.__table_name = s_from_file['mongodb_setting']['db_features']
                        Setting.__table_tree_name = s_from_file['mongodb_setting']['db_tree']
                        Setting.__table_tree_score_name = s_from_file['mongodb_setting']['db_tree_score']
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
    def get_table_name():
        return Setting.__table_name

    @staticmethod
    def get_db_connection_string():
        return Setting.__db_connection_string

    @staticmethod
    def get_token():
        return Setting.__dynamic_token


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

    class Feature(object):

        @staticmethod
        def get_string_feature():
            return 'features'

        @staticmethod
        def get_string_parameter():
            return 'parameters'

        @staticmethod
        def get_string_mapper_time():
            return 'time for mapper (s)'
