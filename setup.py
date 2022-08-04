from setuptools import setup, find_packages
from os.path import dirname
from os.path import realpath
from os.path import join
import io


def open_config_file(*names, **kwargs):
    current_dir = dirname(realpath(__file__))
    return io.open(
        join(current_dir, *names),
        encoding=kwargs.get('encoding', 'utf8')
    )

install_dependencies = open_config_file('requirements.txt').read().splitlines()

setup(
    name='Translator',
    version='0.1.0',
    author='0xLucyfer',
    description='Will use google translate for en to es lists.',
    packages=find_packages(),
    install_requires=install_dependencies,
    entry_points={
        'console_scripts': [
            "run-csv = scripts.translator:translate_csv",
            "run-txt = scripts.translator:translate_txt",
            "animals = scripts.scrapers.animals:run_scraper",
            "clean = scripts.utils:normalize_file"
        ]
    }
)
