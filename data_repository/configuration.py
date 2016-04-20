class Setting:
    __com_addr = 'localhost'
    __com_port = 8100
    __db_name = 'meta_stream'
    __table_name = 'meta_data'
    __db_connection_string = 'mongodb://localhost:27017/'
    __dynamic_token = "None"

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

    __service_path = 'dataRepository'

    @staticmethod
    def get_string_service_path():
        return Setting.__service_path


class Definitions:
    __command_dump_features = 'get_features'
    __command_count_features = 'count'
    __command = 'command'
    __token = 'token'
    __id = 'id'
    __realization = 'realizations'
    __label = 'label'
    __created_by = 'created_by'

    @staticmethod
    def get_string_dump_features():
        return Definitions.__command_dump_features

    @staticmethod
    def get_string_count_features():
        return Definitions.__command_count_features

    @staticmethod
    def get_string_req_command():
        return Definitions.__command

    @staticmethod
    def get_string_request_token():
        return Definitions.__token

    @staticmethod
    def get_string_id():
        return Definitions.__id

    @staticmethod
    def get_string_realization():
        return Definitions.__realization

    @staticmethod
    def get_string_label():
        return Definitions.__label

    @staticmethod
    def get_string_maker():
        return Definitions.__created_by

    class Feature:
        __feature = 'features'
        __parameter = 'parameters'
        __time_for_mapper = 'time for mapper (s)'

        @staticmethod
        def get_string_feature():
            return Definitions.Feature.__feature

        @staticmethod
        def get_string_parameter():
            return Definitions.Feature.__parameter

        @staticmethod
        def get_string_mapper_time():
            return Definitions.Feature.__time_for_mapper