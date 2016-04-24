"""
Application entry point
"""


def run_rest_service():
    # This function is for running rest service
    from .rest_service import RESTService
    rest = RESTService()
    rest.run()


def main():
    # Update configuration from the local file
    from .configuration import Setting
    Setting.read_configuration_from_file()

    # Create a thread for running REST service
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor()
    pool.submit(run_rest_service)

if __name__ == '__main__':
    # Call the main flow of the program
    main()
