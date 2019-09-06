from setuptools import setup, find_packages

setup(
    name='find_zend_quotes',
    version = "1.0",
    setup_requires=["setuptools-git-version"],
    packages = find_packages(),
    description='',
    author='Yuri Mussi',
    author_email='ymussi@gmail.com',
    license='BSD',
    url='https://github.com/ymussi/find_zen_quotes',
    keywords = "Mussi",
    install_requires = ['gunicorn',
                        'sqlalchemy==1.2.18',
                        'flask >= 1.0.2',
                        'flask-restplus',
                        'configparser >= 3.5.0',
                        'requests >= 2.18.4',
                        'flask_cors',
                        'zen_quotes'],
    zip_safe=False
    ),