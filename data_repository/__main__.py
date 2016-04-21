def run_rest_service():
    from .rest_service import RESTService
    rest = RESTService()
    rest.run()


def main():
    # Update configuration from local file
    from .configuration import Setting
    Setting.read_configuration_from_file()

    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor()
    pool.submit(run_rest_service)

if __name__ == '__main__':
    main()