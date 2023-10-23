import setuptools

setuptools.setup(
    name="pdf2jpeg2pdf",
    version="1.0",
    author="Constantinos Menelaou",
    license="MIT",
    description="A simple Python tool that convert PDF to JPEG and back to PDF.",
    install_requires=["pdf2image"],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'pdf2jpeg2pdf=pdf2jpeg2pdf.pdf2jpeg2pdf:main',
        ],
    },
)
