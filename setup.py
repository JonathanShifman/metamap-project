import pip


def install_package(package_name):
    pip.main(['install', package_name])


install_package('configparser')
