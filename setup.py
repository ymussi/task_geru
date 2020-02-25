from setuptools import setup, find_packages

# install requirements of the project
with open("requirements.txt") as req:
    install_requires = req.read()

setup(
    name='find_zend_quotes',
    version = "1.0",
    # setup_requires=["setuptools-git-version"],
    packages = find_packages(),
    description='',
    author='Yuri Mussi',
    author_email='ymussi@gmail.com',
    license='BSD',
    url='https://github.com/ymussi/find_zen_quotes',
    keywords = "Mussi",
    zip_safe=False
    ), 