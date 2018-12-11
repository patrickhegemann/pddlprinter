from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='pddlprinter',
      version='0.1',
      description='Convenient PDDL Problem Generation',
      keywords='ai planning pddl problem generation',
      url='http://github.com/patrickhegemann/pddlprinter',
      author='Patrick Hegemann',
      author_email='planning@mailbox.org',
      packages=['pddlprinter'],
      zip_safe=False,
      install_requires=['pytest'],
      classifiers=[
          "Programming Language :: Python :: 3"
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
          "Operating System :: OS Independent"
      ]
      )

