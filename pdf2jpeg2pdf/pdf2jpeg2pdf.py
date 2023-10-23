#!/usr/bin/env python3
"""A simple Python tool that convert PDF to JPEG and back to PDF."""
import os
import argparse
from pdf2image import convert_from_path

DEFAULT_DPI: int = 300


def get_unique_output_name(output_pdf: str) -> str:
    base_name, ext = os.path.splitext(output_pdf)
    count = 1
    while os.path.exists(output_pdf):
        output_pdf = f"{base_name}-{count}{ext}"
        count += 1
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

    # Check if output PDF already exists
    args.output = get_unique_output_name(args.output)

    return args


def pdf_to_jpeg_to_pdf(input_pdf_path, output_pdf_path, dpi=DEFAULT_DPI):
    images = convert_from_path(input_pdf_path, dpi=dpi)
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])


def main() -> int:
    args = parse_args()
    pdf_to_jpeg_to_pdf(args.input, args.output, dpi=args.dpi)
    print(f"Conversion complete. Output saved as {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
