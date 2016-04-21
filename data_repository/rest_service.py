import falcon
from .configuration import Definitions as df, Setting


class DataObject(object):
    def __init__(self, meta_storage):
        self.__meta_storage = meta_storage

    def on_get(self, req, res):
        """
        GET: /dataRepository?token={None}
        GET: /dataRepository?token={None}&command={count}
        GET: /dataRepository?token={None}&command={get_features}

        """

        token_value = req.params[df.Rest.get_string_request_token()].strip()

        if token_value == Setting.get_token() and \
           df.Rest.get_string_req_command() not in req.params:
            res.body = str(self.__meta_storage.get_all_data())
            res.content_type = "String"
            res.status = falcon.HTTP_200

        elif df.Rest.get_string_req_command() in req.params and \
             req.params[df.Rest.get_string_req_command()] == df.Rest.get_string_count_features():

            # Count feature
            res.body = "Total records:" + str(self.__meta_storage.count_records())
            res.content_type = "String"
            res.status = falcon.HTTP_200

        elif df.Rest.get_string_req_command() in req.params and \
             req.params[df.Rest.get_string_req_command()] == df.Rest.get_string_dump_features():

            res.body = str(self.__meta_storage.get_all_features())
            res.content_type = "String"
            res.status = falcon.HTTP_200

        else:
            res.body = "Invalid token ID."
            res.content_type = "String"
            res.status = falcon.HTTP_401

    def on_post(self, req, res):
        """
        POST: /dataRepository?token={None}&id={data_id}&realization={path}&label={Undefined}
                &created_by={maker}
              Body = {Feature Content}
        """
        # parse the parameters
        token = req.params[df.Rest.get_string_request_token()].strip()
        realization = req.params[df.Rest.get_string_realization()].strip()
        _id = req.params[df.Rest.get_string_id()].strip()
        label = req.params[df.Rest.get_string_label()].strip()
        maker = req.params[df.Rest.get_string_maker()].strip()

        if token != Setting.get_token():
            res.body = "Invalid token ID."
            res.content_type = "String"
            res.status = falcon.HTTP_401

        elif not len(realization) and not len(_id) and not len(label) and not len(maker):
            res.body = "Incomplete data for some required parameters."
            res.content_type = "String"
            res.status = falcon.HTTP_400

        else:
            content = req.stream.read().decode('utf-8')
            if not len(content):
                res.body = "Feature content is required."
                res.content_type = "String"
                res.status = falcon.HTTP_400
            else:
                # Push data into database
                if self.__meta_storage.set_meta_by_key(_id,
                                                       content, # Features
                                                       realization,
                                                       label,
                                                       maker):
                    res.body = "Insert feature complete."
                    res.content_type = "String"
                    res.status = falcon.HTTP_200
                else:
                    res.body = "Insert feature error."
                    res.content_type = "String"
                    res.status = falcon.HTTP_429

    def on_put(self, req, res):
        raise Exception("Have not implemented yet!")

    def on_delete(self, req, res):
        """
        DELETE: /dataRepository?token={None}
        """
        token = req.params[df.Rest.get_string_request_token()].strip()
        if token != Setting.get_token():
            res.body = "Invalid token ID."
            res.content_type = "String"
            res.status = falcon.HTTP_401
        else:
            self.__meta_storage.drop_table()
            res.body = "Table has been dropped."
            res.content_type = "String"
            res.status = falcon.HTTP_200


class RESTService(object):
    def __init__(self):
        from wsgiref.simple_server import make_server
        from .configuration import Setting
        from .meta_storage import MetaStorage
        meta_storage = MetaStorage()
        api = falcon.API()
        api.add_route('/' + df.Rest.get_string_service_path(), DataObject(meta_storage))
        self.__server = make_server(Setting.get_com_addr(), Setting.get_com_port(), api)

    def run(self):
        print("Data Repository Service Enable")
        print("Ready.....\n\n")
        self.__server.serve_forever()