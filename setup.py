from setuptools import setup, find_packages

setup(
    name='mkdocs-umbrella-specs-plugin',
    version='0.0.1',
    description='An MkDocs plugin',
    long_description='',
    keywords='mkdocs',
    url= '',
    author='Loomeijer, E.',
    author_email='e.loomeijer@tue.nl',
    license='MIT',
    python_requires='>=3.10',
    install_requires=[
        'mkdocs>=1.0.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'umbrella-specs = src.plugins.specs.plugin:SpecsPlugin',
        ]
    }
)