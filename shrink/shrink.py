import os
from PIL import Image
import argparse

def shrink(image_path: str, output_dir: str = "output", scale: float = 0.5):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load input image
    try:
        img = Image.open(image_path)
    except Exception as e:
        raise ValueError(f"Error opening image: {e}")

    # Calculate new size
    new_width = int(img.width * scale)
    new_height = int(img.height * scale)

    # Resize image (Pillow 10+)
    img_shrunk = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Save shrunk image
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}_shrunk.png")
    img_shrunk.save(output_path)

    print(f"✅ Shrunk image saved: {output_path}")
    return output_path


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Shrink an image and save to output directory."
    )
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("output_dir", help="Directory to save the shrunk image")
    parser.add_argument("--scale", type=float, default=0.5,
                        help="Shrink scale (0.5 = 50% of original size)")

    args = parser.parse_args()
    shrink(args.image_path, args.output_dir, args.scale)
