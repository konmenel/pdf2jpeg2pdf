# pdf2jpeg2pdf
A simple Python tool that convert PDF to JPEG and back to PDF

## Installation
You can install the tool using git and pip:

```bash
git clone https://github.com/konmenel/pdf2jpeg2pdf.git
cd pdf2jpeg2pdf
pip install -e .
```

## Dependencies
- [pdf2image](https://pypi.org/project/pdf2image/)

## Usage
To convert a PDF to JPEG and back to PDF, use the following command:
```bash
pdf2jpeg2pdf --output_pdf output.pdf --dpi 200 input.pdf
```

## Options
- `input`: Path to the input PDF file.
- `--output_pdf`: Path for the output PDF file (default is input PDF).
- `--dpi`: DPI (dots per inch) for image conversion (default is 200).

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/konmenel/pdf2jpeg2pdf/blob/main/LICENSE) file for details.

## Example
Running the following code from the root directory of the package will convert the PDF `Latex_tutorial.pdf` in the `example` directory file to JPEG images with a DPI of 300, then reassemble the images into a PDF named `Latex_tutorial.pdf` in the same directory.

```bash
pdf2jpeg2pdf --dpi 200 example/Latex_tutorial.pdf
```
