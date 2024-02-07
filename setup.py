import setuptools

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='querySDSS',
    version=find_version('querySDSS.py'),
    description='Query for SDSS datarelease 18',
    long_description=long_description,
)

setuptools.setup(
    name='querySDSS',
    version='1.7',
    license='MIT',
    author="aCosmicDebbuger",
    author_email='acosmicdebugger@gmail.com',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/aCosmicDebugger/querySDSS',
    keywords='example project',
    install_requires=[
          'astropy', 'astroquery',
      ],

)
