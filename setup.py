from setuptools import setup

with open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="bakalari-token",
    version="1.0",
    url="https://github.com/bakalari-api/python-token-generator",
    project_urls={
        "Documentation": "https://github.com/bakalari-api/python-token-generator/blob/master/README.md#návod",
        "Code": "https://github.com/bakalari-api/python-token-generator",
        "Issue tracker": "https://github.com/bakalari-api/python-token-generator/issues",
    },
    license="MIT License",
    author="Marian Šámal",
    author_email="margotka000@gmail.com",
    description="Jednoduchý Python script pro vygenerování tokenu pro Bakaláři API.",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Czech",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Education",
    ],
    py_modules=["bakalari_token"],
    entry_points={"console_scripts": ["bakalari-token=bakalari_token:cli"]},
)
