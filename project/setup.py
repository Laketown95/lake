from setuptools import setup

setup(
    name='flower_suggestion',
      version='1.0.0',
      description='Flower suggestion program',
      py_modules=['project'],
      entry_points= {
          'console_scripts': [
          'flower_sugesstion=project:main',
      ],
   },
)
