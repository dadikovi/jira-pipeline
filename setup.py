#!/usr/bin/env python

"""
Jira-Pipeline issue export-import tool
"""

from setuptools import setup

__author__ = 'Dávid Kovács'
__author_email__ = 'dadikovi@gmail.com'
__copyright__ = 'dadikovi.github.io'
__version__ = '1.0'
__maintainer__ = __author__
__status__ = 'Development'

setup(name='jira_pipeline',
      version=__version__,
      description='Jira-Pipeline issue export-import tool',
      author=__author__,
      license='http://www.apache.org/licenses/LICENSE-2.0',
      url=__copyright__,
      packages=['jira_pipeline'],
      package_dir={'jira_pipeline': 'src/jira-pipeline'},
      install_requires=['briefly>=1.0', 'jira>=2.0.0'],
      dependency_links=['git+https://github.com/bloomreach/briefly.git@1.0#egg=briefly-1.0','git+https://github.com/pycontribs/jira.git@2.0.0#egg=jira-2.0.0']
     )
