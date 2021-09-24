#!python

import os.path, sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

try:
    import pytest
except ImportError:
    pytest = None

sys.path.insert(0, os.path.abspath("src"))
from whoosh import versionstring


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)


if __name__ == "__main__":
    setup(
        name="whooshy",
        version=versionstring(),
        package_dir={'': 'src'},
        packages=find_packages("src"),

        author="Matt Chaput & Marcos Pontes",
        author_email="mfprezende@gmail.com",

        description="Fast, pure-Python full text indexing, search, and spell checking library.",
        long_description="Fork of Whoosh library",

        license="Two-clause BSD license",
        keywords="index search text spell",
        url="http://github.com/matchup-ir/whooshy",

        zip_safe=True,
        install_requires=['cached-property'],
        tests_require=['pytest'],
        cmdclass={'test': PyTest},

        classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Indexing",
        ],
    )
