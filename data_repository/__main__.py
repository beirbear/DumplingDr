def run_rest_service():
    from .rest_service import RESTService
    rest = RESTService()
    rest.run()


def main():
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor()
    pool.submit(run_rest_service)


if __name__ == '__main__':
    main()