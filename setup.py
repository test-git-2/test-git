from setuptools import setup, find_packages

setup(
    name="resampling",
    version='v0.0.16',
    author="victor993",
    author_email="v.hernandez@cgiar.com",
    description="ORM para la base de datos de gap analysis",
    url="https://github.com/test-git-2/test-git",
    download_url="https://github.com/test-git-2/test-git",
    packages=find_packages('src'),
    package_dir={'':'src'},
    keywords='mongodb orm gap-analysis',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "mongoengine"
    ],
    entry_points={
        'console_scripts': [
            'resampling=resampling.scripts.resampling:main',
        ],
    },
)
