# pdf2jpeg2pdf
A simple Python tool that convert PDF to JPEG and back to PDF.

Use this if you are going to print a PDF document with lots of vector images using the printer "HP® Officejet Pro X551dw". Trust me!

## Dependencies
- [pdf2image](https://pypi.org/project/pdf2image/)

## Installation
You can install the tool using git and pip:

```bash
git clone https://github.com/konmenel/pdf2jpeg2pdf.git
cd pdf2jpeg2pdf
pip install -e .
```

Extra steps might be needed depending on the Operating System as explained [here](https://pypi.org/project/pdf2image/). In short, follow the steps below.

### Mac
You need to install [poppler](https://poppler.freedesktop.org/):

```bash
brew install poppler
```

### Windows
You need to install poppler and add it to [PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).

The recommended version can be found [here](https://github.com/oschwartz10612/poppler-windows/releases/). Then add the `bin/` folder to the environment variable "PATH" as explained [here](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).

### Linux
Most likely you are good to go. However, if something is missing install `poppler-utils` from your package manager.

## Usage
```bash
pdf2jpeg2pdf [-h] [-o OUTPUT] [--dpi DPI] input
```

To convert a PDF (`input.pdf`) to JPEG and back to PDF (`output.pdf`) with DPI of 200, use the following command:

```bash
pdf2jpeg2pdf --output output.pdf --dpi 200 input.pdf
```

Print the help message for more info:

```bash
pdf2jpeg2pdf --help
```

## Arguments
- `input`: Path to the input PDF file.

## Options
- `-o`, `--output`: Path for the output PDF file. Default "\<input\>_jpeg.pdf".
- `--dpi`: DPI (dots per inch) for image conversion. Default 300.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/konmenel/pdf2jpeg2pdf/blob/main/LICENSE) file for details.

## Example
Running the following code from the root directory of the package will convert the PDF `Latex_tutorial.pdf` in the `example` directory file to JPEG images with a DPI of 300, then reassemble the images into a PDF named `Latex_tutorial.pdf` in the same directory.

```bash
pdf2jpeg2pdf --dpi 200 example/Latex_tutorial.pdf
```
