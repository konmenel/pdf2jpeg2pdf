#!/usr/bin/env python3
"""A simple Python tool that convert PDF to JPEG and back to PDF.

Example
-------
Running the following code from the root directory of the package will convert the PDF
`Latex_tutorial.pdf` in the `example` directory file to JPEG images with a DPI of 200,
then reassemble the images into a PDF named `Latex_tutorial.pdf` in the same directory.
```bash
python3 ./pdf2jpeg2pdf/pdf2jpeg2pdf.py --dpi 200 example/Latex_tutorial.pdf
```
"""
import os
import argparse
import itertools
from typing import Union
from pdf2image import convert_from_path

DEFAULT_DPI: int = 300


def get_unique_output_name(output_pdf: str) -> str:
    base_name, ext = os.path.splitext(output_pdf)
    for i in itertools.count(1):
        if not os.path.exists(output_pdf):
            break
        output_pdf = f"{base_name}-{i}{ext}"
    return output_pdf


def parse_args() -> argparse.Namespace:
    # Create the arguments
    parser = argparse.ArgumentParser(description="Convert PDF to JPEG and back to PDF")
    parser.add_argument("input", help="Path to the input PDF file")
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Path for the output PDF file. Default <input>_jpeg.pdf",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=DEFAULT_DPI,
        help=f"DPI (dots per inch) for image conversion. Default {DEFAULT_DPI}.",
    )

    # Parsing
    args = parser.parse_args()
    # Set default output PDF if not provided
    if args.output is None:
        args.output = os.path.splitext(args.input)[0] + "_jpeg.pdf"
    # Add .pdf extension if missing
    if not args.output.endswith(".pdf"):
        args.output += ".pdf"
    # If output file exist create a unique name
    args.output = get_unique_output_name(args.output)

    return args


def pdf_to_jpeg_to_pdf(
    input_pdf_path: Union[str, os.PathLike],
    output_pdf_path: Union[str, os.PathLike],
    dpi: int = DEFAULT_DPI,
) -> None:
    images = convert_from_path(input_pdf_path, dpi=dpi)
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])


def main() -> int:
    args = parse_args()
    pdf_to_jpeg_to_pdf(args.input, args.output, dpi=args.dpi)
    print(f"Conversion complete. Output saved as {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
