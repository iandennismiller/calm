from setuptools import setup

setup(
    version='0.1.0',
    name='calm',
    description="A peaceful user experience for Language Models",
    packages=[
        'calm',
    ],
    scripts=[
        'scripts/calm'
    ],
    include_package_data=True,
    keywords='',
    author='Ian Dennis Miller',
    author_email='ian@iandennismiller.com',
    url='https://github.com/iandennismiller/calm',
    install_requires=[
        "python-dotenv",
        "click",
        "pyyaml",
        "rich",
        "psutil",
        "requests",
        "redis",
        "redis-om",
        "guidance",
        "chromadb",
        "llama-cpp-python[server]",
        "llama-cpp-guidance",
        "sentence_transformers",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pdbpp",
            "mypy",
            "pylint",
            "ipython",
        ],
        "docs": [
            "sphinx",
            "sphinx_rtd_theme",
        ]
    },
    license='MIT',
    zip_safe=False,
)
