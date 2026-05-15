from setuptools import setup, find_packages

setup(
    name="companionkit",
    version="1.0.0",
    description="Self-developed AI companion framework with identity, emotion, memory, and verification",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Self-developed",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "emotionengine>=1.0.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="ai companion agent identity emotion memory",
)