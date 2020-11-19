import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-rest-framework-jet",
    version="0.0.3",
    author="Francisco Rosal",
    author_email="ros18676@uvg.edu.gt",
    description="JET - Django APP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FR98/django-rest-framework-jet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content"
    ],
    install_requires=[
        'djangorestframework==3.11.0',
        'json-encrypted-token',
    ],
    python_requires='>=3.6',
)